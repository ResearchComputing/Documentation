## Gaussian

__Important:__ Gaussian is available on Summit only to members of
universities that have purchased Gaussian licenses. It cannot be run
by other Summit users. Please note and abide by the licensing,
rights, and citation information shown at the top of your Gaussian
output files.

This document describes how to run G16 jobs efficiently on
Summit. It does not attempt to teach how to use Gaussian for solving
science/engineering questions.

Good general instructions can be found at
[here](http://gaussian.com/running/); however some minor modifications
are needed when running on Summit.


### Environment

To set up your shell environment to use G16, load a Gaussian software
module (e.g. `module load gaussian/16_avx2`). Nearly all necessary
environment variables are configured for you via the module. You do
not need to source g16.login or g16.profile if running single-node jobs, but if you are running multi-node parallel jobs you will need to add `source $g16root/g16/bsd/g16.login` (tcsh shell) or `source $g16root/g16/bsd/g16.profile` (bash shell) to your job script after you load the Gaussian module.

However, it is important to specify `GAUSS_SCRDIR` to tell G16 where
to put its large scratch files. These should always be on a [scratch storage system](../compute/filesystems.html)
(`/scratch/summit/$USER` on Summit or `rc_scratch/$USER` on Blanca.) If `GAUSS_SCRDIR` is not set, then the
scratch files will be created in whatever directory G16 is run from;
if this directory is in `/projects` or `/home`, then your job's
performance will be dramatically reduced.


### Running G16

If you create a Gaussian input file named h2o_dft.com then you can
execute it simply via `g16 h2o_dft`. Output from the computation will
go to a file called h2o_dft.log.


### Memory

The default dynamic memory request in G16 is frequently too small to
support the amount of memory that needs to be allocated to efficiently
support computations on even modest-sized molecules. If too little
memory is requested, the job can crash. Thus, use the '-m' flag in
your g16 command line (e.g. `-m=48gb`) to specify at least 50% of
the amount of memory your Slurm job has requested.


### Parallel jobs


#### Single-node (SMP) parallelism

Many G16 functions scale well to 8 or more cores on the same node. You
can specify how many cores to use via the '-p' flag to g16
(e.g. `-p=24`). This value should correspond to the number of cores
that your Slurm job has requested. You should test your G16
computations with several different core counts to see how well they
scale, as there may be diminishing returns beyond a certain number of
cores.

__Example SMP BASH script:__

```bash
#!/bin/bash

#SBATCH --job-name=g16-test
#SBATCH --partition=shas
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=24
#SBATCH --time=00:50:00
#SBATCH --output=g16-test.%j.out

module load gaussian/16_avx2

# Always specify a scratch directory on a fast storage space (not /home or /projects!)
export GAUSS_SCRDIR=/scratch/summit/$USER/$SLURM_JOBID
# or export GAUSS_SCRDIR=$SLURM_SCRATCH
# alternatively, to use the local SSD; max 159GB available

# the next line prevents OpenMP parallelism from conflicting with Gaussian's internal SMP parallelization
export OMP_NUM_THREADS=1

mkdir $GAUSS_SCRDIR  # only needed if using /scratch/summit
date  # put a date stamp in the output file for timing/scaling testing if desired
g16 -m=50gb -p=24 my_input.com
date
```


#### Multi-node (Linda) parallelism

In order to run on more than 24 cores in the "shas" partition on
Summit, your job will need to span multiple nodes using the Linda
network parallel communication model. We advise using one Linda worker
per node, with multiple SMP cores per node. For example, your g16
flags might include

```bash
-p=24 -s=ssh -w=shas0521-opa,shas0604-opa,shas0622-opa
```

which tells G16 to use 24 cores on each of three shas nodes, and to
set up the connections between nodes using ssh.

Since you don't know in advance what nodes your job will be assigned
to, you will have to determine the arguments for '-w' at runtime via
commands in your Slurm batch script. See the batch script example
below.

Not all G16 computations scale efficiently beyond a single node!
According to the G16 documentation: "HF, CIS=Direct, and DFT
calculations are Linda parallel, including energies, optimizations,
and frequencies. TDDFT energies and gradients and MP2 energies and
gradients are also Linda parallel. Portions of MP2 frequency and CCSD
calculations are Linda parallel." As with SMP parallelism, testing the
scaling of your Linda parallel computation is very important.

__Linda Parallel__

```bash
#!/bin/bash

#SBATCH --job-name=g16-test
#SBATCH --partition=shas
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=24
#SBATCH --time=00:50:00
#SBATCH --output=g16-test.%j.out

module load gaussian/16_avx2
source $g16root/g16/bsd/g16.profile

for n in `scontrol show hostname | sort -u`; do
 echo ${n}-opa
done | paste -s -d, > tsnet.nodes.$SLURM_JOBID

# Always specify a scratch directory on a fast storage space (not /home or /projects!)
export GAUSS_SCRDIR=/scratch/summit/$USER/$SLURM_JOBID

# the next line prevents OpenMP parallelism from conflicting with Gaussian's internal parallelization
export OMP_NUM_THREADS=1

# the next line increases the verbosity of Linda output messages
export GAUSS_LFLAGS="-v"

mkdir $GAUSS_SCRDIR  # only needed if using /scratch/summit
date  # put a date stamp in the output file for timing/scaling testing
g16 -m=20gb -p=24 -w=`cat tsnet.nodes.$SLURM_JOBID` my_input.com
date
rm tsnet.nodes.$SLURM_JOBID
```


#### G16 on GPU

Please read [http://gaussian.com/running/?tabid=5](http://gaussian.com/running/?tabid=5) carefully to
determine whether the K80 GPUs in Summit's "sgpu" partition will be
effective for your calculations. In many cases, SMP parallelization
across all of the cores in a shas node will provide better speedup
than offloading computational work to a GPU.


#### G16 on Knight's Landing

We do not recommend running Gaussian16 on RMACC Summit's "sknl"
partition.

### Sample input file

Here's an input file that can be used for both SMP and Linda parallel
testing:

```
#P b3lyp/6-31g* test stable=(opt,qconly)

Gaussian Test Job 135:
Fe=O perpendicular to ethene, in triplet state.

0 3
X
Fe X  RXFe
C1 X  RXC  Fe  90.
C2 X  RXC  Fe  90.  C1  180.
O  X  RXO  C1  90.  Fe	0.
H1 C1 RCH  C2 CCH   Fe  Angle1
H2 C1 RCH  C2 CCH   Fe -Angle1
H3 C2 RCH  C1 CCH   Fe  Angle2
H4 C2 RCH  C1 CCH   Fe -Angle2

RXFe  1.7118
RXC   0.7560
RXO   3.1306
RCH   1.1000
Angle1 110.54
Angle2 110.53
CCH   117.81
```

Couldn't find what you need? [Provide feedback on these docs!](https://docs.google.com/forms/d/1WoP_KtLp9lnTEsgW7Os-we45_JbEt3aUgS6j61jARnk/edit)
