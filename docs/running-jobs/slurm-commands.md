# Useful Slurm commands

Slurm provides a variety of tools that allow a user to manage and
understand their jobs. This tutorial will introduce these tools, as
well as provide details on how to use them.

## Finding queuing information with `squeue`

The `squeue` command is a tool we use to pull up information about the
jobs in queue. By default, the squeue command will print out the
*__job ID__*, *__partition__*, *__username__*, *__job status__*,
*__number of nodes__*, and *__name of nodes__* for all jobs queued or
running within Slurm. Usually you wouldn't need information for all
jobs that were queued in the system, so we can specify jobs that only
you are running with the `--user` flag:

```bash
$ squeue --user=your_rc-username
```

We can output non-abbreviated information with the `--long` flag. This
flag will print out the non-abbreviated default information with the
addition of a *__timelimit__* field:

```bash
$ squeue --user=your_rc-username --long
```

The squeue command also provides users with a means to calculate a
job's estimated start time by adding the `--start` flag to our
command. This will append Slurm's estimated start time for each job in
our output information. 
> Note: The start time provided by this command
can be inaccurate. This is because the time calculated is based on
jobs queued or running in the system. If a job with a higher priority
is queued after the command is run, your job may be delayed.

```bash
$ squeue --user=your_rc-username --start
```

When checking the status of a job, you may want to repeatedly call the
squeue command to check for updates. We can accomplish this by adding
the `--iterate` flag to our squeue command. This will run squeue every
n seconds, allowing for a frequent, continuous update of queue
information without needing to repeatedly call squeue:

```bash
$ squeue --user=your_rc-username --start --iterate=n_seconds
```

Press `ctrl`-`c` to stop the command from looping and bring you back
to the terminal.

For more information on squeue, [visit the Slurm page on
squeue](https://slurm.schedmd.com/squeue.html)

## Stopping jobs with `scancel`

Sometimes you may need to stop a job entirely while it’s running. The
best way to accomplish this is with the `scancel` command. The scancel
command allows you to cancel jobs you are running on Research
Computing resources using the job’s ID. The command looks like this:

```bash
$ scancel your_job-id
```

To cancel multiple jobs, you can use a comma-separated list of job IDs:

```bash
$ scancel your_job-id1, your_job-id2, your_jobiid3
```

For more information, [visit the Slurm manual on scancel](https://slurm.schedmd.com/scancel.html)

## Analyzing currently running jobs with `sstat`

The `sstat` command allows users to easily pull up status information
about their currently running jobs. This includes information about *__CPU usage__*,
*__task information__*, *__node information__*, *__resident set size
(RSS)__*, and *__virtual memory (VM)__*. We can invoke the sstat
command as such:

```bash
$ sstat --jobs=your_job-id
```

By default, sstat will pull up significantly more information than
what would be needed in the commands default output. To remedy this,
we can use the `--format` flag to choose what we want in our
output. The format flag takes a list of comma separated variables
which specify output data:

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

For an example, let's print out a job's average job id, cpu time, max
rss, and number of tasks. We can do this by typing out the command:

```bash
sstat --jobs=your_job-id --format=jobid,cputime,maxrss,ntasks
```

A full list of variables that specify data handled by sstat can be
found with the `--helpformat` flag or by [visiting the slurm page on
sstat](https://slurm.schedmd.com/sstat.html).

## Analyzing past jobs with `sacct`

The `sacct` command allows users to pull up status information about
past jobs. This command is very similar to sstat, but is used on jobs
that have been previously run on the system instead of currently
running jobs. We can use a job's id...

```bash
$ sacct --jobs=your_job-id
```

...or your Research Computing username...

```bash
$ sacct --user=your_rc-username
```

...to pull up accounting information on jobs run at an earlier time.

By default, sacct will only pull up jobs that were run on the current
day. We can use the `--starttime` flag to tell the command to look
beyond its short-term cache of jobs.

```bash
$ sacct –-jobs=your_job-id –-starttime=YYYY-MM-DD
```

To see a non-abbreviated version of sacct output, use the `--long`
flag:

```bash
$ sacct –-jobs=your_job-id –-starttime=YYYY-MM-DD --long
```

### Formatting `sacct` output

Like `sstat`, the standard output of sacct may not provide the
information we want. To remedy this, we can use the `--format` flag to
choose what we want in our output. Similarly, the format flag is
handled by a list of comma separated variables which specify output
data:

```bash
$ sacct --user=your_rc-username --format=var_1,var_2, ... ,var_N
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
nnodes      | The number of nodes used in a job.
ntasks      | Number of tasks in a job.
priority    | Slurm priority.
qos         | Quality of service.
reqcpu      | Required number of CPUs
reqmem      | Required amount of memory for a job.
user        | Username of the person who ran the job.

As an example, suppose you want to find information about jobs that
were run on March 12, 2018. You want to show information regarding the
job name, the number of nodes used in the job, the number of cpus, the
maxrss, and the elapsed time. Your command would look like this:

```bash
$ sacct --jobs=your_job-id --starttime=2018-03-12 --format=jobname,nnodes,ncpus,maxrss,elapsed
```

As another example, suppose you would like to pull up information on
jobs that were run on February 21, 2018. You would like information on
job ID, job name, QoS, Number of Nodes used, Number of CPUs used,
Maximum RSS, CPU time, Average CPU time, and elapsed time. Your
command would look like this:

```bash
$ sacct –-jobs=your_job-id –-starttime=2018-02-21 --format=jobid,jobname,qos,nnodes,ncpu,maxrss,cputime,avecpu,elapsed
```

A full list of variables that specify data handled by sacct can be
found with the `--helpformat` flag or by [visiting the slurm page on
sacct](https://slurm.schedmd.com/sacct.html).

## Controlling queued and running jobs using `scontrol`

The `scontrol` command provides users extended control of their jobs
run through Slurm. This includes actions like suspending a job,
holding a job from running, or pulling extensive status information on
jobs.

To suspend a job that is currently running on the system, we can use
scontrol with the `suspend` command. This will stop a running job on
its current step that can be resumed at a later time. We can suspend a
job by typing the command:

```
$ scontrol suspend job_id
```

To resume a paused job, we use scontrol with the `resume` command:

```bash
$ scontrol resume job_id
```

Slurm also provides a utility to hold jobs that are queued in the
system. Holding a job will place the job in the lowest priority,
effectively "holding" the job from being run. A job can only be held
if it's waiting on the system to be run. We use the `hold` command to
place a job into a held state:

```bash
$ scontrol hold job_id
```

We can then release a held job using the `release` command:

```bash
$ scontrol release job_id
```

`scontrol` can also provide information on jobs using the `show job`
command. The information provided from this command is quite extensive
and detailed, so be sure to either clear your terminal window, grep
certain information from the command, or pipe the output to a separate
text file:

```bash
# Output to console
$ scontrol show job job_id

# Streaming output to a textfile
$ scontrol show job job_id > outputfile.txt

# Piping output to Grep and find lines containing the word "Time"
$ scontrol show job job_id | grep Time
```

For a full primer on grep and regular expressions, [visit GNU's page
on Grep](https://www.gnu.org/software/grep/manual/grep.html)

For more information on scontrol, [visit the Slurm page on
scontrol](https://slurm.schedmd.com/scontrol.html)

