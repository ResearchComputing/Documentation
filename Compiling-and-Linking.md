## Table of Contents

- [Overview](#overview)
- [Navigating the Software Stack](#navigating-the-software-stack)
- [Compilation Examples](#compilation-examples)

## Overview

Before compiling in the RC environment, first ssh to one of the Summit compile nodes via `ssh scompile`.  Next, load modules those modules corresponding to the compiler, MPI version (if needed), and third-party libraries required by your application.   The load order should always be compiler first, MPI second, and third-party libraries last.

For example, suppose your application requires MPI and the HDF5 library.  To compile using the Intel compiler and Intel MPI, the sequence of `module` commands would be:
``` 
module purge
module load intel
module load impi
module load hdf5
```
Supporting library-modules will be loaded as needed, and your environment will be updated so that the appropriate library directories are prepended to your `$PATH` and `$LD_LIBRARY_PATH`.  The standard compiler variables `FC`, `CC` and `CXX` are set as appropriate for your compiler/MPI combination.  These environment variables reference to the Fortran, C, and C++ compilers respectively

In addition, several environment variables are set that may be useful during the compilation process.   These variables possess the prefix `CURC` and may easily be found by searching your environment for `CURC` via `env | grep CURC`.  This will yield output similar to:
```
[johndoe@shas0137 ~]$ env | grep CURC
CURC_INTEL_BIN=/curc/sw/intel/17.4/bin
CURC_INTEL_INC=/curc/sw/intel/17.4/include
CURC_INTEL_ROOT=/curc/sw/intel/17.4
CURC_INTEL_LIB=/curc/sw/intel/17.4/lib
CURC_HDF5_ROOT=/curc/sw/hdf5/1.10.1/impi/17.3/intel/17.4
CURC_HDF5_INC=/curc/sw/hdf5/1.10.1/impi/17.3/intel/17.4/include
CURC_HDF5_BIN=/curc/sw/hdf5/1.10.1/impi/17.3/intel/17.4/bin
CURC_HDF5_LIB=/curc/sw/hdf5/1.10.1/impi/17.3/intel/17.4/lib
...
``` 
Once the relevant modules are loaded, you are ready to compile.  For our HDF5 example, a compilation command that uses the environment variables set by the module system may look like:
```
$FC my_program.f90 -I$(CURC_HDF5_INC) -L$(CURC_HDF5_LIB) -lhdf5_fortran -o my_program
```
**Note:** Your run-time environment should reflect your compilation environment.   Be sure to include the same sequence of `module` commands in your job script as that used at compile time.



## Navigating the Software Stack

Compilation on RC systems works hand-in-hand with the Lmod module system.  Detailed of semantics of Lmod are discussed in **LINK HERE**, and we only discuss some key points of the module system here.  Namely, modules should be loaded in a certain order,  loading a module modifies the `PATH` and `LD_LIBRARY_ENVIRONMENT` variables, and certain RC-specific environment variables are set which may be useful during the compilation process.

### Choosing a Compiler
Before compiling, we suggest that you clear any loaded modules from memory:

```[janedoe@shas0136 ~]$ ml purge ```

Next, you can view the available compilers, as well as compiler-independent modules via:

 ```[janedoe@shas0136 ~]$ ml avail 
----------------------------------- Compilers --------------------------------------
   gcc/6.1.0    intel/16.0.3 (m)    intel/17.0.0 (m)    intel/17.4 (m,D)    pgi/16.5
```
If multiple versions of a particular compiler are available, the `D` denotes the default version.  If the version number is omitted in the `module load` command, this is the version that will be used.  In the example above, the following two commands are equivalent:

```[janedoe@shas0136 ~]$ ml intel ```


```[janedoe@shas0136 ~]$ ml intel/17.4 ```

Once the compiler is loaded, MPI-implementations and third-party serial libraries that have been built using that compiler appear in the available module list:
  ```[janedoe@shas0136 ~]$ ml avail 
----------------------------------- MPI Implementations --------------------------------------
   impi/17.3
---------------------------------- Compiler Dependent Applications ---------------------------
   antlr/2.7.7    gdal/2.2.1    gsl/2.4        hdf5/1.10.1              (D)    jasper/1.900.1    mkl/17.3  (m)    ncview/2.1.7      openjpeg/2.2.0    szip/2.1.1
   fftw/3.3.4     geos/3.6.2    hdf5/1.8.18    intel_cluster_tools/17.3        jpeg/9b           nco/4.6.0        netcdf/4.4.1.1    proj/4.9.2        zlib/1.2.11

```
Choosing an MPI implementation will similarly reveal third-party software compiled against the particular compiler/MPI-implementation you have selected:
