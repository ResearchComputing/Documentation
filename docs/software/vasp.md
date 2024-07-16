# VASP

The Vienna Ab initio Simulation Package ([VASP](https://www.vasp.at)) is a computer program for atomic scale materials modelling, e.g. electronic structure calculations and quantum-mechanical molecular dynamics

VASP requires a license. Individual students or entire departments/faculties are not eligible, and therefore CU Research Computing does not have a VASP module for community use. Licenses are issued to well-defined research groups under the direction of a single chair, professor, or group leader at one single physical location.  Group leaders may [apply for a VASP license](https://www.vasp.at/sign_in/registration_form/), after which they will be given access to the source code. 

The documentation below demonstrates how to install and use VASP in one's `/projects/$USER` directory.  A typical case would be to install the software in the `/projects/$USER` directory of the group leader, and then make it available to group members by emailing rc-help@colorado.edu to request that they be added to the Linux user group of the group leader. 

## Prerequisites
* you have a copy of the source code
* you are in a group that has a vasp license
* you only use VASP for research purposes

## Assumptions
* the example below is for version 5.4.4; adjust version to match yours
* the example below assumes the source code is in a tar.gz file; if the source code is in a directory, you can skip the "tar -xf" step
* the example below assumes you will install the software in /projects/$USER/software; adjust as needed.
* you have started an interactive job on alpine ("module load slurm/alpine; acompile")

## To compile vasp
```bash
module purge
module load intel/2022.1.2
module load impi/2021.5.0
module load mkl/2022.0.2
cd /projects/$USER/software
tar -xf vasp.5.4.4.tar.gz
cd vasp.5.4.4
cp arch/makefile.include.linux_intel ./makefile.include
make
```

## To use vasp (example job script)

```bash
#!/bin/bash

#SBATCH --partition=amilan
#SBATCH --qos=normal
#SBATCH --nodes=1
#SBATCH --ntasks=2
#SBATCH --time=1:00:00
#SBATCH --output=vasp.%j.out
#SBATCH --job-name=vasp
#SBATCH --constraint=ib

# this example draws on a the vasp tutorial at:
#    https://www.vasp.at/tutorials/latest/bulk/part1/

#download and unzip the tutorial files
#and set up the POSCAR file (change "a" to "3.9")
wget https://www.vasp.at/tutorials/latest/bulk-part1.zip
tar -xf bulk-part1.zip
unzip bulk-part1.zip
cd bulk-part1/e01_fcc-Si/
sed -i 's/a/3.9/g' ./POSCAR

#load the required modules
module purge
module load intel/2022.1.2
module load impi/2021.5.0
module load mkl/2022.0.2

# add the vasp bin directory to your path
export PATH=$PATH:/projects/$USER/software/vasp.5.4.4/bin

# run vasp
mpirun -n ${SLURM_NTASKS} vasp_std
```
