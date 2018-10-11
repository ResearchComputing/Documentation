#!/bin/bash
#SBATCH --nodes=1                               # Number of requested nodes
#SBATCH --time=0:05:00                          # Max wall time
#SBATCH --qos=testing                           # Specify testing QOS
#SBATCH --partition=shas-testing                # Specify Summit haswell nodes
#SBATCH --ntasks=1                              # Number of tasks per job
#SBATCH --job-name=General-Job-Submission       # Job submission name
#SBATCH --output=GENERAL-JOB-SUBMISSION.%j.out  # Output file name with Job ID


# Written by:	 Shelley Knuth
# Modified by: Daniel Trahan
# Date:		     24 February 2014
# Updated:	   25 July 2018
# Purpose: 	   This script submits a general job to the Slurm job scheduler

# purge all existing modules
module purge

# load any modules needed to run your program  
module load required_module1
module load required_module2
module load required_module3

# The directory where you want the job to run
cd /projects/$USER/your_project

# Run your program
./your_program.exe
