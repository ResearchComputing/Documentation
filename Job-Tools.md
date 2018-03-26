When running a jobs on research computing resources, there may be times where you like more information on the job you are running. In this video, I will be showcasing several tools within research computing resources that provide in-depth information on jobs.

## Getting information using squeue
The simplest tool you can utilize when you need to pull up out information about your job is the `squeue` command. The `squeue` command pulls up information on all jobs pending or running on the cluster.  

The `squeue` command will print out the job ID, partition, username, job status, number of nodes the job is utilizing, and name of the node that the job is running on for all jobs queued or running within Slurm by default. To specify only jobs that you are running use the `--user` flag. Type:
```bash
$ squeue --user=<your_rc-username>
```
Verbose information on the job can be printed using the `--long` flag. This flag will print out the default information unabbreviated with the addition of a time-limit field. The command using the `--long` flag would look something like:
```bash
$ squeue --user=<your_rc-username> --long
```
Appending the `--start` flag to our command will include the start time of jobs in our output. (Note: the start time presented can be fairly inaccurate because of jobs ending sooner or later than expected)
```bash
$ squeue --user=<your_rc-userame> --start
```
Lastly we can use the `--iterate` flag to iteratively run squeue every n amount of seconds. This means the command will sit on the terminal and will run squeue every n amount of seconds. Running this command would look something like:
```bash
$ squeue --user=<your_rc-username> --start --iterate=<n_seconds>
```

### Advanced squeue formatting

We can pull more information on each job using the `--format` flag. The output flag allows us to specify what information we would like to see in what order. The flag takes in several arguments that specify what item you would like to be in each field. Each argument is formatted as such:
```
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
	$ squeue --user=<your_rc-username> -- format=%8U%j%.12J
For more information about the usage of squeue, visit the Slurm manual [here](https://slurm.schedmd.com/squeue.html)

## Stopping jobs using scancel
Sometimes you may need to stop a job while it’s running entirely. The best way to accomplish this is with the `scancel` command. The `scancel` command allows you to cancel jobs you are running on research computing resources using the job’s job ID. The command looks like this:
```
$ scancel <job_id-number>
```
To cancel multiple jobs, you can use a comma-separated list of job IDs:
```	
$ scancel <job_id-number1>, <job_id-number2>, <job_id-number3>
```
For more information about the scancel command visit the Slurm manual [here](https://slurm.schedmd.com/scancel.html)

## Controlling Jobs with scontrol
The `scontrol` command allows users further control of their jobs through Slurm. A few examples of this include pausing a job as its running, holding a job from running, or creating a job checkpoint.
To pause a job, we can use `scontrol` with the `suspend` command:
```bash
$ scontrol suspend <job_id-number>
```
To resume a job, we can use `scontrol` with the `resume` command:
```bash
$ scontrol resume <job_id-number>
```
To hold a job in queue before it begins running we can use the hold command. This would look like:
```bash	
$ scontrol hold <job_id-number>
```
We can then release a held job using the release command. The command would look like this on the command line. 
```bash
$ scontrol release <job_id-number>
```
Scontrol can also provide detailed information on jobs using the `show job` command. The information provided from this command is very verbose and detailed, so be sure to either clear your terminal window, grep certain information from the command, or pipe the output to a seperate text file. 
For more information on scontrol, visit the Slurm manual [here](https://slurm.schedmd.com/scontrol.html)

## Getting information on older jobs using sacct
The `sacct` command allows users to pull up information about jobs that they have run through Slurm. The `sacct` command lets up pull up job information by using the job ID:
```
$ sacct --jobs=<job_id-number>
```
or by rc username:
```
$ sacct --user=<your_rc-username>
```
By default, `sacct` will only pull up jobs that were run that took place on the current day. We can use the `--starttime` flag so the command knows to look beyond its short-term cache of jobs The format of the flag is:  `--starttime=<Year-Month-Day>`
```bash
$ sacct –-jobs=<job_id-number> –-starttime=2018-10-10
```
To see the long version of this output, use the `--long` flag:
```bash
$ sacct –-job <your job id> –-starttime=2017-10-10 --long
```
You can also format the `sacct` output to show the fields you want to see:
```bash
$ sacct –-jobs=<your job id> –-starttime=2017-10-10 --format=jobid,jobname,qos,nnodes,ncpu,maxrss,cputime,avecpu,elapsed
```

For more information on sacct check out the Slurm page [here](https://slurm.schedmd.com/sacct.html).

