# Alpine Software

## Software Installed on Alpine

This list includes the software applications, compilers, libaries, and software development kits (SDKs) installed as modules on CURC Alpine. 

Refer to our [Modules System](https://curc.readthedocs.io/en/latest/compute/modules.html) page for instructions on how to view and load software.

| Application           | Version(s)          | Description      |
| --------------------- | ------------------- | ---------------- |
| [Abaqus](https://www.3ds.com/products-services/simulia/products/abaqus/) (L) | V6R2019x | Abaqus FEA is a software suite for finite element analysis and computer-aided engineering.|  
| [Allinea DDT](https://developer.nvidia.com/allinea-ddt) | 6.0.4 | Graphical debugging tool for single-process, OpenMP, and MPI applications.| 
| [Anaconda](https://www.anaconda.com/products/distribution) | 2020.11, 2022.10 (D) | Anaconda is a distribution of the Python and R programming languages for scientific computing, that aims to simplify package management and deployment. [CURC Usage Guide](https://curc.readthedocs.io/en/latest/software/python.html)| 
| [Ansys](https://www.ansys.com/) (L,G) | EM21.2, EM22.2 | CAE/multiphysics engineering simulation software for product design, testing and operation.|
| [Arm Forge](https://developer.arm.com/Tools%20and%20Software/Arm%20Forge) | 19.1.3 | Arm Forge is a server and HPC development tool suite for C, C++, Fortran, and Python high performance code on Linux.|
| [AOCC](https://www.amd.com/en/developer/aocc.html) | 3.1.0 (D), 3.2.0 |The AMD Optimizing C/C++ and Fortran Compilers (“AOCC”) are a set of production compilers optimized for software performance when running on AMD host processors using the AMD “Zen” core architecture.| 
| [AOCL](https://www.amd.com/en/developer/aocl.html) | 3.2.0 |AOCL is a set of numerical libraries optimized for AMD processors based on the AMD “Zen” core architecture and generations.| 
| [Autotools](https://www.gnu.org/software/automake/faq/autotools-faq.html) | 2.6.9, 2.7.1 (D)| The GNU Autotools, also known as the GNU Build System, is a suite of programming tools designed to assist in making source code packages portable to many Unix like systems.|
| [boost](https://www.boost.org/) | 1.78.0 | Boost provides free peer-reviewed portable C++ source libraries.| 
| [CDO](https://code.mpimet.mpg.de/projects/cdo/) | 2.1.1 | CDO is a collection of command line Operators to manipulate and analyse Climate and NWP model Data.|
| [ChimeraX](https://www.cgl.ucsf.edu/chimerax/) | 1.2.5 | A next-generation molecular visualization program. | 
| [CMake](https://cmake.org/) | 3.5.2, 3.9.2, 3.14.1, 3.20.2, 3.25.0 (D) | CMake is an open-source, cross-platform family of tools designed to build, test and package software.| 
| [Coreform Cubit](https://coreform.com/products/coreform-cubit/) (L)| Coreform-Cubit-2021.5 | Coreform Cubit is a comprehensive toolset for high-quality FEA and CFD mesh generation that provides a similar user experience as GAMBIT.| 
| [CP2K](https://www.cp2k.org/) | 2023.1 | CP2K is a quantum chemistry and solid state physics software package that can perform atomistic simulations of solid state, liquid, molecular, periodic, material, crystal, and biological systems.|
| [CST Studio Suite](https://www.3ds.com/products-services/simulia/products/cst-studio-suite/) (L) | 2021 | CST Studio Suite is a high-performance 3D EM analysis software package for designing, analyzing and optimizing electromagnetic (EM) components and systems. | 
| [Cube](https://www.scalasca.org/scalasca/software/cube-4.x/download.html) | 3.4.3, 4.3.4 (D) | Cube, which is used as performance report explorer for Scalasca and Score-P, is a generic tool for displaying a multi-dimensional performance space. | 
| [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit) (G) | 11.2, 11.3 (D), 11.4 | The NVIDIA CUDA Toolkit includes GPU-accelerated libraries, debugging and optimization tools, a C/C++ compiler, and a runtime library to deploy your application. | 
| [cuDNN](https://developer.nvidia.com/cudnn) (G)| 8.1, 8.2 (D)| The NVIDIA CUDA Deep Neural Network library (cuDNN) is a GPU-accelerated library of primitives for deep neural networks. | 
| [curc-quota](https://curc.readthedocs.io/en/latest/compute/filesystems.html#monitoring-disk-usage) | 5.0 | CU Boulder script that provides information the user's home, projects, scratch, and PetaLibrary space.| 
| [DMTCP](https://dmtcp.sourceforge.io/) | 2.6.0 | DMTCP (Distributed MultiThreaded Checkpointing) transparently checkpoints a single-host or distributed computation in user-space without modifications to user code or to the O/S.|
| [Eigen](https://eigen.tuxfamily.org/index.php?title=Main_Page) | 3.4.0 | Eigen is a C++ template library for linear algebra: matrices, vectors, numerical solvers, and related algorithms.|
| [Emacs](https://www.gnu.org/software/emacs/) | 25.3, 27.2 (D) | An extensible, customizable, text editor.|
| [Expat](https://libexpat.github.io/) | 2.1.1, 2.3.0 (D) | Stream-oriented XML parser library written in C.| 
| [FFmpeg](https://ffmpeg.org/) | 4.4 | A complete, cross-platform solution to record, convert and stream audio and video.| 
| [FFTW](https://www.fftw.org/) | 3.3.8, 3.3.9, 3.3.10 | FFTW is a C subroutine library for computing the discrete Fourier transform (DFT) in one or more dimensions, of arbitrary input size, and of both real and complex data.|
| [Gaussian 16](https://gaussian.com/gaussian16/) (L,G) | 16_avx2 | Guassian 16 provides state-of-the-art capabilities for electronic structure modeling. [CURC Usage Guide](https://curc.readthedocs.io/en/latest/software/gaussian.html)|
| [gcc](https://gcc.gnu.org/) |  10.3.0, 11.2.0 (D) |The GNU Compiler Collection includes front ends for C, C++, Objective-C, Fortran, Ada, Go, and D, as well as libraries for these languages (libstdc++,...).| 
| [GDAL](https://gdal.org/) | 3.4.2, 3.5.0 | GDAL is a translator library for raster and vector geospatial data formats.| 
| [GDB](https://www.sourceware.org/gdb/) | 8.1, 10.1 (D) | GDB, the GNU Project debugger, allows you to see what is going on 'inside' another program while it executes -- or what another program was doing at the moment it crashed.|
| [GEOS](https://libgeos.org/) | 3.9.1, 3.10.2 | GEOS is a C/C++ library for computational geometry with a focus on algorithms used in geographic information systems (GIS) software.|
| [Ghostscript](https://ghostscript.com/index.html) | 9.56.0 |Ghostscript is an interpreter for the PostScript language and PDF files.| 
| [Git](https://git-scm.com/downloads) | 2.31.0 | Git is a distributed version control system that tracks changes in any set of computer files.| 
| [Gmsh](https://gmsh.info/) | 2.16.0, 4.11.1 (D) | Gmsh is an open source 3D finite element mesh generator with a built-in CAD engine and post-processor.|
| [GNU Parallel](https://www.gnu.org/software/parallel/) | 20160622, 20210322 (D) | GNU parallel is a shell tool for executing jobs in parallel using one or more computers. [CURC Usage Guide](https://curc.readthedocs.io/en/latest/software/GNUParallel.html)| 
| [gnuplot](http://www.gnuplot.info/) | 5.4.3 | gnuplot is a command-line and GUI program that can generate two- and three-dimensional plots of functions, data, and data fits.| 
| [GROMACS](https://www.gromacs.org/) (G) | 2022.4 | GROMACS is a molecular dynamics package mainly designed for simulations of proteins, lipids, and nucleic acids.| 
| [GSL](https://www.gnu.org/software/gsl/doc/html/#) | 2.7 |The GNU Scientific Library (GSL) is a numerical library for C and C++ programmers.|
| [HDF5](https://portal.hdfgroup.org/display/support/Documentation) | 1.10.1, 1.12.1 | HDF5 is a data model, library, and file format for storing and managing data.|
| [IDL](https://www.l3harrisgeospatial.com/Software-Technology/IDL) | 8.7 |IDL software is a scientific programming language used across disciplines to create visualizations out of complex numerical data.|
| [ImageMagick](https://imagemagick.org/index.php) | 6.9.12 |ImageMagick is a free and open-source software suite for displaying, converting, and editing raster image and vector image files.| 
| [Intel Advisor](https://www.intel.com/content/www/us/en/developer/tools/oneapi/advisor.html#gs.odmdiw) | 2022.0.0 | Intel Advisor is a design and analysis tool for developing performant code. The tool supports C, C++, Fortran, SYCL, OpenMP, OpenCL code, and Python.|  
| Intel cluster tools | 17.3 | Intel cluster tools.| 
| Intel debugger | 17.3, 2021.5.0 |Intel debugging tools.|
| [Intel Inspector](https://www.intel.com/content/www/us/en/developer/tools/oneapi/inspector.html#gs.nwibbc) | 2022.0.0 | Intel Inspector is a memory and thread checking and debugging tool to increase the reliability, security, and accuracy of C/C++ and Fortran applications. |
| [Intel MPI (impi)](https://www.intel.com/content/www/us/en/developer/tools/oneapi/mpi-library.html#gs.nwdbyx) | 2021.4.0, 2021.5.0 |Intel MPI Library is a multifabric message-passing library that implements the open source MPICH specification.| 
| [Intel oneAPI](https://www.intel.com/content/www/us/en/developer/tools/oneapi/overview.html#gs.nwk0f3) | 2022.1.2 | Intel compilers, libraries, and development tools.|
| [Intel VTune](https://www.intel.com/content/www/us/en/developer/tools/oneapi/vtune-profiler.html#gs.nwdnjz) | 2022.0.0 | Intel VTune Profiler optimizes application performance, system performance, and system configuration for HPC, cloud, IoT, media, storage, and more.|
| [JDK (Java Development Kit)](https://www.oracle.com/java/) | 1.7.0, 1.8.0_91, 1.8.0_281, 1.8.0, 18.0.1.1 (D) | JDK is a software development environment used for developing Java applications and applets. |
| [JPEG](https://jpegclub.org/reference/reference-sources/) | 9d, 9e | Open source JPEG Image Library.|
| [Julia](https://julialang.org/) | 0.6.2, 1.6.0, 1.6.6, 1.8.1 (D) | Julia is a high-level, dynamic programming language. Its features are well suited for numerical analysis and computational science. |
| [LAMMPS](https://www.lammps.org/#nogo&gsc.tab=0) | 29Sept21, 29Sept2021_update3 | LAMMPS is a classical molecular dynamics code with a focus on materials modeling. |
| [LFTP](https://lftp.yar.ru) | 4.8.4 | LFTP is a sophisticated file transfer program supporting a number of network protocols (ftp, http, sftp, fish, torrent) |
| [Load Balancer](https://curc.readthedocs.io/en/latest/software/loadbalancer.html?highlight=load%20balancer) | 0.2 |Load Balancer is an effective tool for optimally utilizing multiple processors and nodes on the CURC HPC resources, without the need to learn OpenMP or MPI.| 
| [Mathematica](https://www.wolfram.com/mathematica/) | 9.0, 11.1.0 (D) | A software system with built-in libraries for several areas of technical computing. | 
| [MATLAB](https://www.mathworks.com/products/matlab.html) | R2020b, R2021b (D), R2022b | MATLAB is a proprietary multi-paradigm programming language and numeric computing environment. [CURC Usage Guide](https://curc.readthedocs.io/en/latest/software/matlab.html)| 
| [Maven](https://maven.apache.org/) | 3.8.1 | Apache Maven is a build automation tool used primarily for Java projects. Maven can also be used to build and manage projects written in C#, Ruby, Scala, and other languages. |
| [MKL](https://www.intel.com/content/www/us/en/develop/documentation/get-started-with-mkl-for-dpcpp/top.html) | 2021.4.0, 2022.0.2 |A library of optimized math routines for science, engineering, and financial applications. Core math functions include BLAS, LAPACK, ScaLAPACK, sparse solvers, fast Fourier transforms, and vector math.|
| [NAMD](http://www.ks.uiuc.edu/Research/namd/) | 2.14 | NAMD is a parallel molecular dynamics code for large biomolecular systems.| 
| [NCL](https://www.ncl.ucar.edu/Download/) | 6.3.0, 6.6.2 (D) | NCAR Command Language. An interpreted language designed for scientific data analysis and visualization. |
| [Ncview](http://meteora.ucsd.edu/~pierce/ncview_home_page.html) | 2.1.7 | Ncview is a visual browser for netCDF format files. | 
| [NetCDF](https://www.unidata.ucar.edu/software/netcdf/) | 4.8.1 | NetCDF (Network Common Data Form) is a set of software libraries and machine-independent data formats that support the creation, access, and sharing of array-oriented scientific data.  |
| [NVIDIA HPC SDK](https://developer.nvidia.com/hpc-sdk) (G)| 2022.229, 2023.233|The NVIDIA HPC Software Development Kit (SDK) includes the proven compilers, libraries and software tools essential to maximizing developer productivity and the performance and portability of HPC applications.| 
| [OpenBLAS](https://www.openblas.net/) | 0.3.20 | OpenBLAS is an optimized Basic Linear Algebra Subprograms (BLAS) library based on GotoBLAS 21.13 BSD version. | 
| [OpenJPEG](https://www.openjpeg.org/) | 2.2.0 | OpenJPEG is an open-source JPEG 2000 codec written in C language. | 
| [Open MPI](https://www.open-mpi.org/) | 4.1.1, 4.1.4 | The Open MPI Project is an open source Message Passing Interface implementation that is developed and maintained by a consortium of academic, research, and industry partners. | 
| [ORCA](https://orcaforum.kofo.mpg.de/app.php/portal) | 5.0.3 | ORCA is an ab initio quantum chemistry program package that contains modern electronic structure methods.| 
| [PAPI](https://icl.utk.edu/papi/index.html)| 5.4.3, 5.5.1 (D) | A complete, cross-platform solution to record, convert and stream audio and video. |
| [ParaView](https://www.paraview.org/) | 5.0.1, 5.6.0, 5.9.0, 5.10.0 (D) | ParaView is an open-source multiple-platform application for interactive, scientific visualization. | 
| [PDT (Program Database Toolkit)](https://www.cs.uoregon.edu/research/pdt/home.php) | 3.22, 3.25.1 (D) | PDT is a framework for analyzing source code written in several programming languages and for making rich program knowledge accessible to developers of static and dynamic analysis tools. | 
| [Perl](https://www.perl.org/) | 5.16.3, 5.24.0 (D), 5.28.1, 5.36.0 | Perl is a high-level, interpreted, general-purpose programming language originally developed for text manipulation.| 
| [PETSc](https://petsc.org/) | 3.18.3 (D) | PETSc is a suite of data structures and routines for the scalable (parallel) solution of scientific applications modeled by partial differential equations.| 
| [pigz](https://zlib.net/pigz/) | 2.7 (D) | Pigz is a parallel implementation of gzip.| 
| [Python](https://www.python.org/) | 2.7.18, 3.10.2 (D) |Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.| 
| [PyTorch](https://pytorch.org/) | 1.13.0 (G) |PyTorch is a machine learning framework based on the Torch library, used for applications such as computer vision and natural language processing.| 
| [Q-Chem](https://www.q-chem.com/) | 4010 |Q-Chem is a comprehensive ab initio quantum chemistry software for accurate predictions of molecular structures, reactivities, and vibrational, electronic and NMR spectra.| 
| [Quantum ESPRESSO](https://www.quantum-espresso.org/) | 7.0 |An integrated suite of Open-Source computer codes for electronic-structure calculations and materials modeling at the nanoscale.| 
| [Qt](https://doc.qt.io/) | 4.8.5, 5.6.0, 5.9.1, 5.15 (D) |Qt ("cute") is cross-platform software for creating graphical user interfaces as well as cross-platform applications that run on various software and hardware platforms.| 
| [R](https://www.r-project.org/) | 3.6.3,4.2.2 (D)|R is a programming language for statistical computing and graphics.| 
| [rclone](https://rclone.org/) | 1.58.0 |Rclone is a command-line program to manage files on cloud storage.| 
| [RELION](https://relion.readthedocs.io/en/release-4.0/index.html) | 3.1.3_cpu, 4.0-beta-cu11.2 (G) |Relion (for **RE**gularised **LI**kelihood **O**ptimisatio**N**, pronounce rely-on) is a software package that employs an empirical Bayesian approach for electron cryo-microscopy (cryo-EM) structure determination.| 
| [ROCm](https://www.amd.com/en/graphics/servers-solutions-rocm) (G)  | 5.2.3 |ROCm is an AMD software stack for GPU programming.| 
| [Ruby](https://www.ruby-lang.org/en/) | 2.3.1, 3.0.0 (D) |Ruby is an interpreted, high-level, general-purpose programming language which supports multiple programming paradigms.| 
| [ScaLAPACK](https://netlib.org/scalapack/) | 2.2.0 |ScaLAPACK is a library of high-performance linear algebra routines for parallel distributed memory machines.| 
| [Singularity/Apptainer](https://apptainer.org/) | 3.6.4 (D), 3.7.4 |Singularity/Apptainer is a computer program that performs operating-system-level virtualization also known as containerization. [CURC Usage Guide](https://curc.readthedocs.io/en/latest/software/Containerizationon.html#singularity)|
| [Slurmtools](https://curc.readthedocs.io/en/latest/compute/monitoring-resources.html#slurmtools) | 0.0.0 |A collection of helper scripts for everyday use of the Slurm job scheduler.|
| [SQLite](https://sqlite.org/index.html) | 3.36.0, 3.38.01 |SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.| 
| [Subversion](https://subversion.apache.org/) | 1.8.16, 1.10.2, 1.14.1 (D) |Apache Subversion is a software versioning and revision control system.| 
| [Tcl/Tk](https://www.tcl.tk/about/) | 8.6.5, 8.6.11 (D) |Tcl is a high-level, general-purpose, interpreted, dynamic programming language.| 
| [tDOM](http://tdom.org/index.html/dir?ci=release) | 0.8.3, 0.9.2 |tDOM is a Tcl extension for parsing XML.| 
| [TeX Live](https://www.tug.org/texlive/) | 2021 |TeX Live is a cross-platform, free software distribution for the TeX typesetting system that includes major TeX-related programs, macro packages, and fonts.| 
| [TIFF](http://www.simplesystems.org/libtiff/) | 4.3.0 |The LibTIFF software provides support for the Tag Image File Format (TIFF), a widely used format for storing image data.| 
| [TotalView](https://totalview.io/) | 2016.06.21 |TotalView debugging software provides tools you need to debug, analyze, and scale high-performance computing (HPC) applications.| 
| [Trelis](https://coreform.com/company/news/2020/rebrand/) (L) | 16.3.6 | Software that includes everything needed for streamlined progress from CAD to analysis, with full-featured capabilities for geometry preparation and mesh generation, analysis, and fine-tuning. | 
| [UCX](https://openucx.org/) | 1.10.1, 1.12.1 (D) | A communication framework for data-centric and high-performance applications.| 
| [UDUNITS](https://www.unidata.ucar.edu/software/udunits/) | 2.2.20, 2.2.24, 2.2.25, 2.2.28 (D) |The UDUNITS package supports units of physical quantities. Its C library provides for arithmetic manipulation of units and for conversion of numeric values between compatible units.|
| [Valgrind](https://valgrind.org/) | 3.11.0, 3.17.0 (D) |Valgrind is an instrumentation framework containing tools that can automatically detect many memory management and threading bugs, and profile your programs in detail.| 
| [VAPOR](https://github.com/NCAR/VAPOR) | 3.3.0, 3.4.0 (D) |VAPOR is the Visualization and Analysis Platform for Ocean, Atmosphere, and Solar Researchers.|
| [vtf3](https://www.paratools.com/otf/) | 1.43 |VTF3 trace generation package.|  
| [zip](https://infozip.sourceforge.net/) | rhel7|A compressor/archiver for creating and modifying zipfiles.|
| [zlib](https://www.zlib.net/) | 1.2.11 | Lossless data-compression library.|

**(D)** Default module version **(G)** GPU-accelerated **(L)** License-restricted

## Alpine Software Policy 

Historically, software installations have been a sticking point for many users or CURC resources. Though we still encourage users to 
install and manage their own packages locally, CURC has decided to move forward with the following software policy:

CURC will perform software installations for users of CURC resources in a globally accessible module stack provided:

- A user requires a specified software that is unavailable on the current stack.
- A user requires a different version of a currently existing software which provides additional functionality required for the user’s work.
- The user provides all of the relevant information including release, version, etc. 
- The installation will not violate the software’s User Agreement policy.
- The installation is not better suited for a local install (I.E. Anaconda Environments, Singularity Containers).

Furthermore, licensed/proprietary software are subject the following requirements:

- The user has access to an appropriate license for cluster usage.
- The license can be installed or accessed on the cluster. 

Software accepted for installation will be given an estimated installation time based on capacity of the team and urgency of the request. Note that this time is an estimation and not a strict deadline. Installed software will be available to load with a module in the ‘User Software’ category in the software stack. Unused modules will be pruned after 12 months without usage. Any pruned module may be restored by user request.

Core software such as compilers, MPIs, and relevant libraries will be updated at a semesterly interval. A different version of these core softwares can be requested at any point, but installation may be performed in accordance to that timeline.

All software installations are “Best Effort” and are not guaranteed. RC reserves the right to deny any software installation that is requested on CURC resources.

To request a software installation please fill out the [Software Request Form](https://www.colorado.edu/rc/userservices/software-request)

_Please note that this software policy is subject to change. Please review the software policy before submitting a request._


Alpine is jointly funded by the University of Colorado Boulder, the University of Colorado Anschutz, Colorado State University, and the National Science Foundation (award 2201538).

Couldn't find what you need? [Provide feedback on these docs!](https://forms.gle/bSQEeFrdvyeQWPtW9)
