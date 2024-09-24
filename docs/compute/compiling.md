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
CURC_INTEL_BIN=/curc/sw/intel/17.4/bin
CURC_INTEL_INC=/curc/sw/intel/17.4/include
CURC_INTEL_ROOT=/curc/sw/intel/17.4
CURC_INTEL_LIB=/curc/sw/intel/17.4/lib
CURC_HDF5_ROOT=/curc/sw/hdf5/1.10.1/impi/17.3/intel/17.4
CURC_HDF5_INC=/curc/sw/hdf5/1.10.1/impi/17.3/intel/17.4/include
CURC_HDF5_BIN=/curc/sw/hdf5/1.10.1/impi/17.3/intel/17.4/bin
CURC_HDF5_LIB=/curc/sw/hdf5/1.10.1/impi/17.3/intel/17.4/lib
[...]
```

Once the relevant modules are loaded, you are ready to compile. For our HDF5 example, a compilation command that uses the environment variables set by the module system may look like:

```
$FC my_program.f90 -I$CURC_HDF5_INC -L$CURC_HDF5_LIB -lhdf5_fortran -o my_program
```

> **Note:** Your run-time environment should reflect your compilation environment. Be sure to include the same sequence of `module` commands in your job script as that used at compile time.


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
   aocc/3.1.0 (D)    gcc/10.3.0        gcc/13.2.0            nvhpc_sdk/2021.213    nvhpc_sdk/2023.233 (D)
   aocc/3.2.0        gcc/11.2.0 (D)    intel/2022.1.2 (m)    nvhpc_sdk/2022.229
```

Several compiler-independent modules will also be displayed. Those modules (e.g., the Julia module) can be loaded at any time, irrespective of the compiler or MPI version in use.

If multiple versions of a package are available, a `D` is used to indicate the default version. When the version number is omitted during the `module load` command, the default version will be used. Considering the output above, the following two commands are equivalent:

```[janedoe@c3cpu-a5-u17-2 ~]$ module load intel ```

```[janedoe@c3cpu-a5-u17-2 ~]$ module load intel/2022.1.2 ```

Once the compiler is loaded, MPI-implementations and third-party
serial libraries that depend on that compiler appear in the available module list until `MPI Implementations` and `Compiler Dependent Applications`:

```
[janedoe@c3cpu-a5-u17-2 ~]$ module load intel
[janedoe@c3cpu-a5-u17-2 ~]$ module avail
----------------------------------- MPI Implementations --------------------------------------
   impi/2021.5.0
---------------------------------- Compiler Dependent Applications ---------------------------
    advisor/2022.0.0    gdal/3.4.2         hdf5/1.10.1                     jasper/4.0.0        nco/5.1.4       (D)    openjpeg/2.2.0        szip/2.1.1
   boost/1.78.0        gdal/3.5.0  (D)    hdf5/1.12.1              (D)    jpeg/9e             ncview/2.1.7           proj/6.0.0            tiff/4.3.0
   cdo/2.1.1           geos/3.10.2        intel_debugger/2021.5.0         libxc/5.2.2         netcdf/4.8.1           proj/8.2.1     (D)    vtune/2022.0.0
   fftw/3.3.10         gsl/2.7            intel_inspector/2022.0.0        mkl/2022.0.2 (m)    openblas/0.3.20        sqlite/3.38.01        zlib/1.2.11
```

Choosing an MPI implementation will similarly reveal MPI-dependent software under the header `MPI Dependent Applications`:

```
[janedoe@c3cpu-a5-u17-2 ~]$ module load impi
[janedoe@c3cpu-a5-u17-2 ~]$ module avail
 ---------------------------------- MPI Dependent Applications -------------------
   QE/7.0       (D)    epw/6.0alpha        hdf5/1.10.1          lammps/29Sep21                      netcdf/4.8.1 (D)    pnetcdf/1.12.2
   QE/7.2              fftw/3.3.8          hdf5/1.12.1   (D)    lammps/29Sep2021_update3            opensees/3.4        yambo/5.2.2
   boost/1.78.0 (D)    fftw/3.3.10  (D)    lammps/2Aug23        lammps/29Sep2021_update3.1.1 (D)    petsc/3.18.3
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
```

Finally, to see which modules must be loaded to make your desired version available, run the `module spider` command again with the version information included:

```
[janedoe@c3cpu-a5-u17-2 ~]$ module spider hdf5/1.10.1
------------------------------------------------------------------
  hdf5: hdf5/1.10.1
------------------------------------------------------------------
    Description:
      HDF5 Tools and Library

    You will need to load all module(s) on any one of the lines below before
    the "hdf5/1.10.1" module is available to load.

      intel/2022.1.2
      intel/2022.1.2  impi/2021.5.0
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

Note that if your application uses FFTW, you will must use the FFTW include flag just as with the Intel compiler. See the link advisor or contact <rc-help@colorado.edu> if you have additional questions about how to link MKL to your application.

