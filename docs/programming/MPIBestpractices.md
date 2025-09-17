# MPI Best practices
MPI, or Message Passing Interface, is a powerful library standard that allows for the parallel execution of applications across multiple processors on a system. It differs from other parallel execution libraries like OpenMP by also allowing a user to run their applications across multiple nodes. Unfortunately it can sometimes be a bit tricky to run a compiled MPI application within an HPC resource. The following page outlines best practices in running your MPI applications across CURC resources.  

```{attention}
Please note that this page *does not* cover compiling or optimization of MPI applications.  
```

## MPI Compatible Compilers and Libraries

### Selecting your Compiler and MPI

Several families of compilers are available to users: Intel, GCC, and AOCC _(Alpine only)_.  Intel compilers have Intel MPI available for messsage passing, and GCC and AOCC compilers have OpenMPI available for message passing. To load a compiler/MPI combo run one the following commands from a job script or compile node (note that you should subsitute the version you need for `<version>` in the examples below; available compiler versions can be seen by typing `module avail`):


(tabset-ref-mpi-best-compiler)=
`````{tab-set}
:sync-group: tabset-mpi-best-compiler

````{tab-item} Intel
:sync: mpi-best-compiler-intel

```bash
module load intel/<version> impi
```

````

````{tab-item} GCC
:sync: mpi-best-compiler-gcc

```bash
module load gcc/<version> openmpi

# Uncomment this additional line when adding this command to a JobScript!
# SLURM_EXPORT_ENV=ALL
```

````

````{tab-item} AOCC
:sync: mpi-best-compiler-aocc

```bash
module load aocc/<version> openmpi

# Uncomment this additional line when adding this command to a JobScript!
# SLURM_EXPORT_ENV=ALL
```

````

`````

```{important}
It is important to note that use of OpenMPI should be paired with the `SLURM_EXPORT_ENV=ALL` environment variable to ensure the job can function when scheduled from a login node!
```

```{note}
On Blanca, in most situations you will want to try to compile and run your applications utilizing the Intel set of compilers and MPI libraries. Most CPUs on Blanca are of Intel architecture, so utilizing Intel will ensure the highest level of optimization comes from your compiler. GCC should only be utilized when your application cannot be compiled on intel software or if compiler specific optimizations exist within your code. We do not yet have compiler/MPI recommendations for Alpine, which has AMD CPUs. 
```

## Commands to Run MPI Applications
Regardless of compiler or MPI distribution, there are 3 “wrapper” commands that will run MPI applications: `mpirun`, `mpiexec`, and `srun`. These “wrapper” commands should be used after loading in your desired compiler and MPI distribution and simply prepend whatever application you wish to run. Each command offers their own pros and cons alongside nuance as to how they function.


(tabset-ref-mpi-best-prac-run)=
`````{tab-set}
:sync-group: tabset-mpi-best-prac-run

````{tab-item} mpirun
:sync: mpi-best-prac-run-mpirun

`mpirun` is probably the most direct method to run MPI applications with the command being tied to the distribution. This means distribution dependent flags can be passed directly through the command.   

```bash
mpirun -np <core-count> ./<your-application>
```

````

````{tab-item} mpiexec
:sync: mpi-best-prac-run-mpiexec

`mpiexec` is a standardized MPI command execution command that allows for more general MPI flags to be passed. This means that commands are universal across all distributions.

```bash
mpiexec -np <core-count> ./<your-application>
```

````

````{tab-item} srun
:sync: mpi-best-prac-run-srun

The final command `srun` is probably the most abstracted away from a specific implementation. This command lets Slurm figure out specific MPI features that are available in your environment and handles running the process as a job. This command is usually a little less efficient and may have some issues with reliability. 

```bash
srun -n <core-count> ./<your-application>
```

````
`````

```{note}
RC usually recommends `mpirun` and `mpiexec` for simplicity and reliability when running MPI applications. `srun` should be used sparingly to avoid issues with execution.
```

## Running MPI on Alpine

Running MPI jobs on Alpine is relatively straightforward. However, one caveat on Alpine is that MPI jobs cannot be run across chassis, which limits them to a maximum `--ntask` count of 4096 cores (64 nodes per chassis * 64 cores each).

Simply select the Compiler and MPI wrapper you wish to use and place it in a job script. In the following example, we run a 128 core, 4 hour job with a gcc compiler and OpenMPI:  

```
#!/bin/bash
#SBATCH --nodes=2
#SBATCH --time=04:00:00
#SBATCH --partition=amilan
#SBATCH --qos=normal
#SBATCH --constraint=ib
#SBATCH --ntasks=128
#SBATCH --job-name=mpi-job
#SBATCH --output=mpi-job.%j.out

module purge
module load gcc/10.3 openmpi
  
export SLURM_EXPORT_ENV=ALL

#Run a 128 core job across 2 nodes:
mpirun -np $SLURM_NTASKS /path/to/mycode.exe

#Note: $SLURM_NTASKS has a value of the amount of cores you requested
```

```{important}
When running MPI jobs on Alpine, you can use the `--constraint=ib` flag to force the job onto an Alpine node that has Infiniband, the networking fabric used by MPI.

To ensure optimal MPI performance and proper task placement, always explicitly specify the number of nodes with the `--nodes` flag. For example:
- Use `--nodes=1` if you're using up to 64 cores (one full node).
- Use `--nodes=2` and `--ntasks=128` for 128-core jobs.
Continue scaling by full nodes to maintain efficient communication (e.g., nodes=4 for 256 tasks, etc.).
```

## Running MPI on Blanca

Blanca is often a bit more complicated due to the variety of nodes available. In general, there are 3 types of nodes on Blanca that can all run single node multi-core MPI processes that may require additional flags and parameters to achieve cross node parallelism.  

```{important}
As with Alpine, it's recommended to explicitly specify the number of nodes using `nodes` along with `ntasks`, especially for multi-node MPI jobs. Blanca nodes may have different core counts depending on the hardware configuration, so be sure to match your `ntasks` to the number of cores available per node. You can check a node's core count using `scontrol show node <node-name>`.
```

### General Blanca Nodes
General Blanca nodes are not intended to run multi-node processes but this can still be achieved through the manipulation of some network fabric settings. In order to achieve cross node parallelism we must force MPI to utilize ethernet instead of our normal high speed network fabric. We can enforce this with various `mpirun` flags for each respective compiler.


(tabset-ref-mpi-best-prac-blanca)=
`````{tab-set}
:sync-group: tabset-mpi-best-prac-blanca

````{tab-item} Intel Single-Node Jobs
:sync: mpi-best-prac-blanca-intel-sing

```bash
mpirun -genv I_MPI_FABRICS=shm
```
````

````{tab-item} Intel Multi-Node Jobs
:sync: mpi-best-prac-blanca-intel-mult

Constrain Jobs to EDR IB (InfiniBand)

```bash
mpirun -genv I_MPI_FABRICS=edr
```

````

````{tab-item} Open MPI
:sync: mpi-best-prac-blanca-openmpi

```bash
mpirun --mca btl tcp <other arguments>
```

````


`````

```{note}
This does not ensure high speed communications in message passing, but it will allow for basic parallelization across nodes.
```

### Blanca HPC
Blanca HPC comes equipped with InfiniBand high speed interconnects that allow for high speed communication between nodes. These nodes supoort the Intel and Intel MPI compiler/MPI combo, as well as the `gcc`/`openmpi_ucx` modules _(note: bve sure to use the *ucx* version of the OpenMPI module)_. 

Blanca HPC nodes can easily be distinguished from other Blanca nodes with the node's name in the cluster. Nodes will clearly be distinguished with the `bhpc` prefix.  They also will have the `edr` feature in their feature list if you query them with `scontrol show node`. If you are using Open MPI, jobs on  Blanca HPC nodes can be run using `mpirun` without any special arguments, although be sure to `export SLURM_EXPORT_ENV=ALL` prior to invoking `mpirun`.  If you are using IMPI, select the `ofa` (Open Fabrics Alliance) option to enable Infiniband-based message passing, the fastest interconnect availble on the `bhpc` nodes. You can do this with the following flag: 

```
mpirun -genv I_MPI_FABRICS shm:ofa <other arguments>
```
  
 
### ROCE Enabled Nodes
The nodes in Blanca chassis 5 (nodes named `bnode05<NN>`) are equipped with high speed network fabrics that are more suited for cross node MPI processes. These nodes are labeled as *RoCE enabled* and require applications to be compiled with UCX-enabled openmpi modules, which are available with both `gcc/8.2.0` and `gcc/10.2.0`.

If you are unsure if your node supports RoCE feature then you can check by using the scontrol command on your node.  

```
scontrol show node <your-bnode>
```

You will be presented a block information that details all the nodes features. The key feature you should look for is `fdr`. If your Blanca node lacks this feature then it is not ROCE Enabled.  Jobs on RoCE nodes can be run using `mpirun` without any special arguments, although be sure to `export SLURM_EXPORT_ENV=ALL` prior to invoking `mpirun`. 


