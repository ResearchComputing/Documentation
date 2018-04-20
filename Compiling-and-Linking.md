## Table of Contents

- [The Compilation Environment](#the-compilation-environment)
- [Compilation Examples](#compilation-examples)

## The Compilation Environment

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
