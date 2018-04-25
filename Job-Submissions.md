## Table of Contents

- [Overview](#overview)
- [How to Submit a Job](#how-to-submit-a-job)

## Overview

Before submitting a job be sure to obtain:
- A Research Computing account
- Two-factor authentication
- A SSH client application
- An allocation

Login to a Research Computing resource to submit your job.
When you want to run a non-interactive job:
- Submit the job from a login node or compile node
- The job will run in the background when resources are available.

Need more assistance? Watch a tutorial [video](https://youtu.be/sStJQKTa9zY) or read the information below.

<!---
## Video

[![Logging-in-video](https://raw.githubusercontent.com/ResearchComputing/Research-Computing-User-Tutorials/master/Job-Submissions/job-submissions-vid.jpg)](https://youtu.be/sStJQKTa9zY)
--->

## How to Submit a Job

```
#!/bin/bash
#SBATCH --nodes=1
#SBATCH --time=00:05:00
#SBATCH --qos=debug
#SBATCH --partition=shas
#SBATCH --ntasks=1
#SBATCH --job-name=test-job
#SBATCH --output=test-job.%j.out

module purge

echo "hello!"
sleep 30
echo "goodbye!"
```

1. Write your job script in a text editor
    - You will submit the script to Slurm, a batch queuing system that will schedule the job to run non-interactively when resources are available
    - Use this [template](https://raw.githubusercontent.com/ResearchComputing/Research-Computing-User-Tutorials/master/Templates/General-Job-Template.sh) to write your job script in the text editor
    - You can confirm the content of your script with this command: `cat job-name.sh`
    - Replace “job-name” with the name of your job

2. Submit your job
    - Load the Slurm module with the command `module load slurm/summit` if you are submitting from a login node.  When submitting from a compile node this step is not necessary.
    - Submit the script to Slurm with the command `sbatch test-job.sh`
    - When Slurm accepts the job, it responds with a job ID number
         * Reference the ID number to expedite support if you contact rc-help@colorado.edu about your job

3. To check your job status
    - Use the command `squeue -u $USER`
    - This will show
         * Job ID
         * The partition the job is running on
         * Username
         * Status (“R” for “running”, “PD” for “pending”, or “CG” for “closing”)
         * Length of time the job has been running
         * Number of nodes
         * Name of the node on which the job is running

4. To view the job output
     - Use the command `cat job-name.jobid.out`
     - Replace “job-name” with your job name and “jobid” with your job ID number
