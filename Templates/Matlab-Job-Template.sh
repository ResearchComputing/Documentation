#!/bin/bash
#SBATCH --nodes=1                    		        # Number of requested nodes
#SBATCH --time=0:05:00               		        # Max wall time
#SBATCH --qos=tesing                            # Specify testing QOS
#SBATCH --partition=shas-testing             		# Specify Summit haswell nodes
#SBATCH --ntasks=24          	 	                # Number of tasks per job
#SBATCH --job-name=Matlab_Gen_Parallel          # Job submission name
#SBATCH --output=MATLAB_GEN_PARALLEL.%j.out     # Output file name with Job ID


# Written by:	Shelley Knuth
# Date:		24 February 2014
# Updated:	25 July 2017
# Purpose: 	This script calls a Matlab parallel program 

# purge all existing modules
module purge

# load the matlab module
module load matlab

# The directory where you want the job to run
cd /projects/$USER/tutorials/parallelization_workshop/new

# Run matlab without a GUI and ask for all available workers
matlab -nosplash -nodesktop -r "clear; num_workers=$SLURM_NTASKS; parallel_std;"
