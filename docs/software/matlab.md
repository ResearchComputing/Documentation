# Matlab

Research Computing (RC) provides a large suite of software on RC
resources. In this tutorial we will learn how to run Matlab on these
resources. The tutorial assumes you are familiar with Matlab and basic
Linux terminal commands.

There are two basic ways to run Matlab (or many other kinds of
software) on RC resources. The first is through an interactive job,
and the second is through a batch job. An interactive job allows one
to work in real-time with Matlab. Two reasons you may want to do this
would be if you are actively debugging your code, or if you would like
to use the GUI (in this instance, the Matlab Desktop). However, there
might be other reasons you would like to work interactively with
Matlab.

The second way to run Matlab on RC resources is through a
batch job. This allows the job to run in the background when resources
become available. You may choose to use this method if you have a
large job that may wait in the queue for awhile, or if you are not
debugging or in need of a GUI. Both ways to work with Matlab are
below.


## Running Matlab Interactive Jobs

Running Matlab interactive jobs on RC resources is both a simple and
easy task to accomplish. In this section we will learn 2 ways to launch
Matlab as an interactive job: 

1. MATLAB Interactive Application (CURC OnDemand):

	You can access a full Matlab GUI in your browser with CURC 
OnDemand. CURC OnDemand is a browser-based, integrated, single access 
point for HPC resources. It includes access to interactive apps such 
as Matlab, a virtual desktop, and more. 

	You can find instructions to start an interactive Matlab session in our [OnDemand documentation](../gateways/OnDemand.md#matlab). 


2. Interactive SLURM job:

	For more information on launching
	interactive jobs [check out our interactive jobs
	tutorial](../running-jobs/interactive-jobs.md)

	Begin by launching an interactive job by loading slurm/alpine into
	your environment and running the `sinteractive` command.

	```bash
	module load slurm/alpine
	sinteractive
	```

	From here you will load the Matlab module into your environment.

	```bash
	module load matlab
	```

	Lastly we will run Matlab from the terminal.

	```bash
	matlab -nosplash
	```

	By default Matlab will load an interactive terminal session. If you would like to access the Matlab GUI 
	then simply run Matlab with X11 forwarding enabled.

	To find out how you enable X11 forwarding in your terminal 
session, check out our [X11 forwarding tutorial.](../running-jobs/interactive-jobs.md#interactive-gui-applications)


## Running Matlab Batch Jobs

Here, we will learn how to run a Matlab script in a non-interactive
batch job. For more general information on batch job scripts on
Alpine, [please see our tutorial on batch 
jobs](../running-jobs/batch-jobs.md)

Let’s begin by constructing a small Matlab script that prints ‘hello
world’ to the user.  The Matlab script we will use for the purposes of
this tutorial is called `hello_world.m` and contains only one line,
the Matlab command:

```matlab
fprintf(‘Hello world\n’)
```

Which simply prints "Hello world" when called.

Next, we will construct a batch script that will enable us to run
this job. The batch script organizes the variety of flags slurm needs
to run a job and specifies the software commands we want to
execute. One advantage of batch scripts is that they are easily
reusable and adaptable for other similar tasks.

We will run this job using a bash script titled: `slurm_hello.sh`,
which contains the following lines:

```bash
#!/bin/bash

#SBATCH --nodes=1
#SBATCH --time=0:01:00
#SBATCH --partition=atesting
#SBATCH --qos=testing
#SBATCH --ntasks=1
#SBATCH --job-name=Matlab_Hello_World
#SBATCH --output=Matlab_Hello_World.out

module purge

module load matlab

matlab -nodesktop -nodisplay -r ‘clear; hello_world;’
```

This file has a few basic parts:

1. The first line specifies that it is a bash shell script, and
   ensures the rest of the lines will be interpreted in the correct
   shell.

2. The lines beginning with `#SBATCH` specify the Slurm parameters
   that will be used for this job. These lines are viewed as comments
   by bash, but will be read by Slurm. Of particular note is the
   `--output` parameter which specifies the file where stderr and
   stdout (including the output from our Matlab script) will be
   written. For a description of the Slurm parameters, [please see the
   general Slurm documentation
   here](https://slurm.schedmd.com/sbatch.html)

3. The lines beginning with `module purge` remove any unneeded
   software and ensure that the appropriate Matlab module is loaded on
   the compute node.

4. The final line calls Matlab and instructs it to run our
   script. This entire line includes commands that are specific to
   Matlab; the `nodesktop` and `nodisplay` flags ensure that the
   Matlab Desktop will not open, and the `r` flag will run the script
   `hello_world`. The `clear` command forces Matlab to clear any
   existing variables, and is simply included as good coding practice.

You have now completed your batch script. After saving the script and
exiting your text editor, run the job as follows:

```bash
sbatch slurm_hello.sh
```

Once the job has run, the output of the Matlab script, "Hello world"
will be shown in `Matlab_Hello_World.out`.


## Parallel Matlab on Alpine

To fully utilize the multi-core capabilities of Alpine to speed up
jobs, most code must first be parallelized. Matlab has many built in
tools to accomplish this task. In this tutorial we will parallelize
our "Hello World" program.

Let’s begin with the Matlab script we created above called
`hello_world.m`. First we will modify the fprintf line so that it
includes a variable 'i' that will print out the iteration of the
parallel loop.

```matlab
fprintf(“Hello World from process %i”, i)
```

Next, we need to encapsulate the print statement in a parallel 'for'
loop. Matlab uses the construct `parfor` to separate the task into
multiple threads. In order to utilize the `parfor` command one must
ensure that the Parallel Computing Toolbox is available as part of the
Matlab software package. CURC has this available and thus no additional
action is required on your part if you are utilizing CURC resources.

The order of runtime in the loop is not guaranteed, so the output may
not be in sequential order. The loop is formatted as such:

```matlab
parfor(i = initial_Value:final_Value, maximum_amount_of_threads)
```

For example, let’s use `parfor` to implement an 5-iteration loop with a
maximum of 4 processors in our script:

```matlab
parfor(i = 1:5, 4)
        fprintf("Hello, World from process %i", i)
end
```

Now all we have left to do is modify our batch script to specify that
we want to run 4 tasks on the node (we can use up to 64 cores on each
‘amilan' node on Alpine). We can also change the name of the job and the
output file if we choose.

```bash
#!/bin/bash

#SBATCH --nodes=1
#SBATCH --time=0:01:00
#SBATCH --partition=atesting
#SBATCH --qos=testing
#SBATCH --ntasks=4
#SBATCH --job-name=Matlab_Parallel_Hello
#SBATCH --output=Matlab_Parallel_Hello.out

module purge

module load matlab

matlab -nodesktop -nodisplay -r 'clear; hello_world;'
```

Now we run the job using the `sbatch` command shown above, and our
output in `Matlab_Parallel_Hello.out` will be as follows (the process
order may be different in your output):

```
Hello World from process 4
Hello World from process 1
Hello World from process 2
Hello World from process 3
```

CURC Matlab currently does not support parallelization across nodes,
only across cores on one node.

