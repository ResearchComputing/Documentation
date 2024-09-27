# Running Applications with Jobs

<iframe width="560" height="315" src="https://www.youtube.com/embed/dZLSEyYTiBM" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

Because our HPC system is shared among many researchers, Research Computing manages system usage through jobs. **Jobs** are simply an allotment of resources that can be used to execute processes. Research Computing uses a program named the *Simple Linux Utility for Resource Management*, or **Slurm**, to create and manage jobs.

In order to run a program on a cluster, you must request resources from Slurm to generate a job. Resources can be requested from a login node or a compile node. You must then provide commands to run your program on those requested resources. Where you provide your commands depends on whether you are running a [batch job](batch-jobs.md) or an [interactive job](interactive-jobs.md).

When you run a batch job or an interactive job, it will be placed in a queue until resources are available. 

```{seealso}
A detailed guide on the Slurm queue and accounting tools can be found in the [Useful Slurm Commands](slurm-commands.md) page.
```

## Batch Jobs

The primary method of running applications on Research Computing resources is through a batch job. A **batch job** is a job that runs on a compute node with little or no interaction with the users. You should use batch jobs for:

- Any computationally expensive application that could take hours or days to run
- Any application that requires little or no user input
- Applications that you do not need to monitor extensively

Unlike running an application on your personal machine, you do not call the application you wish to run directly. Instead, you create a **job script** that includes a call to your application. Job scripts are simply a set of resource requests and commands. When a job script is run, all the commands in the job script are executed on a compute node. 

Once created, you can run your job script by passing it to the Slurm queue with the `sbatch` command followed by your job script name:

```bash
sbatch <your-jobscript-name>
```

If no job script is provided then `sbatch` will take whatever commands follow as standard input.

```{seealso}
A detailed guide on constructing and running Job scripts can be found in the [Batch Jobs and Job Scripting](batch-jobs.md) page.
```

## Interactive Jobs

Another method of running applications on Research Computing resources is through an interactive job. As the name would imply, an **interactive job** is a job that allows users to interact with requested resources in real-time. Users can run applications, execute scripts, or run other commands directly on a compute node. Interactive jobs should be used for:

- Debugging applications or workflows
- Any application that requires user input at runtime
- Any application with a GUI (Graphical User Interface)

You can request an interactive job by using the `sinteractive` command. Unlike the `sbatch`, resources must be requested via the command line through the use of flags. Though running sinteractive without any flags is possible, this will result in default values being used for your jobs. Research Computing highly recommends you provide a `time` directive to avoid long queue times. 

```bash
sinteractive --time=00:10:00
```

The example above will run an interactive job that will run a terminal session on one core of one node with the interactive quality of service (QoS) for ten minutes. Once the interactive session has started you can run any interactive terminal application you may need on the command line. 

```{seealso}
More details on sinteractive parameters can be found in the [Slurm Flags, Partitions, and QoS](job-resources.md) page and in the [Interactive Jobs](interactive-jobs.md) page.
````
