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

## How to Submit a Job

Watch this [video](https://youtu.be/sStJQKTa9zY) or read the information below.

[![Logging-in-video](https://raw.githubusercontent.com/ResearchComputing/Research-Computing-User-Tutorials/master/Job-Submissions/job-submissions-vid.jpg)](https://youtu.be/sStJQKTa9zY)

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

## Job Scripts
Though Research Computing provides a variety of template samples for users to utilize, but knowing each part of a Job Submission script can be useful to know when writing your own job scripts. A job submission script is composed of 5 parts:

```bash
# === 1. Shebang: Tells bash to run the following script as a Shell command ===
#!/bin/bash 

# === 2. List of SBATCH arguements ===
#SBATCH --nodes=1
#SBATCH --time=00:05:00
#SBATCH --qos=debug
#SBATCH --partition=shas
#SBATCH --ntasks=1
#SBATCH --job-name=test-job
#SBATCH --output=test-job.%j.out

# === 3. Purge and load needed modules ===
module purge

module load python

# === 4. Additional commands needed to run a program ===
echo "Set environment variables or create directories here!"

# === 5. Running the program ===
python example_Program.py
```

1. Shebang -- This section of the script tells the terminal to run the file as a bash script. This line should not be modified in anyway.

2. SBATCH arguments -- This section of tells sbatch what arguments to pass into the command when the script is run. A variety of these commands can be found at the bottom of this document [here]() and on [the Slurm page for sbatch](). Adjust and modify these lines to fit the needs of your program.

3. Modules -- This section of code is meant to hold commands that will clean up and add any modules needed to our program. In this example we purge all existing modules from the environment and adds the python module afterwards. It is best practice to first purge all modules needed and add any modules you need after. 

4. Additional Commands -- This section of code allows a user to run any additional commands that may be needed to run your program. This can include the creation of directories, changing directories, the setting of environment variables and a whole variety of other commands. 

5. Running the Program -- This line of code actually runs your code. Adjust the command to execute your program.

Using this information we can construct efficient and organized job submissions that can be recycled or reused. 

### Examples

Job script to run a 5 minute long, 1 node, 1 core C++ Job:

```bash
#!/bin/bash 

#SBATCH --nodes=1
#SBATCH --time=00:05:00
#SBATCH --qos=debug
#SBATCH --partition=shas
#SBATCH --ntasks=1
#SBATCH --job-name=cpp-job
#SBATCH --output=cpp-job.%j.out

module purge

./example_cpp.exe
```

Job script to run a 7 minute long, 1 node, 4 core C++ OpenMP Job:

```bash
#!/bin/bash 

#SBATCH --nodes=1
#SBATCH --time=00:07:00
#SBATCH --qos=debug
#SBATCH --partition=shas
#SBATCH --ntasks=4
#SBATCH --job-name=omp-cpp-job
#SBATCH --output=omp-cpp-job.%j.out

module purge

export OMP_NUM_THREADS=4

./example_omp.exe
```

Job script to run a 10 minute long, 2 node, 48 core C++ MPI Job: 

```bash
#!/bin/bash 

#SBATCH --nodes=2
#SBATCH --time=00:07:00
#SBATCH --qos=debug
#SBATCH --partition=shas
#SBATCH --ntasks=24
#SBATCH --job-name=mpi-cpp-job
#SBATCH --output=mpi-cpp-job.%j.out

module purge
module load intel
module load impi

mpirun -np 48 ./example_mpi.exe
```

## Partitions

On Summit, nodes with the same hardware configuration are grouped into partitions. You will need to specify a partition using  --partition in sbatch in order for your job to run on the appropriate type of node.

These are the partitions available on Research Computing resources.

|Partition|    Description   |# of nodes|cores/node|RAM/core (GB)|Billing weight|Default and Max Walltime|
|---------|------------------|----------|----------|-------------|--------------|------------------------|
|   shas  | Haswell (default)|   380    |    24    |    5.25     |       1      |       4H, 24H*         |
|   sgpu  |     GPU-enabled  |    10    |    24    |    5.25     |      2.5     |       4H, 24H*         |
|   smem  |     High-memory  |     5    |    48    |     42      |       6      |       4H, 7D           |
|   sknl  |    Phi (KNL)     |    20    |    68    |    TBD      |      0.1     |       4H, 24H*         |

* The _normal_ QOS is the default QOS if no other is specified.

To run a job longer than 24 hours on the _shas_, _sgpu_, or _sknl_ partitions, use the _long_ QOS.

More details about each type of node can be found [here](https://www.colorado.edu/rc/resources/summit/specifications).

## Quality of Service (QoS)

On Summit, QoS's are used to constrain or modify the characteristics that a job can have. For example, by selecting the "debug" QoS, a user can obtain higher queue priority for a job with the trade-off that the maximum allowed wall time is reduced from what would otherwise be allowed on that partition. We recommend specifying a QoS (using the  --qos  flag or directive in Slurm) as well as a partition for every job.

The available Summit QoS's are:

|QOS name|       Description          |     Max walltime     |Max jobs/user|   Node limits   |Priority boost|
|--------|----------------------------|----------------------|-------------|-----------------|--------------|
| normal |         default            |    see table above   |     n/a     |  256/user       |       0      |
| testing  |     For quick turnaround when testing      |          30M          |      1      |   2/user (max 12 cores/node)        |0|
| interactive  |     For interactive jobs (command or GUI)      |          4H          |      1      |   1 core    |0|
|  long  |     Longer wall times      |          7D          |     n/a     |22/user;40 total |0       |
|  condo | Condo purchased nodes only |          7D          |     n/a     |n/a              |Equiv. of 1 day queue wait time|
