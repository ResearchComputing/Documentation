#!/bin/bash
#SBATCH --nodes=1                    		        # Number of requested nodes
#SBATCH --time=0:05:00               		        # Max wall time
#SBATCH --qos=testing                           # Specify testing QOS
#SBATCH --partition=shas-testing             		# Specify Summit haswell nodes
#SBATCH --ntasks=12          	 	                # Number of tasks per job
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

# Traverse to the directory that contains any matlab scripts you would like to run
cd /projects/$USER/target_Directory

# Run matlab without a GUI and ask for all available workers
# In this example we will run the matlab script "parallel_std.m"
matlab -nosplash -nodesktop -r "clear; num_workers=$SLURM_NTASKS; parallel_std;"
