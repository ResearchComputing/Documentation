## Running applications with Jobs

Because Summit is a shared resource between a variety of researchers, Research Computing manages usage of the system through jobs. **Jobs** are simply an allotment of resources that can be used to execute processes. Research Computing utilizes the *Simple Linux Utility for Resource Management* or **Slurm** to create and manage jobs.

In order to run a program on Summit, you must request resources from Slurm to generate a job. Resources can be requested from a login node or a compile node. You must then provide commands to run your program on those requested resources. Where you provide you commands depends on whether you are running a [batch job]() or an [interactive job]().

Regardless on if you wish to run a batch job or an interactive job, your job will be placed into a job queue where your job will be held until its priority has been reached and resources are available to schedule your job. [A detailed guide on Slurm's queue and accounting tools can be found here.]()

### Batch Jobs

The primary method of running applications on Research Computing resources is through a batch job. A **batch job** is a job that runs on a compute node with little to no interaction from the users end. You should use batch jobs for:

- Any computationally expensive application that could take hours or days to run
- Any application that requires little or no user input
- Applications that you do not need to monitor extensively

Unlike running an application on your personal machine, you do not call the application you wish to run directly. Instead you must create a **job script** that includes a call to your application. Job scripts are simply a set of resource requests and commands. When a job script is submitted all the commands detailed in the job script are executed on a compute node. 

You must then run the `sbatch` command followed by your job script:

```bash
sbatch <your-jobscript>
```

If no job script is provided then `sbatch` will take whatever commands follow as standard input.

A detailed guide [on constructing and submitting Job scripts can be found here.]()

### Interactive Jobs

Another method of running applications on Research Computing resources is through an interactive job. As the name would imply, an **interactive job** is a job that allows users to interact with requested resources in real time. Users can run applications, execute scripts, or run other commands directly on a compute node. Interactive jobs should be used for:

- Debugging applications or workflows
- Any application that require user input
- Any applications with a GUI (Graphical User Interface)

You can request an interactive job by utilizing the `sinteractive`command. Unlike the `sbatch`, resources must be requested via the command line through the use of flags. Though running sinteractive without any flags is possible, this will result in default values being used for you jobs. Research Computing highly recommends you provide a `qos` and a `time` parameter to avoid long queue times or accidental overuse of your priority. 

```bash
sinteractive --qos=interactive --time=00:10:00
```

[A list of sinteractive parameters can be found here]()

This will load an interactive session that will run on one core of one node on the interactive quality of service for ten minutes. From here you can run any interactive terminal application you may need. 

More details [on running Interactive Jobs can be found here.]()
