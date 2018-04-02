When running a jobs on research computing resources, there may be times where you like more information on the job you are running. In this video, I will be showcasing several tools within research computing resources that provide in-depth information on jobs.

## Getting information using squeue
The simplest tool you can utilize when needed to obtain information about your job is via the `squeue` command. The `squeue` command pulls up information on all jobs pending or running on the cluster.  

The `squeue` command will print out the _job ID, partition, username, job status, number of nodes the job is utilizing,_ and _name of the node_ that the job is running on for all jobs queued or running within Slurm by default. To specify only jobs that you are running use the `--user` flag. Type:

```bash
$ squeue --user=<your_rc-username>
```

Verbose information on the job can be printed using the `--long` flag. This flag will print out the non-abbreviated default information with the addition of a time limit field. The command using the flag would look something like:

```bash
$ squeue --user=<your_rc-username> --long
```

The squeue also allows users to pull up information on an estimated start time by appending the `--start` flag to our command. This will add Slurm's estimated start time of each job to our output information. (Note: the start time presented can be fairly inaccurate because of jobs ending sooner or later than expected)

```bash
$ squeue --user=<your_rc-userame> --start
```

Lastly squeue provides us with an ability to repeatly call squeue to frequently check on the progress of a job. We can accomplish this by appending the `--iterate` flag to iteratively run squeue every n amount of seconds. This means the command will run squeue every n amount of seconds without stopping. Running this command would look something like:

```bash
$ squeue --user=<your_rc-username> --start --iterate=<n_seconds>
```

Pressing `ctrl`-`z` will stop the command from looping and bring you back to the terminal.

### Formatting output with squeue

We can pull more information on each job using the `--format` flag. The output flag allows us to specify what information we would like to see in what order. The flag takes in several arguments that specify what item you would like to be in each field. Each argument is formatted as such:

```bash
%[.][size_of_field](information_variable)
```

where `[.]` tells whether or not this field should be right justified, `[size_of_field]` is the minimum size of space the field (If nothing is specified then defaults to space needed), and `(information_variable)` is the data we want the field to actually carry. Because the list of information variables available for this flag is very large, we’ll just be going over a couple of these options.

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

For example let’s set up our output to display the job id, the job name, the number of CPUs requested, the job state, and the expected start time, all left justified:
```bash
$ squeue --user=<your_rc-username> --format=%A%j%C%T%S
```
Now let’s set our out output to display a username with a 8 character minimum chart value and a right justified ‘job-name’ with a 12 character minimum chart value.
	$ squeue --user=<your_rc-username> -- format=%9U%7j%.12J

For more information, [visit the Slurm page on squeue](https://slurm.schedmd.com/squeue.html)

## Stopping jobs using scancel
Sometimes you may need to stop a job while it’s running entirely. The best way to accomplish this is with the `scancel` command. The `scancel` command allows you to cancel jobs you are running on research computing resources using the job’s job ID. The command looks like this:

```bash
$ scancel <job_id-number>
```

To cancel multiple jobs, you can use a comma-separated list of job IDs:

```bash
$ scancel <job_id-number1>, <job_id-number2>, <job_id-number3>
```

For more information, [visit the Slurm manual on scancel](https://slurm.schedmd.com/scancel.html)

## Controlling Jobs with scontrol
The `scontrol` command allows users further control of their jobs through Slurm. A few examples of this include pausing a job as its running, holding a job from running, or printing information about the job.

To pause a job that is currently running on the system, we can use `scontrol` with the `suspend` command. This will stop a running job on its current step that can be resumed at a later time. We can pause a job by typing in the command:

```bash
$ scontrol suspend <job_id-number>
```

To resume a paused job, we use `scontrol` with the `resume` command:

```bash
$ scontrol resume <job_id-number>
```

Holding a job differs from suspending a job in the state in which the command can be executed. Holding a job puts a pending jobs priority to the 0, stopping the job from being run. To hold a pending job we can use the `hold` command:

```bash	
$ scontrol hold <job_id-number>
```

We can then release a held job using the release command. The command would look like this on the command line.

```bash
$ scontrol release <job_id-number>
```

Scontrol can also provide detailed information on jobs using the `show job` command. The information provided from this command is very verbose and detailed, so be sure to either clear your terminal window, grep certain information from the command, or pipe the output to a separate text file. This command would look similar to:

```bash
$ scontrol show job <job_id-number>
```

For more information, [visit the Slurm page on scontrol](https://slurm.schedmd.com/scontrol.html)

## Getting information on older jobs using sacct
The `sacct` command allows users to pull up information about jobs that they have run through Slurm. With the `sacct` command, we can pull up job information by using the job ID:

```bash
$ sacct --jobs=<job_id-number>
```

or by rc username:
```bash
$ sacct --user=<your_rc-username>
```

By default, `sacct` will only pull up jobs that were run that took place on the current day. We can use the `--starttime` flag so the command knows to look beyond its short-term cache of jobs The format of the flag is:  `--starttime=<Year-Month-Day>`
```bash
$ sacct –-jobs=<job_id-number> –-starttime=2018-10-10
```
To see an on-abbreviated version of sacct output, use the `--long` flag:
```bash
$ sacct –-job <your job id> –-starttime=2017-10-10 --long
```

### Formatting Output with sacct

Oftentimes, the standard output of `sacct` will not provide the information we want. To remedy this, we can use the `--format` flag to choose what we want in our output. The format flag is handled by a list of comma separated variables that specify data that sacct handles. The command with the `--format` flag looks as so:

```bash
$ sacct --user=<your_rc-username> --format=<item1>,<item2>,<item3>
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

#### Examples:
Suppose you want to find information jobs that were ran on March 12, 2018. You want to show information regarding the job name, the number of nodes used in the job, the number of cpus, the maxrss, and the elapsed time. Your `--format` flag would look like this:

```bash
$ sacct --jobs=<your_job-id> --starttime=<2018-03-12> --format=jobname,nnodes,ncpus,maxrss,elapsed
```

This time you would like to pull up information on jobs that were ran on February 21, 2018. You would like information on job ID, job name, QoS, Number of Nodes used, Number of CPUs used, Maximum RSS, CPU time, Average CPU time, and elapsed time. Your script would look like this:

```bash
$ sacct –-jobs=<your_job-id> –-starttime=<job_date> --format=jobid,jobname,qos,nnodes,ncpu,maxrss,cputime,avecpu,elapsed
```
A full list of variables that specify data handled by sacct can be found with the `--helpformat` flag or by [visiting the slurm page on sacct](https://slurm.schedmd.com/sacct.html).

