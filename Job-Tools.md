## Table of Contents
* [Overview](#Overview)
* [Finding queuing information with squeue](#Finding-queuing-information-with-squeue)
* [Stopping jobs with scancel](#Stopping-jobs-with-scancel)
* [Finding status information with sstat](#Finding-status-information-with-sstat)
* [Analyzing past jobs with sacct](#Analyzing-past-jobs-with-sacct)
* [Finding fair share information with sshare](#Finding-fair-share-information-with-sshare)
* [Controlling queued and running jobs using scontrol](#Controlling-queued-and-running-jobs-using-scontrol)

## Overview
When running a job on Research Computing resources, there may be times where you would like specific information about about your job. You may also wish to have some extended control over jobs that you have submitted to Summit. This tutorial showcases several tools that provide information about jobs as well as extended control over submitted jobs.

## Finding queuing information with squeue
The `squeue` command will print out the _job ID, partition, username, job status, number of nodes the job is utilizing,_ and _name of nodes the job is running on_ for all jobs queued or running within Slurm by default. To specify jobs that only you are running, use the `--user` flag:

```bash
$ squeue --user=your_rc-username
```

Squeue can also output non-abbreviated information on jobs with the `--long` flag. This flag will print out the non-abbreviated default information with the addition of a timelimit field. The command using the flag would look like:

```bash
$ squeue --user=your_rc-username --long
```

The squeue also allows users to calculate an estimated start time by adding the `--start` flag to our command. This will append Slurm's estimated start time for each job in our output information. (Note: The start time provided by this command can be inaccurate. This is because the time calculated is based off of jobs queued or running in the system. If a job with a higher priority is queued after the command is run, you job may be delayed.)

```bash
$ squeue --user=your_rc-username --start
```

Lastly squeue provides us with a means to continuously repeat our squeue command. This will run squeue every _n seconds_, allowing for a frequent, continuous update of queue information without needing to repeatedly call squeue. We can accomplish this by adding the `--iterate` flag to our squeue command.  Running squeue with this flag would look like:

```bash
$ squeue --user=your_rc-username --start --iterate=n_seconds
```

Pressing `ctrl`-`z` will stop the command from looping and bring you back to the terminal.

### Formatting squeue output

We can obtain even more information about each job using the `--format` flag. The output flag allows us to specify what information we would like to see in what order. The flag takes in several arguments that specify what item you would like to be in each field. Each argument is formatted as such:

```
%[.][size_of_field][information_variable]
```

where `[.]` tells whether or not this field should be right justified, `[size_of_field]` is the minimum size of space the field (If nothing is specified then defaults to space needed), and `[information_variable]` is the data we want the field to actually hold. Because the list of variables available for this flag is large, we’ll just be going over a couple of these options.

Format code | Description
---|-----------------------------
%A | Job ID
%C | Number of CPUs requested or allocated
%j | Job name
%J | Number of threads per core requested by the job
%m | Minimum size of memory requested by the job in MB
%M | Time used by the job
%p | Priority of the job
%S | Actual or expected job start time
%T | Job state
%U | User ID for a job
%v | Reservation for the job

For example, let’s set up our output to display the job id, the job name, the number of CPUs requested, the job state, and the expected start time, all left justified:

```bash
$ squeue --user=your_rc-username --format=%A%j%C%T%S
```

Now let’s set our out output to display a username with a 8 character minimum chart value and a right justified ‘job-name’ with a 12 character minimum chart value.

```bash
$ squeue --user=your_rc-username --format=%9U%7j%.12J
```

For more information, [visit the Slurm page on squeue](https://slurm.schedmd.com/squeue.html)

## Stopping jobs with scancel
Sometimes you may need to stop a job entirely while it’s running. The best way to accomplish this is with the `scancel` command. The `scancel` command allows you to cancel jobs you are running on Research Computing resources using the job’s ID. The command looks like this:

```bash
$ scancel your_job-id
```

To cancel multiple jobs, you can use a comma-separated list of job IDs:

```bash
$ scancel your_job-id1, your_job-id2, your_jobiid3
```

For more information, [visit the Slurm manual on scancel](https://slurm.schedmd.com/scancel.html)

## Finding status information with sstat






## Analyzing past jobs with sacct 
The `sacct` command allows users to pull up status information about past jobs. We can use a job's id:

```bash
$ sacct --jobs=your_job-id
```
...or your rc username:
```bash
$ sacct --user=your_rc-username
```

to pull up accounting information on jobs ran at an earlier time.

By default, `sacct` will only pull up jobs that were ran on the current day. We can use the `--starttime` flag so the command knows to look beyond its short-term cache of jobs.
```bash
$ sacct –-jobs=your_job-id –-starttime=YYYY-MM-DD
```
To see a non-abbreviated version of sacct output, use the `--long` flag:
```bash
$ sacct –-job your_job-id –-starttime=YYYY-MM-DD --long
```

### Formatting Output with sacct

Oftentimes, the standard output of `sacct` will not provide the information we want. To remedy this, we can use the `--format` flag to choose what we want in our output. The format flag is handled by a list of comma separated variables which specify output data. The command with the `--format` flag looks as such:

```bash
$ sacct --user=your_rc-username --format=var_1,var_2, ... , var_N
```

A chart of some variables is provided below:

Variable    | Description
------------|------------
account     | Account the job ran under.
avecpu      | Average CPU time of all tasks in job.
cputime     | Formatted (Elapsed time * CPU) count used by a job or step.
elapsed     | Jobs elapsed time formated as DD-HH:MM:SS.
exitcode    | The exit code returned by the job script or salloc.
jobid       | The id of the Job.
jobname     | The name of the Job.
maxdiskread | Maximum number of bytes read by all tasks in the job.
maxdiskwrite| Maximum number of bytes written by all tasks in the job.
maxrss      | Maximum resident set size of all tasks in the job.
ncpus       | Amount of allocated CPUs.
nnodes      | Then number of nodes used in a job.
ntasks      | Number of tasks in a job.
priority    | Slurm priority.
qos         | Quality of service.
reqcpu      | Required number of CPUs
reqmem      | Required amount of memory for a job.
user        | Username of the person who ran the job.

A full list of variables that specify data handled by sacct can be found with the `--helpformat` flag or by [visiting the slurm page on sacct](https://slurm.schedmd.com/sacct.html).

#### Examples:
Suppose you want to find information jobs that were ran on March 12, 2018. You want to show information regarding the job name, the number of nodes used in the job, the number of cpus, the maxrss, and the elapsed time. Your command would look like this:

```bash
$ sacct --jobs=your_job-id --starttime=2018-03-12 --format=jobname,nnodes,ncpus,maxrss,elapsed
```

Now you would like to pull up information on jobs that were ran on February 21, 2018. You would like information on job ID, job name, QoS, Number of Nodes used, Number of CPUs used, Maximum RSS, CPU time, Average CPU time, and elapsed time. Your command would look like this:

```bash
$ sacct –-jobs=your_job-id –-starttime=2018-02-21 --format=jobid,jobname,qos,nnodes,ncpu,maxrss,cputime,avecpu,elapsed
```

## Finding fair share information with sshare







## Controlling queued and running jobs using scontrol
The `scontrol` command provides users extended control of their jobs through Slurm. This includes actions like suspending a job, holding a job from running, or pulling extensive status information on jobs.

To suspend a job that is currently running on the system, we can use `scontrol` with the `suspend` command. This will stop a running job on its current step that can be resumed at a later time. We can suspend a job by typing the command:

```bash
$ scontrol suspend <job_id>
```

To resume a paused job, we use `scontrol` with the `resume` command:

```bash
$ scontrol resume <job_id>
```

Holding a job differs from suspending a job by placing the job in a low priority state. Holding a job puts a pending jobs priority to the 0, stopping the job from being run. To hold a pending job we can use the `hold` command:

```bash	
$ scontrol hold job_id
```

We can then release a held job using the release command:

```bash
$ scontrol release job_id
```

Scontrol can also provide information on jobs using the `show job` command. The information provided from this command is quite extensive and detailed, so be sure to either clear your terminal window, grep certain information from the command, or pipe the output to a separate text file. This command would look similar to:

```bash
# Output to console
$ scontrol show job job_id

# Streaming output to a textfile
$ scontrol show job job_id > outputfile.txt

# Piping output to Grep
$ scontrol show job job_id | grep Time
```

For more information, [visit the Slurm page on scontrol](https://slurm.schedmd.com/scontrol.html)

