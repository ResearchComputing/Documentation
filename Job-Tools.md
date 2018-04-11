## Table of Contents
* [Overview](#overview)
* [Finding queuing information with squeue](#finding-queuing-information-with-squeue)
* [Stopping jobs with scancel](#stopping-jobs-with-scancel)
* [Finding status information with sstat](#finding-status-information-with-sstat)
* [Analyzing past jobs with sacct](#analyzing-past-jobs-with-sacct)
* [Finding fair share information with sshare](#finding-fair-share-information-with-sshare)
* [Controlling queued and running jobs using scontrol](#controlling-queued-and-running-jobs-using-scontrol)

## Overview


When running a job on Research Computing resources, there may be times where you would like specific information about about your job. You may also wish to have some extended control over jobs that you have submitted to Summit. This tutorial showcases several tools that provide information about jobs as well as extended control over submitted jobs.

## Finding queuing information with squeue
The `squeue` command is a tool we use to pull up information about the jobs in queue. By default, the `squeue` command will print out the _job ID, partition, username, job status, number of nodes the job is utilizing,_ and _name of nodes the job is running on_ for all jobs queued or running within Slurm. Usually you wouldn't need information for all Jobs that were queued in the system, so we can specify jobs that only you are running, use the `--user` flag:

```bash
$ squeue --user=your_rc-username
```

We can output non-abbreviated information with the `--long` flag. This flag will print out the non-abbreviated default information with the addition of a timelimit field:

```bash
$ squeue --user=your_rc-username --long
```

The squeue also provides users with a means to calculate a jobs estimated start time by adding the `--start` flag to our command. This will append Slurm's estimated start time for each job in our output information. (Note: The start time provided by this command can be inaccurate. This is because the time calculated is based off of jobs queued or running in the system. If a job with a higher priority is queued after the command is run, you job may be delayed.)

```bash
$ squeue --user=your_rc-username --start
```
When checking the status of a job, you may want to repeatedly call the squeue command to check for updates. We can accomplish this by adding the `--iterate` flag to our squeue command. This will run squeue every _n seconds_, allowing for a frequent, continuous update of queue information without needing to repeatedly call squeue:

```bash
$ squeue --user=your_rc-username --start --iterate=n_seconds
```

Press `ctrl`-`z` to stop the command from looping and bring you back to the terminal.

For more information on squeue, [visit the Slurm page on squeue](https://slurm.schedmd.com/squeue.html)

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

The `sstat` command allows users to easily pull up status information about their jobs. This includes information about CPU usage, Task information, Node information, Resident Set Size (RSS), and Virtual Memory (VM). We can invoke the `sstat` as such:
```
$ sstat --jobs=your_job-id
```
By default, sstat is unlikely to pull up information you'd like with the commands default output. To remedy this, we can use the `--format` flag to choose what we want in our output. The format flag is handled by a list of comma separated variables which specify output data:

```bash
$ sstat --jobs=your_job-id --format=var_1,var_2, ... , var_N
```
A chart of some these variables are listed in the table below:

Variable    | Description
------------|------------
avecpu      | Average CPU time of all tasks in job.
averss      | Average resident set size of all tasks.
avevmsize   | Average virtual memory of all tasks in a job.
jobid       | The id of the Job.
maxrss      | Maximum number of bytes read by all tasks in the job.
maxvsize    | Maximum number of bytes written by all tasks in the job.
ntasks      | Number of tasks in a job.

A full list of variables that specify data handled by sstat can be found with the `--helpformat` flag or by [visiting the slurm page on sstat](https://slurm.schedmd.com/sstat.html).

## Analyzing past jobs with sacct 
The `sacct` command allows users to pull up status information about past jobs. We can use a job's id:

```bash
$ sacct --jobs=your_job-id
```

...or your rc username:

```bash
$ sacct --user=your_rc-username
```

To pull up accounting information on jobs ran at an earlier time.

By default, `sacct` will only pull up jobs that were ran on the current day. We can use the `--starttime` flag so the command knows to look beyond its short-term cache of jobs.

```bash
$ sacct –-jobs=your_job-id –-starttime=YYYY-MM-DD
```

To see a non-abbreviated version of sacct output, use the `--long` flag:

```bash
$ sacct –-job your_job-id –-starttime=YYYY-MM-DD --long
```

### Formatting Output with sacct

Like sstat, the standard output of `sacct` will usually not provide the information we want. To remedy this, we can use the `--format` flag to choose what we want in our output. Similarly, the format flag is handled by a list of comma separated variables which specify output data:

```bash
$ sacct --user=your_rc-username --format=var_1,var_2, ... , var_N
```

A chart of some variables is provided below:

Variable    | Description
------------|------------
account     | Account the job ran under.
avecpu      | Average CPU time of all tasks in job.
averss      | Average resident set size of all tasks in the job.
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

