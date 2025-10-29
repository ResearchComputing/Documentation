# Compiling and Linking

Before compiling in the RC environment, begin a compile job by using the `acompile` command. Next, load the modules corresponding to the compiler, MPI version (if needed), and any third-party libraries required by your application. The load order should always be compiler first, MPI second, and third-party libraries last.

For example, suppose your application requires MPI and the HDF5
library. To compile using the Intel compiler and Intel MPI, the
sequence of `module` commands would be:

```
module purge
module load intel
module load impi
module load hdf5
```

Supporting library-modules will be loaded as needed, and your
environment will be updated so that the appropriate library
directories are prepended to your `$PATH` and `$LD_LIBRARY_PATH`. The standard compiler variables `FC`, `CC` and `CXX` are set as appropriate for your compiler/MPI combination. These environment variables reference the Fortran, C, and C++ compilers respectively

In addition, several environment variables are set that may be useful during the compilation process.  These variables are prefixed by `CURC` and may easily be found by searching your environment for `CURC` via `env | grep CURC`. This will yield output similar to:

```
[johndoe@@c3cpu-a5-u17-2 ~]$ env | grep CURC
CURC_INTEL_INCLUDE=/curc/sw/install/intel/2024.2.1/mpi/2021.13/include
CURC_INTEL_INC=/curc/sw/install/intel/2024.2.1/mpi/2021.13/include
CURC_INTEL_ROOT=/curc/sw/install/intel/2024.2.1/mpi/2021.13
CURC_INTEL_LIB=/curc/sw/install/intel/2024.2.1/mpi/2021.13/lib
CURC_INTEL_BIN=/curc/sw/install/intel/2024.2.1/mpi/2021.13/bin
CURC_HDF5_INC=/curc/sw/install/hdf5/1.14.5/impi/2021.13/intel/2024.2.1/include
CURC_HDF5_LIB=/curc/sw/install/hdf5/1.14.5/impi/2021.13/intel/2024.2.1/lib
CURC_HDF5_ROOT=/curc/sw/install/hdf5/1.14.5/impi/2021.13/intel/2024.2.1
CURC_HDF5_BIN=/curc/sw/install/hdf5/1.14.5/impi/2021.13/intel/2024.2.1/bin
[...]
```

Once the relevant modules are loaded, you are ready to compile. For our HDF5 example, a compilation command that uses the environment variables set by the module system may look like:

```
$FC my_program.f90 -I$CURC_HDF5_INC -L$CURC_HDF5_LIB -lhdf5_fortran -o my_program
```

```{caution}
Your run-time environment should reflect your compilation environment. Be sure to include the same sequence of `module` commands in your job script as that used at compile time.
```


## Navigating the Software Stack

The RC module system is hierarchical in nature, and available software libraries become visible to the user only after the compiler and MPI implementations that they depend on have been loaded. As noted above, modules should be loaded in the order: compiler, MPI, third-party software.  At each stage of the load, executing `module avail` will reveal a list of newly available modules.  The `module purge` command can be used to unload all currently loaded modules (note that the software stack will be unavailable from login nodes).

For example, before choosing a compiler, we can view the available compilers with

```
[janedoe@c3cpu-a5-u17-2 ~]$ module purge
[janedoe@c3cpu-a5-u17-2 ~]$ module avail
```

This will yield output similar to

```
----------------------------------- Compilers --------------------------------------
  aocc/3.1.0 (D)    gcc/10.3.0    gcc/13.2.0        intel/2022.1.2 (m)    nvhpc_sdk/2021.213    nvhpc_sdk/2023.233 (D)    nvhpc_sdk/2025.255
  aocc/3.2.0        gcc/11.2.0    gcc/14.2.0 (D)    intel/2024.2.1 (D)    nvhpc_sdk/2022.229    nvhpc_sdk/2025.251
```

Several compiler-independent modules will also be displayed. Those modules (e.g., the Julia module) can be loaded at any time, irrespective of the compiler or MPI version in use.

If multiple versions of a package are available, a `D` is used to indicate the default version. When the version number is omitted during the `module load` command, the default version will be used. Considering the output above, the following two commands are equivalent:

```[janedoe@c3cpu-a5-u17-2 ~]$ module load intel ```

```[janedoe@c3cpu-a5-u17-2 ~]$ module load intel/2024.2.1 ```

Once the compiler is loaded, MPI-implementations and third-party
serial libraries that depend on that compiler appear in the available module list until `MPI Implementations` and `Compiler Dependent Applications`:

```
[janedoe@c3cpu-a5-u17-2 ~]$ module load intel
[janedoe@c3cpu-a5-u17-2 ~]$ module avail
----------------------------------- MPI Implementations --------------------------------------
    impi/2021.13
---------------------------------- Compiler Dependent Applications ---------------------------
   advisor/2024.2    debugger/2024.2.1    geos/3.13.0    jasper/4.2.4    mkl/2024.2          netcdf/4.9.2       proj/9.5.0       tiff/4.7.0
   boost/1.86.0      fftw/3.3.10          gsl/2.8        jpeg/9f         nco/5.2.9    (D)    openblas/0.3.28    sqlite/3.46.1    vtune/2024.2
   cdo/2.4.4         gdal/3.10.0          hdf5/1.14.5    libxc/7.0.0     ncview/2.1.7        openjpeg/2.5.2     szip/2.1.1       zlib/1.3.1
```

Choosing an MPI implementation will similarly reveal MPI-dependent software under the header `MPI Dependent Applications`:

```
[janedoe@c3cpu-a5-u17-2 ~]$ module load impi
[janedoe@c3cpu-a5-u17-2 ~]$ module avail
 ---------------------------------- MPI Dependent Applications -------------------
      QE/7.4.1    boost/1.86.0 (D)    fftw/3.3.10 (D)    hdf5/1.14.5 (D)    netcdf/4.9.2 (D)    petsc/3.22.1    pnetcdf/1.13.0
```

You may search for a particular software package using the `module spider` command. This is typically a two-stage process. First search on the general software name without including any version information. If the software exists on our system, a list of available versions will appear:

```
[janedoe@c3cpu-a5-u17-2 ~]$ module spider hdf5
----------------------------------------------------------------
  hdf5:
----------------------------------------------------------------
    Description:
      HDF5 Tools and Library

     Versions:
        hdf5/1.10.1
        hdf5/1.12.1
        hdf5/1.14.5
```

Finally, to see which modules must be loaded to make your desired version available, run the `module spider` command again with the version information included:

```
[janedoe@c3cpu-a5-u17-2 ~]$ module spider hdf5/1.14.5
------------------------------------------------------------------
  hdf5: hdf5/1.10.1
------------------------------------------------------------------
    Description:
      HDF5 Tools and Library

    This module can be loaded directly: module load hdf5/1.14.5

    Additional variants of this module can also be loaded after loading the following modules:

      gcc/14.2.0
      gcc/14.2.0  openmpi/5.0.6
      impi/2021.13
[...]
```


## Compiler and Optimization Recommendations

The Alpine cluster runs on AMD-designed hardware, whereas the Blanca cluster runs on Intel-designed hardware. As such, we **strongly recommend** using the appropriate compiler and MPI library when compiling software.  For production, we
suggest compiling with the `-O2` or `-O3` optimization flags along with the vectorization flags appropriate for the node you plan to run on. More compiler options and flags can be found in [AMD's reference guide](https://developer.amd.com/wp-content/resources/Compiler%20Options%20Quick%20Ref%20Guide%20for%20AMD%20EPYC%207xx3%20Series%20Processors.pdf). 

## Linking to the Math Kernel Library (MKL)

[The Intel Math Kernel Library
(MKL)](https://software.intel.com/en-us/mkl/documentation) provides optimized routines for a number of common mathematical
operations. Notably, it provides interfaces to the LAPack and BLAS linear algebra libraries as well as the FFTW Fourier transform package.

If you wish to link MKL to your Intel-compiled application, use the `-mkl` flag:

```
$CXX -O3 -xCORE-AVX2 my_program.cpp -o my_program.out -mkl
```

If your application uses FFTW, you will also need to include MKL's FFTW directory in your compilation command:

```
$CXX -O3 -xCORE-AVX2 -I$CURC_MKL_INC/fftw my_program.cpp -o my_program.out -mkl
```

For the GNU and PGI compilers, the link syntax becomes more
complex. [The Intel Link
Advisor](https://software.intel.com/en-us/articles/intel-mkl-link-line-advisor) can be used to generate the appropriate linking syntax based on your application's needs.

For the GNU compiler, linking against sequential MKL libraries, the appropriate Fortran linking syntax is:

```
$FC my_program.f90  -m64 -I$CURC_MKL_INC -o my_program.out  -L$CURC_MKL_LIB -Wl,--no-as-needed -lmkl_gf_lp64 -lmkl_sequential -lmkl_core -lpthread -lm -ldl
```

The comparable c/c++ syntax would be:

```
$FC my_program.cpp  -m64 -I$CURC_MKL_INC -o my_program.out   -L$CURC_MKL_LIB -Wl,--no-as-needed -lmkl_intel_lp64 -lmkl_sequential -lmkl_core -lpthread -lm -ldl
```

Note that if your application uses FFTW, you will must use the FFTW include flag just as with the Intel compiler. See the link advisor or submit a [support request form](https://colorado.service-now.com/req_portal?id=ucb_sc_rc_form), if you have additional questions about how to link MKL to your application.

