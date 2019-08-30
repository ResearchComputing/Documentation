##  Best practices for running parallel executables on RC Resources

Many scientific software packages are programmed such that they can parallelize tasks across multiple cores on one node (shared memory parallelization) or multiple cores across multiple nodes (distributed memory parallelization).  Either way, running the executable programs that result from compiling parallel-capable software packages requires the use of MPI ("message passing interface") libraries which coordinate the passing of information between the parallel tasks.

This documentation covers the best way to _run_ parallel executables on Summit and Blanca across multiple cores and nodes. Running a parallel executable on Summit or Blanca requires loading both a compiler and an mpi module, in addition to any other modules one needs.  Here the focus is on the two primary compiler/mpi module "combos": 1) Intel compilers with Intel-MPI (IMPI) and 2) Gnu (gcc) compilers with OpenMPI.  ___It is recommended that you always use the Intel/IMPI combo to compile and run your parallel software on Summit and Blanca, because Intel/IMPI-compiled codes typically run more efficiently. The gcc/OpenMPI combo can be used as a fallback if the code will not compile with Intel/IMPI.___

This documentation assumes you have already compiled your parallel software into an executable program.  Additonal information on compiling (and programming) MPI-capable software in [Fortran](https://curc.readthedocs.io/en/latest/programming/MPI-Fortran.html) and [C](https://curc.readthedocs.io/en/latest/programming/MPI-C.html) is provided in the RC documentation. ___To run your parallel executable you should always load and use the same compiler/mpi module combo that you used to compile it.___  



### Running parallel executables

Shared memory parallel codes (that run across multiple cores on a single node) can be run anywhere on Summit or Blanca.  Distributed memory parallel codes (that run across multiple cores _and_ multiple nodes) can be run on any Summit partition, as well as any Blanca-HPC partition (e.g.,`blanca-nso` and `blanca-topopt`) and the `blanca-ccn` partition.  If uncertain whether distributed memory parallel jobs can be run in a given Blanca partition, users can employ the `scontrol` command to query whether _fdr_ or _edr_ is an available feature for a random node in the partition-of-interest. For example, to check a node in the `blanca-ccn` partition: 
```
$ scontrol show node bnode0201 |grep AvailableFeatures
   AvailableFeatures=ivybridge,Quadro,K2000,avx,fdr,rhel7
   ```

#### With Intel/IMPI

__Step1__
Load the _intel_ and _impi_ modules. In this example _intel/17.4_ and _impi/17.3_ are loaded, but note that other options are also available and can be viewed with the `module avail` command.
```
module load intel/17.4
module load impi/17.3
```

__Step 2__
Export the following two environment variables:
```
export I_MPI_FABRICS=shm:ofi
export I_MPI_PMI_LIBRARY=/lib64/libpmi.so
```

__Step 3__
Now use one of the following three commands (`srun`, `mpirun`, or `mpiexec`) to invoke your parallel executable.  In this example the parallel executable is called _myexecutable.exe_ (yours will have a different name), and we are parallelizing across 2 cores (`-n 48`):
```
srun -n 48 ./myexecutable.exe
```
or
```
mpirun -n 48 ./myexecutable.exe
```
or
```
mpiexec -n 48 ./myexecutable.exe
```

In practice, all three methods will provide nearly identical performance, so choosing one is often a matter of preference. Slurm recommends using the `srun` command because it is best integrated with the Slurm Workload Manager that is used on both Summit and Blanca. Additional details on the use of `srun`, `mpirun` and `mpiexec` with _Intel-MPI_ can be found in the [Slurm MPI and UPC User's Guide](https://slurm.schedmd.com/mpi_guide.html#intel_mpi). 

#### With gcc/OpenMPI

__Step1__
Load the _gcc_ and _openmpi_ modules. In this example _gcc/6.1.0_ and _openmpi/2.0.1_ are loaded), but note that other options are also available and can be viewed with the `module avail` command.
```
module load gcc/6.1.0
module load openmpi/2.0.1
```

__Step 2__
Now use one of the following three commands (`srun`, `mpirun`, or `mpiexec`) to invoke your parallel executable. In this example the parallel executable is called _myexecutable.exe_ (yours will have a different name), and we are parallelizing across 2 cores (`-n 48`):
```
srun -n 48 ./myexecutable.exe
```
or
```
mpirun -n 48 ./myexecutable.exe
```
or
```
mpiexec -n 48 ./myexecutable.exe
```

In practice, all three methods will provide nearly identical performance, so choosing one is often a matter of preference. Slurm recommends using the `srun` command because it is best integrated with the Slurm Workload Manager that is used on both Summit and Blanca. Additional details on the use of `srun`, `mpirun` and `mpiexec` with _OpenMPI_ can be found in the [Slurm MPI and UPC User's Guide](https://slurm.schedmd.com/mpi_guide.html#open_mpi).

### Example job script for running a parallel executable:

```bash
#!/bin/bash

#SBATCH --nodes=2
#SBATCH --time=04:00:00
#SBATCH --qos=normal
#SBATCH --partition=shas
#SBATCH --ntasks=48
#SBATCH --job-name=mpi-job
#SBATCH --output=mpi-job.%j.out

module purge
module load intel/17.4
module load impi/17.3

#Run a 48 core job across 2 nodes:
srun -n $SLURM_NTASKS /path/to/mycode.exe
```

### Notes

* Software compiled with _intel/impi_ modules on Summit presently work on Blanca and visa-versa.
* Software compiled with _gcc/openmpi_ modules on Summit presently will not work on Blanca, and likely visa-versa, due to differences in the available shared libraries used for openmpi-based parallelization between the two systems. Therefore, when compiling software with _gcc/openmpi_ users should do so on the system they intend to use it on.
* When invoking _gcc/openmpi_-compiled softare via the `srun` command, make sure the code is compiled with _openmpi_ version 2.X or greater. 
* Other compiler/mpi combos are also available in the RC module stack.  For example, Portland Group (_pgi_) compilers are available with OpenMPI.  There are also _gcc/impi_ and _intel/openmpi_ combos available.  To explore options, first choose and load a compiler module (e.g., `intel/V.XX`, `gcc/V.XX` or `pgi/V.XX`) and then type `module avail` to see the list of MPI modules available for that particular compiler. 
* ___Tip___: you can substitute `-n $SLURM_NTASKS` for `-n 48` in the examples above, which will prevent you from having to change the number of tasks each time you change the number of _--ntasks_ requested in your job script.  The _$SLURM_NTASKS_ variable will automatically take on the value of the number of tasks requested.  







