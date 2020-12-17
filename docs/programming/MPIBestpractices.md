## MPI Best practices
MPI or Message Passing Interface is a powerful library standard that allows for the parallel execution of applications across multiple processors on a system. It differs from other parallel execution libraries like OpenMP by also allowing a user to run their applications across multiple nodes. Unfortunately it can sometimes be a bit tricky to run a compiled MPI application within an HPC resource. The following page outlines best practices in running your MPI applications across Summit and Blanca resources.  

Please note that this page *does not* go over compiling or optimization of MPI applications.  

### MPI Compatible Compilers and Libraries

#### Loading the new Module Stack

Currently, only CURC’s older modules are visible within our base module stack. Luckily newer modules do exist within Summit and simply needs to be activated with a few commands. To see more newer versions of compilers and MPI libraries, simply run the following commands on a compute or compile node:  

```
source /curc/sw/opt/spack/linux-rhel7-haswell/gcc-4.8.5/lmod-8.3-pvwkxsyumgym34z7b7cq52uny77cfx4l/lmod/lmod/init/bashexport 
MODULEPATH=/curc/sw/modules/spack/spring2020/linux-rhel7-x86_64/Core
```

To return to the base module stack, simply exit the current node and return to a compile or compute node.  

#### Selecting your Compiler and MPI

The two families of compilers that are available to users of the system are Intel and GCC with Intel MPI and OpenMPI available respectively. To load Intel with Intel MPI or GCC with OpenMPI, run one the following commands from a job script or compile node.  

**Intel**

```
module load intel intel-mpi
```

or...

**GCC**

```
module load gcc openmpi

# Uncomment this additional line when adding this command to a JobScript!
# SLURM_EXPORT_ENV=ALL
```

It is important to note that GCC and OpenMPI should be paired with the `SLURM_EXPORT_ENV=ALL` environment variable when loading the pair into a job script. This will ensure the job can function when run on a login node!

In most situations you will want to try to compile and run your applications utilizing the Intel set of compilers and MPI libraries. Most cores on Summit and Blanca are of Intel architecture, so utilizing Intel will ensure the highest level of optimization comes from your compiler. GCC should only be utilized when your application cannot be compiled on intel software or if compiler specific optimizations exist within your code.  

### Commands to Run MPI Applications
Regardless of compiler or MPI distribution, there are 3 “wrapper” commands that will run MPI applications: `mpirun`, `mpiexec`, and `srun`. These “wrapper” commands should be used after loading in your desired compiler and MPI distribution and simply prepend whatever application you wish to run. Each command offers their own pros and cons alongside nuance as to how they function.  

`mpirun` is probably the most direct method to run MPI applications with the command being tied to the distribution. This means distribution dependent flags can be passed into the command as well as the command being the most reliable to work with:  

```
mpirun -np <core-count> ./<your-application>
```

`mpiexec` is a standardized MPI command execution command that allows for more general MPI flags to be passed. This means that commands you use of one MPI distribution can be used on another MPI distribution.  

```
mpiexec -np <core-count> ./<your-application>
```

The final command `srun` is probably the most abstracted away from a specific implementation. This command lets Slurm figure out specific MPI features that are available in your environment and handles running the process as a job. This command is usually a little less efficient and may have some issues in reliability.  

```
srun -n <core-count> ./<your-application>
```

RC usually recommends `mpirun` and `mpiexec` for simplicity and reliability when running MPI applications. `srun` should be used sparing to avoid issues with execution.

### Running MPI on Summit

Because Summit exists as a mostly homogeneous compute cluster, running MPI applications across nodes isn’t usually too troublesome.  

Simply select your Compiler/MPI and MPI wrapper command you wish to use, and place them all in a job script. Below is an example of what this can look like. In this example we run a 48 core, 4 hour job with the Intel compiler and Intel distribution of MPI:  

```
#!/bin/bash
#SBATCH --nodes=2
#SBATCH --time=04:00:00
#SBATCH --partition=shas
#SBATCH --ntasks=48
#SBATCH --job-name=mpi-job
#SBATCH --output=mpi-job.%j.out

source /curc/sw/opt/spack/linux-rhel7-haswell/gcc-4.8.5/lmod-8.3-pvwkxsyumgym34z7b7cq52uny77cfx4l/lmod/lmod/init/bashexport MODULEPATH=/curc/sw/modules/spack/spring2020/linux-rhel7-x86_64/Core

module purge
module load intel intel-mpi

#Run a 48 core job across 2 nodes:
mpirun -np $SLURM_NTASKS /path/to/mycode.exe

#Note: $SLURM_NTASKS has a value of the amount of cores you requested
```

### Running MPI on Blanca

Unlike Summit, Blanca is often a bit more complicated because of the diverse variety of nodes it is composed of. In general, there are 3 types of nodes on Blanca that can all run single node multi-core MPI processes that may require additional flags and parameters to achieve cross node parallelism.  

#### General Blanca Nodes
General Blanca nodes are not intended to run multi-node processes but this can still be achieved through the manipulation of some network fabric settings. In order to achieve cross node parallelism we must force MPI to utilize ethernet instead of our normal high speed network fabric. We can enforce this with various `mpirun` flags for each respective compiler.

**Intel**
```
mpirun -genv I_MPI_FABRICS shm:tcp
```
**OpenMPI** 
```
mpirun --mca btl tcp
```

Please note that this does not ensure high speed communications in message passing, but it will allow for basic parallelization across nodes.

#### ROCE Enabled Nodes
Some Blanca nodes are equipped with high speed network fabrics that are a bit more suited for cross node MPI processes. These nodes are labeled as *RoCE enabled* and require applications to be compiled with GCC 8.4.0 and OpenMPI_UCX 4.0.0 in order to function. Users should compile their applications using this compiler and MPI distribution that is found on Summit's base module stack.

If you are unsure if your node supports this feature then you can check by using the scontrol command on your node.  

```
scontrol show node <your-bnode>
```

You will be presented a block information that details all the nodes features. The key feature you should look for is `fdr`. If your Blanca node lacks this feature then it is not ROCE Enabled.  

#### Blanca HPC
Blanca HPC come equipped with high speed interconnects that would normally allow for high speed communication between nodes. These nodes currently only support Intel and Intel MPI compiler/MPI combo. Unfortunately there also exists a few issues regarding fabrics available to each node group so a bit of nuance must be had when running your applications.

Blanca HPC nodes can easily be distinguished from other Blanca nodes with the node's name in the cluster. Nodes will clearly be distinguished with the `bhpc` prefix.

There are currently 2 fabrics that can really be utilized within Blanca HPC depending on the node. The most efficient of these is the `ofi` fabric. Regardless of node, users should run a test job with this fabric to validate if it is supported on their nodes. You can do this with the following flag:   

**Intel**
```
mpirun -genv I_MPI_FABRICS shm:ofi
```
If this fabric returns an error then your jobs should function by loading the `ofa` fabric instead. This fabric can be loaded similarly with:  

**Intel**

```
mpirun -genv I_MPI_FABRICS shm:ofa
```
