- [Overview](#overview)
- [How to Submit a Job](#how-to-submit-a-job)
- [Specifying a Partition](#partitions)
- [Specifying Quality-of-Service](#quality-of-service-qos)

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

Watch this [video](https://youtu.be/sStJQKTa9zY) or read the information below.

[![Logging-in-video](https://raw.githubusercontent.com/ResearchComputing/Research-Computing-User-Tutorials/master/Job-Submissions/job-submissions-vid.jpg)](https://youtu.be/sStJQKTa9zY)

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
    - Update your template with any job specifications, including [QOS or Partitions](https://github.com/ResearchComputing/Research-Computing-User-Tutorials/wiki/qos-and-partitions) 
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


## Partitions

On Summit, nodes with the same hardware configuration are grouped into partitions. You will need to specify a partition using  --partition in sbatch in order for your job to run on the appropriate type of node.

These are the partitions available on Research Computing resources.

|Partition name|    Description        |# of nodes|cores/nodes|RAM/core (GB)|Max Walltime|Billing weight|
|--------------|-----------------------|----------|-----------|-------------|------------|--------------|
|     shas     | Haswell CPUs (default)|   380    |    24     |    5.25     |    24H     |       1      |
|     sgpu     |      GPU-enabled      |    10    |    24     |    5.25     |    24H     |      2.5     |
|     smem     |      High-memory      |     5    |    48     |     42      |     7D     |       6      |
|     sknl     | Phi (Knights Landing) |    20    |    64     |    TBD      |    24H     |      0.1     |

More details about each type of node can be found [here](https://www.colorado.edu/rc/resources/summit/specifications).

## Quality of Service (QoS)

On Summit, QoS's are used to constrain or modify the characteristics that a job can have. For example, by selecting the "debug" QoS, a user can obtain higher queue priority for a job with the trade-off that the maximum allowed wall time is reduced from what would otherwise be allowed on that partition. We recommend specifying a QoS (using the  --qos  flag or directive in Slurm) as well as a partition for every job.

The available Summit QoS's are:

|QOS name|       Description          |     Max walltime     |Max jobs/user|   Node limits   |Priority boost|
|--------|----------------------------|----------------------|-------------|-----------------|--------------|
| normal |         default            |Derived from partition|     n/a     |  256/user       |       0      |
| debug  |     For quick testing      |          1H          |      1      |   32/job        |Equiv. of 3-day queue wait time|
|  long  |     Longer wall times      |          7D          |     n/a     |22/user;40 total |0       |
|  condo | Condo purchased nodes only |          7D          |     n/a     |n/a              |Equiv. of 1 day queue wait time|
