# Batch Jobs and Job Scripting

Batch jobs are, by far, the most common type of job on our HPC system. Batch jobs are resource provisions that run applications on compute nodes and do not require supervision or interaction. Batch jobs are commonly used for applications that run for long periods of time or require little to no user input. 

## Job Scripts

Even though it is possible to run jobs completely from the command line, it is often overly tedious and unorganized to do so. Instead, Research Computing recommends constructing a job script for your batch jobs. A **job script** is set of Linux commands paired with a set of resource requirements that can be passed to the Slurm job scheduler. Slurm will then generate a job according to the parameters set in the job script. Any commands that are included with the job script will be run within the job.

<iframe width="560" height="315" src="https://www.youtube.com/embed/sStJQKTa9zY" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>


## Running a Job Script

Running a job script can be done with the `sbatch` command:

```bash
sbatch <your-job-script-name>
```

Because job scripts specify the desired resources for your job, you won't need to specify any resources on the command line. You can, however, overwrite or add any job parameter by providing the specific resource as a flag within `sbatch` command:

```bash
sbatch --partition=amilan <your-job-script>
```

Running this command would force your job to run on the amilan partition *no matter what your job script specified*.

## Making a Job Script

Although Research Computing provides a variety of different sample scripts users can utilize when running their own jobs, knowing how to draft a job script can be quite handy if you need to debug any errors in your jobs or you need to make substantial changes to a script.

A job script looks something like this:

```bash
#!/bin/bash

#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=00:10:00
#SBATCH --partition=atesting
#SBATCH --output=sample-%j.out

module purge

module load intel
module load mkl

echo "== This is the scripting step! =="
sleep 30
./executable.exe
echo "== End of Job =="
```

Normally job scripts are divided into 3 primary parts: directives, loading software, and user scripting. Directives give the terminal and the Slurm daemon instructions on setting up the job. Loading software involves cleaning out the environment and loading specific pieces of software you need for your job. User scripting is simply the commands you wish to be executed in your job.  

### 1. Directives

A directive is a comment that is included at the top of a job script that tells the shell information about the script. 

The first directive, the shebang directive, is always on the first line of any script. The directive indicates which shell you want running commands in your job. Most users employ bash as their shell, so we will specify bash by typing:

```bash
#!/bin/bash
```

The next directives that must be included with your job script are *sbatch* directives. These directives specify resource requirements to Slurm for a batch job.  These directives must come after the shebang directive and before any commands are issued in the job script. Each directive contains a flag that requests a resource the job would need to complete execution. An sbatch directive is written as such:

```bash
#SBATCH --<resource>=<amount>
```

For example if you wanted to request 2 nodes with an sbatch directive, you would write:

```bash
#SBATCH --nodes=2
```

A list of some useful sbatch directives [can be found here.](job-resources.md) A full list of commands [can be found in Slurm's documentation for sbatch.](https://slurm.schedmd.com/sbatch.html)

### 2. Software

Because jobs run on different nodes, any shared software that is needed must be loaded via the job script. Software can be loaded in a job script just like it would be on the command line. First, we will purge all software that may be left behind from your working environment on a compile node by running the command:

```bash
module purge
```

Next, you can load whatever software you need by running the following command:

```bash
module load <software>
```

More information about [software modules can be found here.](../compute/modules.md)

### 3. User Scripting

The last part of a job script is the actual script. This includes all user commands that are needed to set up and execute the desired task. Any Linux command can be utilized in this step. Scripting can range from highly complex loops iterating over thousands of files to a simple call to an executable. Below is an simple example of some user scripting:

```bash
echo "== This is the scripting step! =="

touch tempFile1.in
touch tempFile2.in

sleep 30
./executable.exe tempfile1.in tempfile2.in

echo "== End of Job =="
```

## Examples

Job script to run a 5 minute long, 1 node, 1 core C++ Job:

```bash
#!/bin/bash

#SBATCH --nodes=1
#SBATCH --time=00:05:00
#SBATCH --partition=shas-testing
#SBATCH --ntasks=1
#SBATCH --job-name=cpp-job
#SBATCH --output=cpp-job.%j.out

module purge
module load gcc

./example_cpp.exe
```

Job script to run a 7 minute long, 1 node, 4 core C++ OpenMP Job:

```bash
#!/bin/bash

#SBATCH --nodes=1
#SBATCH --time=00:07:00
#SBATCH --partition=atesting
#SBATCH --ntasks=4
#SBATCH --job-name=omp-cpp-job
#SBATCH --output=omp-cpp-job.%j.out

module purge
module load gcc

export OMP_NUM_THREADS=4

./example_omp.exe
```

Job script to run a 10 minute long, 2 node, 16 core C++ MPI Job:

```bash
#!/bin/bash

#SBATCH --nodes=2
#SBATCH --time=00:10:00
#SBATCH --partition=atesting#SBATCH --ntasks=16
#SBATCH --job-name=mpi-cpp-job
#SBATCH --output=mpi-cpp-job.%j.out

module purge
module load intel
module load impi

mpirun -np 16 ./example_mpi.exe
```

## Job Flags

The `sbatch` command supports many optional flags. To review all the options, please visit the Slurm [sbatch page](http://slurm.schedmd.com/sbatch.html). Below are a few flags you may want to consider when running your job via `sbatch`.

| Type                   | Description                                         | Flag                       |
| :--------------------- | :-------------------------------------------------- | :------------------------- |
| Allocations            | Specify an allocation account if you have multiple  | --account=account_no       |
| [Partitions](job-resources.md)         | Specify a partition                                 | --partition=partition_name |
| Sending email          | Receive email at beginning or end of job completion | --mail-type=type           |
| Email address          | Email address to receive the email                  | --mail-user=user           |
| Number of nodes        | The number of nodes needed to run the job           | --nodes=nodes              |
| Number of tasks        | The total number of cores needed to run the job     | --ntasks=processes         |
| [Quality of service](job-resources.md) | Specify a QOS                                       | --qos=qos                  |
| Wall time              | The max. amount of time your job will run for       | --time=wall time           |
| Job Name               | Name your job so you can identify in queue          | --job-name=<jobname>       |


