##  Best practices for using MPI on RC Resources

Many scientific software packages are programmed such that they can parallelize tasks across multiple cores on one node (shared memory parallelization) or multiple cores across multiple nodes (distributed memory parallelization).  Either way, running the executable programs that result from compiling parallel-capable software packages requires the use of MPI ("message passing interface") libraries which coordinate the passing of information between the parallel tasks.

This documentation covers the best way to _run_ parallel executables on Summit and Blanca across multiple cores and nodes. Running a parallel executable on Summit or Blanca requires loading both a compiler and an mpi module, in addition to any other modules one needs.  Here the focus is on the two primary compiler/mpi module "combos": 1) Intel compilers with Intel-MPI (IMPI) and 2) Gnu (gcc) compilers with OpenMPI.  _It is recommended that you always use the Intel/IMPI to compile and run your parallel software on Summit and Blanca, because Intel/IMPI-codes typically run more efficiently. The gcc/OpenMPI combo can be used as a fallback if the code will not compile with Intel/IMPI._

This documentation assumes you have already compiled your parallel software into an executable.  Additonal information on compiling (and programming) MPI-capable software in [Fortran](https://curc.readthedocs.io/en/latest/programming/MPI-Fortran.html) and [C](https://curc.readthedocs.io/en/latest/programming/MPI-C.html) is provided in the RC documentation. _To run your parallel executable you should always load and use the same compiler/mpi module combo that you used to compile it._  



### XXX

Text Here.

#### Subcategory

Text here.
