# CURC-Provided Software

The following page provides a list of all software that is included in CURC's software stack. This list includes the software applications, compilers, libaries, and software development kits (SDKs) installed as modules on CURC. These modules are accessible on both Alpine and Blanca. For more information on viewing and using modules, please refer to our [Modules System](../compute/modules.md) page. 

```{important}
Before requesting a software installation, please review our [Software installations](../additional-resources/policies.md#software-installations) policy. This should be done before each request, as the policy is subject to change. If you have any questions about this policy, please feel free to reach out to us by submitting a [support request form](https://colorado.service-now.com/req_portal?id=ucb_sc_rc_form). 
```

:::{admonition} Legend for software table
:class: tip

**(D)** Default module version **(G)** GPU-accelerated **(L)** License-restricted
:::

| Application           | Version(s)          | Description      |
| --------------------- | ------------------- | ---------------- |
| [Abaqus](https://www.3ds.com/products-services/simulia/products/abaqus/) (L) | V6R2019x | Abaqus FEA is a software suite for finite element analysis and computer-aided engineering.|  
| [AlphaFold](https://www.deepmind.com/research/highlighted-research/alphafold) (G) | 2.2.0, 2.3.1, 3.0.0, 3.0.1 (D) | AlphaFold is an artificial intelligence program developed by DeepMind, a subsidiary of Alphabet, which performs predictions of protein structures.| 
| [AltairFEKO](https://altair.com/feko) (L) | 2019.2, 2023.1 (D) | FEKO is an electromagnetics software developed by Altair Engineering for use in field calculations for bodies of arbitrary shapes. | 
| [Anaconda](https://www.anaconda.com/products/distribution) | 2020.11, 2022.10, 2023.09 (D) | Anaconda is a distribution of the Python and R programming languages for scientific computing, that aims to simplify package management and deployment. [CURC Usage Guide](./python.md)| 
| [Ansys](https://www.ansys.com/) (L,G) | EM21.2, EM22.2 (D), EM23.1 | CAE/multiphysics engineering simulation software for product design, testing and operation.|
| [ANTLR](https://www.antlr.org/) | 4.13.1 | A parser generator for reading, processing, executing, or translating structured text or binary files. |
| [AOCC](https://www.amd.com/en/developer/aocc.html) | 3.1.0 (D), 3.2.0 |The AMD Optimizing C/C++ and Fortran Compilers (“AOCC”) are a set of production compilers optimized for software performance when running on AMD host processors using the AMD “Zen” core architecture.| 
| [AOCL](https://www.amd.com/en/developer/aocl.html) | 3.2.0 |AOCL is a set of numerical libraries optimized for AMD processors based on the AMD “Zen” core architecture and generations.| 
| [Autotools](https://www.gnu.org/software/automake/faq/autotools-faq.html) | 2.6.9, 2.7.1 (D)| The GNU Autotools, also known as the GNU Build System, is a suite of programming tools designed to assist in making source code packages portable to many Unix like systems.|
| [BamTools](https://github.com/pezmaster31/bamtools) | 2.5.2| BamTools provides both a programmer's API and an end-user's toolkit for handling BAM files.|
| [BBTools](https://archive.jgi.doe.gov/data-and-tools/software-tools/bbtools/) | 39.01 | BBTools is a suite of fast, multithreaded bioinformatics tools designed for analysis of DNA and RNA sequence data.|
| [BCFtools](https://samtools.github.io/bcftools/) | 1.16 | BCFtools is a set of utilities that manipulate variant calls in the Variant Call Format (VCF) and its binary counterpart BCF. All commands work transparently with both VCFs and BCFs, both uncompressed and BGZF-compressed.|
| [bedtools](https://bedtools.readthedocs.io/en/latest/) | 2.29.1 | Collectively, the bedtools utilities are a Swiss Army knife of tools for a wide-range of genomics analysis tasks.|
| [boost](https://www.boost.org/) | 1.78.0, 1.86.0 | Boost provides free peer-reviewed portable C++ source libraries.| 
| [Bowtie2](https://bowtie-bio.sourceforge.net/bowtie2/index.shtml) | 2.5.0 | Bowtie2 is an ultrafast and memory-efficient tool for aligning sequencing reads to long reference sequences.| 
| [BWA](https://bio-bwa.sourceforge.net/) | 0.7.17 | BWA is a software package for mapping low-divergent sequences against a large reference genome, such as the human genome.| 
| [CDO](https://code.mpimet.mpg.de/projects/cdo/) | 2.1.1, 2.4.4 | CDO is a collection of command line operators to manipulate and analyze climate and NWP model data.|
| [Cellranger](https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/latest/what-is-cell-ranger) | 7.1.0 | Cellranger is a set of analysis pipelines that process Chromium single cell data to align reads, generate feature-barcode matrices, perform clustering and other secondary analysis, and more.|
| [ChimeraX](https://www.cgl.ucsf.edu/chimerax/) | 1.2.5 | A next-generation molecular visualization program. | 
| [CMake](https://cmake.org/) | 3.5.2, 3.9.2, 3.14.1, 3.20.2, 3.25.0, 3.27.7, 3.31.0, 4.2.3 (D) | CMake is an open-source, cross-platform family of tools designed to build, test and package software.| 
| [Coreform Cubit](https://coreform.com/products/coreform-cubit/) (L)| Coreform-Cubit-2021.5 | Coreform Cubit is a comprehensive toolset for high-quality FEA and CFD mesh generation that provides a similar user experience as GAMBIT.| 
| [CP2K](https://www.cp2k.org/) | 2023.1 | CP2K is a quantum chemistry and solid state physics software package that can perform atomistic simulations of solid state, liquid, molecular, periodic, material, crystal, and biological systems.|
| [CST Studio Suite](https://www.3ds.com/products-services/simulia/products/cst-studio-suite/) (L) | 2021, 2024 (D) | CST Studio Suite is a high-performance 3D EM analysis software package for designing, analyzing and optimizing electromagnetic (EM) components and systems. | 
| [Cube](https://www.scalasca.org/scalasca/software/cube-4.x/download.html) | 3.4.3, 4.3.4 (D) | Cube, which is used as performance report explorer for Scalasca and Score-P, is a generic tool for displaying a multi-dimensional performance space. | 
| [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit) (G) | 11.2, 11.3, 11.4, 11.7, 11.8, 12.1.1 (D), 12.9* | The NVIDIA CUDA Toolkit includes GPU-accelerated libraries, debugging and optimization tools, a C/C++ compiler, and a runtime library to deploy your application. *Included in the `nvhpc_sdk/2025.255` module. Future CUDA versions will only be available through the NVIDIA HPC SDK module. | 
| [cuDNN](https://developer.nvidia.com/cudnn) (G)| 8.1, 8.2, 8.6 (D), 9.10.2 | The NVIDIA CUDA Deep Neural Network library (cuDNN) is a GPU-accelerated library of primitives for deep neural networks. | 
| [curc-quota](../compute/filesystems.md#monitoring-disk-usage) | 5.0 | CU Boulder script that provides information the user's home, projects, scratch, and PetaLibrary space.| 
| [Cutadapt](https://cutadapt.readthedocs.io/en/stable/) | 4.2 | Cutadapt finds and removes adapter sequences, primers, poly-A tails and other types of unwanted sequences from your high-throughput sequencing reads.| 
| [DMTCP](https://dmtcp.sourceforge.io/) | 2.6.0 | DMTCP (Distributed MultiThreaded Checkpointing) transparently checkpoints a single-host or distributed computation in user-space without modifications to user code or to the OS.|
| [Eigen](https://eigen.tuxfamily.org/index.php?title=Main_Page) | 3.4.0 | Eigen is a C++ template library for linear algebra: matrices, vectors, numerical solvers, and related algorithms.|
| [Emacs](https://www.gnu.org/software/emacs/) | 25.3, 27.2, 30.1 (D) | An extensible, customizable, text editor.|
| [EPW](https://docs.epw-code.org) | 6.0alpha | EPW is part of the Quantum ESPRESSO suite & calculates properties related to the electron-phonon interaction|
| [Expat](https://libexpat.github.io/) | 2.1.1, 2.3.0 (D) | Stream-oriented XML parser library written in C.| 
| [FastQC](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/) | 0.11.9 | A quality control tool for high throughput sequence data.|
| [FFmpeg](https://ffmpeg.org/) | 4.4 | A complete, cross-platform solution to record, convert and stream audio and video.| 
| [FFTW](https://www.fftw.org/) | 3.3.8, 3.3.9, 3.3.10 | FFTW is a C subroutine library for computing the discrete Fourier transform (DFT) in one or more dimensions, of arbitrary input size, and of both real and complex data.|
| [GATK](https://gatk.broadinstitute.org/hc/en-us) | 4.3.0.0 | GATK4 aims to bring together well-established tools from the GATK and Picard codebases under a streamlined framework.|
| [Gaussian 16](https://gaussian.com/gaussian16/) (L,G) | g16_c.02 | Guassian 16 provides state-of-the-art capabilities for electronic structure modeling. [CURC Usage Guide](./gaussian.md)|
| [gcc](https://gcc.gnu.org/) |  10.3.0, 11.2.0, 13.2.0, 14.2.0 (D) |The GNU Compiler Collection includes front ends for C, C++, Objective-C, Fortran, Ada, Go, and D, as well as libraries for these languages (libstdc++,...).| 
| [GDAL](https://gdal.org/) | 3.4.2, 3.5.0, 3.10.0 | GDAL is a translator library for raster and vector geospatial data formats.| 
| [GDB](https://www.sourceware.org/gdb/) | 8.1, 10.1 (D) | GDB, the GNU Project debugger, allows you to see what is going on 'inside' another program while it executes -- or what another program was doing at the moment it crashed.|
| [GEOS](https://libgeos.org/) | 3.9.1, 3.10.2, 3.13.0 | GEOS is a C/C++ library for computational geometry with a focus on algorithms used in geographic information systems (GIS) software.|
| [Ghostscript](https://ghostscript.com/index.html) | 9.56.0 |Ghostscript is an interpreter for the PostScript language and PDF files.| 
| [Git](https://git-scm.com/downloads) | 2.31.0 | Git is a distributed version control system that tracks changes in any set of computer files.| 
| [Git-LFS](https://git-lfs.com) | 3.1.2 | Git-LFS is a Git exention for versioning large files.| 
| [Gmsh](https://gmsh.info/) | 2.16.0, 4.11.1 (D) | Gmsh is an open source 3D finite element mesh generator with a built-in CAD engine and post-processor.|
| [GNU Parallel](https://www.gnu.org/software/parallel/) | 20160622, 20210322 (D) | GNU parallel is a shell tool for executing jobs in parallel using one or more computers. [CURC Usage Guide](./GNUParallel.md)| 
| [gnuplot](http://www.gnuplot.info/) | 5.4.3 | gnuplot is a command-line and GUI program that can generate two- and three-dimensional plots of functions, data, and data fits.| 
| [GROMACS](https://www.gromacs.org/) (G) | 2022.4, 2024.2 | GROMACS is a molecular dynamics package mainly designed for simulations of proteins, lipids, and nucleic acids.| 
| [GSL](https://www.gnu.org/software/gsl/doc/html/#) | 2.7, 2.8 |The GNU Scientific Library (GSL) is a numerical library for C and C++ programmers.|
| [HDF5](https://www.hdfgroup.org/solutions/hdf5/) | 1.10.1, 1.12.1, 1.14.5 | HDF5 is a data model, library, and file format for storing and managing data.|
| [HOMER](http://homer.ucsd.edu/homer/) | 4.11 | Software for motif discovery and next-gen sequencing analysis.|
| [IDL](https://www.nv5geospatialsoftware.com/Products/IDL) | 8.7 |IDL software is a scientific programming language used across disciplines to create visualizations out of complex numerical data.|
| [ImageMagick](https://imagemagick.org/index.php) | 6.9.12 |ImageMagick is a free and open-source software suite for displaying, converting, and editing raster image and vector image files.| 
| [Intel Advisor](https://www.intel.com/content/www/us/en/developer/tools/oneapi/advisor.html#gs.odmdiw) | 2022.0.0, 2024.2 | Intel Advisor is a design and analysis tool for developing performant code. The tool supports C, C++, Fortran, SYCL, OpenMP, OpenCL code, and Python.|  
| Intel cluster tools | 17.3 | Intel cluster tools.| 
| Intel debugger | 17.3, 2021.5.0, 2024.2.1 |Intel debugging tools.|
| [Intel Inspector](https://www.intel.com/content/www/us/en/developer/tools/oneapi/inspector.html#gs.nwibbc) | 2022.0.0 | Intel Inspector is a memory and thread checking and debugging tool to increase the reliability, security, and accuracy of C/C++ and Fortran applications. |
| [Intel MPI (impi)](https://www.intel.com/content/www/us/en/developer/tools/oneapi/mpi-library.html#gs.nwdbyx) | 2021.4.0, 2021.5.0, 2021.13 | The Intel MPI Library is a multifabric message-passing library that implements the open source MPICH specification.| 
| [Intel oneAPI](https://www.intel.com/content/www/us/en/developer/tools/oneapi/overview.html#gs.nwk0f3) | 2022.1.2, 2024.2.1 (D) | Intel compilers, libraries, and development tools.|
| [Intel VTune](https://www.intel.com/content/www/us/en/developer/tools/oneapi/vtune-profiler.html#gs.nwdnjz) | 2022.0.0, 2024.2 | Intel VTune Profiler optimizes application performance, system performance, and system configuration for HPC, cloud, IoT, media, storage, and more.|
| [Jasper](https://jasper-software.github.io/jasper/) | 4.0.0, 4.2.4 | JasPer is a software toolkit for the handling of image data. |
| [JDK (Java Development Kit)](https://www.oracle.com/java/) | 1.7.0, 1.8.0_91, 1.8.0_281, 1.8.0, 18.0.1.1 (D) | JDK is a software development environment used for developing Java applications and applets. |
| [JPEG](https://jpegclub.org/reference/reference-sources/) | 9d, 9e, 9f | Open source JPEG image library.|
| [Julia](https://julialang.org/) | 0.6.2, 1.6.0, 1.6.6, 1.8.1, 1.9.4, 1.10.0, 1.10.2, 1.11.6 (D) | Julia is a high-level, dynamic programming language. Its features are well suited for numerical analysis and computational science. |
| [LAMMPS](https://www.lammps.org/#nogo&gsc.tab=0) | 22July25, 2Aug23, 29Sept21, 29Sept2021_update3, 29Sept21, 29Sept2021_update3.1.1 | LAMMPS is a classical molecular dynamics code with a focus on materials modeling. |
| [LFTP](https://lftp.yar.ru) | 4.8.4, 4.9.2 (D) | LFTP is a sophisticated file transfer program supporting a number of network protocols (ftp, http, sftp, fish, torrent) |
| [Libxc](https://gitlab.com/libxc/libxc) | 5.2.2, 7.0.0 | Libxc is a library of exchange-correlation functionals for density-functional theory. |
| [Load Balancer](./loadbalancer.md) | 0.2 |Load Balancer is an effective tool for optimally utilizing multiple processors and nodes on the CURC HPC resources, without the need to learn OpenMP or MPI.| 
| [Mamba](https://mamba.readthedocs.io/) | 24.11.3-0 | Mamba is a fast, robust, and cross-platform package manager that aims to be a drop-in replacement for conda. Please see our [Mamba Package Manager](./python.md#mamba-package-manager) section for more details.| 
| [Mathematica](https://www.wolfram.com/mathematica/) | 9.0, 11.1.0 (D) | A software system with built-in libraries for several areas of technical computing. | 
| [MATLAB](https://www.mathworks.com/products/matlab.html) | R2018b, R2019b, R2020b, R2021b, R2022b, R2023b, R2024b, R2025b (D) | MATLAB is a proprietary multi-paradigm programming language and numeric computing environment. [CURC Usage Guide](./matlab.md)| 
| [Maven](https://maven.apache.org/) | 3.8.1 | Apache Maven is a build automation tool used primarily for Java projects. Maven can also be used to build and manage projects written in C#, Ruby, Scala, and other languages. |
| [MKL](https://www.intel.com/content/www/us/en/developer/tools/oneapi/onemkl.html#gs.ecsytg) | 2021.4.0, 2022.0.2, 2024.2 |A library of optimized math routines for science, engineering, and financial applications. Core math functions include BLAS, LAPACK, ScaLAPACK, sparse solvers, fast Fourier transforms, and vector math.|
| [MultiQC](https://multiqc.info/) | 1.14 | MultiQC is a reporting tool that parses results and statistics from bioinformatics tool outputs, such as log files and console outputs.|
| [NAMD](http://www.ks.uiuc.edu/Research/namd/) | 2.14, 3.0.1 | NAMD is a parallel molecular dynamics code for large biomolecular systems.| 
| [NCL](https://www.ncl.ucar.edu/Download/) | 6.3.0 (D) | NCAR Command Language. An interpreted language designed for scientific data analysis and visualization. |
| [NCO](https://nco.sourceforge.net/) | 4.8.1, 5.1.4, 5.2.9 | A toolkit that manipulates and analyzes data stored in netCDF-accessible formats, including DAP, HDF4, HDF5, and, Zarr | 
| [Ncview](https://cirrus.ucsd.edu/ncview/) | 2.1.7 | Ncview is a visual browser for netCDF format files. | 
| [NetCDF](https://www.unidata.ucar.edu/software/netcdf/) | 4.8.1, 4.9.2 | NetCDF (Network Common Data Form) is a set of software libraries and machine-independent data formats that support the creation, access, and sharing of array-oriented scientific data.|
| [Nextflow](https://www.nextflow.io/) | 22.10.6, 23.04, 24.04.4 (D), 25.10.2 | Nextflow enables scalable and reproducible scientific workflows using software containers. It allows the adaptation of pipelines written in the most common scripting languages.|
| [NVIDIA HPC SDK](https://developer.nvidia.com/hpc-sdk) (G)| 2021.213(CUDA 11.2), 2022.229 (CUDA 11.7), 2023.233 (D, CUDA 12.0), 2025.251 (CUDA 12.6), 2025.255 (CUDA 12.9) | The NVIDIA HPC Software Development Kit (SDK) includes the proven compilers, libraries and software tools essential to maximizing developer productivity and the performance and portability of HPC applications. | 
|[Ollama](https://ollama.com/) | Latest version only | Ollama is an open-source, lightweight, and extremely beginner friendly tool that enables users to run LLMs locally and retrieve models that are compatible with the system they are running on. For more information on using Ollama, see [Running Large Language Models](../ai-ml/llms.md#ollama) |
| [OpenBLAS](https://www.openblas.net/) | 0.3.20, 0.3.28 | OpenBLAS is an optimized Basic Linear Algebra Subprograms (BLAS) library based on GotoBLAS 21.13 BSD version. | 
| [OpenJPEG](https://www.openjpeg.org/) | 2.2.0, 2.5.2 | OpenJPEG is an open-source JPEG 2000 codec written in the C language. | 
| [Open MPI](https://www.open-mpi.org/) | 4.1.1, 4.1.4, 5.0.6 | The Open MPI Project is an open source Message Passing Interface implementation that is developed and maintained by a consortium of academic, research, and industry partners. | 
| [OpenSees](https://opensees.berkeley.edu) | 3.4 | OpenSees is a software framework for developing applications to simulate the performance of structural and geotechnical systems subjected to earthquakes. |
| [ORCA](https://www.faccts.de/orca/) | 5.0.3, 5.0.4, 6.1.0 (D) | ORCA is an ab initio quantum chemistry program package that contains modern electronic structure methods. | 
| [PAPI](https://icl.utk.edu/papi/index.html)| 5.4.3, 5.5.1 (D) | The Performance Application Programming Interface (PAPI) offers a universal interface and methodology for gathering performance counter information from diverse hardware and software components. |
| [ParaView](https://www.paraview.org/) | 5.0.1, 5.6.0, 5.8.0, 5.9.0, 5.10.0 (D) | ParaView is an open-source multiple-platform application for interactive, scientific visualization. | 
| [PDT (Program Database Toolkit)](https://www.cs.uoregon.edu/research/pdt/home.php) | 3.22, 3.25.1 (D) | PDT is a framework for analyzing source code written in several programming languages and for making rich program knowledge accessible to developers of static and dynamic analysis tools. | 
| [Perl](https://www.perl.org/) | 5.16.3, 5.24.0 (D), 5.28.1, 5.36.0 | Perl is a high-level, interpreted, general-purpose programming language originally developed for text manipulation.| 
| [PETSc](https://petsc.org/) | 3.18.3, 3.22.1 | PETSc is a suite of data structures and routines for the scalable (parallel) solution of scientific applications modeled by partial differential equations.| 
| [pigz](https://zlib.net/pigz/) | 2.7 (D) | Pigz is a parallel implementation of gzip.| 
| [Picard](https://broadinstitute.github.io/picard/) | 2.27.5 | Picard is a set of command line tools for manipulating high-throughput sequencing (HTS) data and formats such as SAM/BAM/CRAM and VCF.| 
| [PLINK2](https://www.cog-genomics.org/plink/2.0/) | 2.00a2.3 | PLINK 2.0 is a widely used open-source C/C++ toolset for genome-wide association studies (GWAS) and research in population genetics.|
| [PnetCDF](https://parallel-netcdf.github.io) | 1.12.2, 1.13.0 | PnetCDF is a high-performance parallel I/O library for accessing Unidata's NetCDF, files in classic formats, specifically the formats of CDF-1, 2, and 5. |
| [PROJ](https://proj.org/en/stable/) | 6.0.0, 8.1.1, 8.2.1, 9.5.0 | PROJ is a generic coordinate transformation software that transforms geospatial coordinates from one coordinate reference system (CRS) to another. This includes cartographic projections as well as geodetic transformations. |
| [Python](https://www.python.org/) | 2.7.18, 3.10.2 (D) |Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.| 
| [PyTorch](https://pytorch.org/) | 1.13.0 (G) |PyTorch is a machine learning framework based on the Torch library, used for applications such as computer vision and natural language processing.| 
| [QIIME 2](https://qiime2.org/) | 2023.5, Amplicon 2024.2 (D), Amplicon 2024.10, Amplicon 2026.1 | QIIME 2 is a next-generation microbiome bioinformatics platform that is extensible, free, open source, and community developed.|
| [Quantum ESPRESSO](https://www.quantum-espresso.org/) | 7.0, 7.2, 7.4.1 |An integrated suite of Open-Source computer codes for electronic-structure calculations and materials modeling at the nanoscale.| 
| [Qt](https://doc.qt.io/) | 5.6.0, 5.9.1, 5.15 (D) |Qt ("cute") is cross-platform software for creating graphical user interfaces as well as cross-platform applications that run on various software and hardware platforms.| 
| [R](https://www.r-project.org/) | 3.6.3, 4.2.2, 4.4.0 (D)|R is a programming language for statistical computing and graphics.| 
| [rclone](https://rclone.org/) | 1.58.0 |Rclone is a command-line program to manage files on cloud storage.| 
| [RELION](https://relion.readthedocs.io/en/release-4.0/index.html) | 3.1.3_cpu, 4.0-beta-cu11.2 (G), 4.0.1-cu11.8 (G,D) 5.0 (G), 5.0-cu12.1 (G) |Relion (for **RE**gularised **LI**kelihood **O**ptimisatio**N**, pronounce rely-on) is a software package that employs an empirical Bayesian approach for electron cryo-microscopy (cryo-EM) structure determination.| 
| [ROCm](https://www.amd.com/en/products/software/rocm.html) (G)  | 5.2.3, 5.3.0, 5.5.0, 5.6.0, 6.1.0 (D) |ROCm is an AMD software stack for GPU programming.| 
| [Ruby](https://www.ruby-lang.org/en/) | 2.3.1, 3.0.0 (D) |Ruby is an interpreted, high-level, general-purpose programming language which supports multiple programming paradigms.| 
| [SAMtools](http://www.htslib.org/doc/samtools.html) | 1.16.1 | Samtools is a suite of programs for interacting with high-throughput sequencing data.| 
| [ScaLAPACK](https://netlib.org/scalapack/) | 2.2.0 |ScaLAPACK is a library of high-performance linear algebra routines for parallel distributed memory machines.| 
| [Singularity/Apptainer](https://apptainer.org/) | 3.6.4 (D), 3.7.4 |Singularity/Apptainer is a computer program that performs operating-system-level virtualization also known as containerization. [CURC Usage Guide](./containerization.md#apptainer)|
| [SQLite](https://sqlite.org/index.html) | 3.36.0, 3.38.01, 3.46.1 |SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.| 
| [SRA-Toolkit](https://hpc.nih.gov/apps/sratoolkit.html) | 3.0.0 | The SRA Toolkit and SDK from NCBI is a collection of tools and libraries for using data in the INSDC Sequence Read Archives.| 
| [STAR](https://github.com/alexdobin/STAR/tree/master) | 2.7.10b | A tool to align RNA-seq data. The STAR algorithm uses suffix arrays, seed clustering, and stitching.| 
| [Subversion](https://subversion.apache.org/) | 1.8.16, 1.10.2, 1.14.1 (D) |Apache Subversion is a software versioning and revision control system.| 
| [Szip](http://www.compressconsult.com/szip/) | 2.1.1 | Szip is a freeware portable general purpose lossless compression program. |
| [Tcl/Tk](https://www.tcl.tk/about/) | 8.6.5, 8.6.11, 9.0.1 (D) |Tcl is a high-level, general-purpose, interpreted, dynamic programming language.| 
| [tDOM](http://tdom.org/index.html/dir?ci=release) | 0.8.3, 0.9.2 |tDOM is a Tcl extension for parsing XML.| 
| [TeX Live](https://www.tug.org/texlive/) | 2021 |TeX Live is a cross-platform, free software distribution for the TeX typesetting system that includes major TeX-related programs, macro packages, and fonts.| 
| [TIFF](http://www.simplesystems.org/libtiff/) | 4.3.0, 4.7.0 |The LibTIFF software provides support for the Tag Image File Format (TIFF), a widely used format for storing image data.| 
| [TotalView](https://totalview.io/) | 2016.06.21 |TotalView debugging software provides tools you need to debug, analyze, and scale high-performance computing (HPC) applications.| 
| [Transformers](https://huggingface.co/docs/transformers/en/index#transformers) by Hugging Face | Latest version only | Transformers is Hugging Face’s LLM framework. For more information on using Transformers, see [Running Large Language Models](../ai-ml/llms.md#transformers-by-hugging-face) |
| [Trimmomatic](http://www.usadellab.org/cms/?page=trimmomatic) | 0.39 | Trimmomatic performs a variety of useful trimming tasks for Illumina paired-end and single-ended data. |
| [UCX](https://openucx.org/) | 1.10.1, 1.12.1 (D) | A communication framework for data-centric and high-performance applications.| 
| [UDUNITS](https://www.unidata.ucar.edu/software/udunits/) | 2.2.20, 2.2.24, 2.2.25, 2.2.28 (D) |The UDUNITS package supports units of physical quantities. Its C library provides for arithmetic manipulation of units and for conversion of numeric values between compatible units.|
| [uv](https://docs.astral.sh/uv/) | 0.8.15 (D) | uv is a Python package manager designed for fast, reproducible workflows. Built with Rust, uv uses the venv tool to create isolated Python environments, making it easy to manage dependencies and ensure consistency across different projects. For more information on using uv, see [CURC's uv usage guide](./uv.md)| 
| [Valgrind](https://valgrind.org/) | 3.11.0, 3.17.0 (D) |Valgrind is an instrumentation framework containing tools that can automatically detect many memory management and threading bugs, and profile your programs in detail.| 
| [VAPOR](https://github.com/NCAR/VAPOR) | 3.9.1 |VAPOR is the Visualization and Analysis Platform for Ocean, Atmosphere, and Solar Researchers.|
| [vtf3](https://www.paratools.com/otf/) | 1.43 |VTF3 trace generation package.|  
| xlibs | rhel8 (D) |Provides libraries associated with Xlib, an X Window System protocol client library. These libraries are often needed for visualization software and libraries.|  
| [Yambo](https://www.yambo-code.eu/wiki/index.php/Main_Page) | 5.2.2 |An ab initio tool for excited state calculations.|  
| [zip](https://infozip.sourceforge.net/) | rhel7|A compressor/archiver for creating and modifying zip files.|
| [zlib](https://www.zlib.net/) | 1.2.11, 1.3.1 | Lossless data-compression library.|
