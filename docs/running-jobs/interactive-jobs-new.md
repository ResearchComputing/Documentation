## Interactive jobs

Interactive jobs allow a user to interact with applications in real time within an HPC environment. With interactive jobs, users request time and resources to work on a compute node directly. Users can then run graphical user interface (GUI) applications, execute scripts, or run other commands directly on a compute node.  Common reasons for running interactive jobs include debugging, designing workflows, or preference in using the GUI interface of an application.

### General Interactive Jobs

<iframe width="560" height="315" src="https://www.youtube.com/embed/s53sjDubBpo" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

---

To run an interactive job on Research Computing resources, request an interactive session by utilizing the `sinteractive` command.  The `sinteractive` command creates a job with parameters provided through flags run with the command. After moving through the Slurm queue the interactive job will put the user onto the command line of a compute node to interactively use their resource allotment. 

Any resource that could be specified in a job script or with `sbatch` can also be used with `sinteractive`. The primary flags we recommend users specify are the `qos` flag and the `time` flag. These flags will specify quality of service and amount of time for your job respectively. The `sinteractive` command is run as follows:

```bash
sinteractive --qos=interactive --time=00:10:00
```

This will submit an interactive job to the Slurm queue that will start a terminal session that will run on one core of one node with the interactive quality of service for ten minutes. Once the session has started you can run any application or script you may need from the command line.  For example, if you type `python` you will open an interactive python shell on a compute node (rather than the login nodes, which is forbidden). 

### Interactive GUI Applications

<iframe width="560" height="315" src="https://www.youtube.com/embed/DFnHsMxPC5w" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

---

To run an interactive GUI application on Summit, we must install an X windows server application and enable X11 forwarding on our personal computer.

#### Windows setup

On Windows we must first install an X windows server application to allow Summit to forward the GUI information to your local system. For Windows, we will use an application called Xming to accomplish
this. [Download the Xming here](https://sourceforge.net/projects/xming/).

Next we must enable X11 forwarding on the PuTTY application. Download and install the [PuTTY application](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) here if you have not done so already.

![Putty-Image-1](https://raw.githubusercontent.com/ResearchComputing/Research-Computing-User-Tutorials/master/Interactive-Jobs/putty-1.png)

Expand the SSH tab on the left side of the application and click X11.

![Putty-Image-2](https://raw.githubusercontent.com/ResearchComputing/Research-Computing-User-Tutorials/master/Interactive-Jobs/putty-2.png)

In the X11 Menu check the "Enable X11 Forwarding" checkbox and type "localhost:0" in the X display location field.  Clicking open will open a terminal window where you can login.

#### macOS setup

Using macOS, we will also need to install an X windows server application to allow Summit to forward GUI information to your local system. For Mac, we will use an application called XQuartz to accomplish this. [Download and install XQuartz here](https://www.xquartz.org/).

Opening the application will bring up a terminal window. In this window, you will ssh to login.rc.colorado.edu as you normally would except you'll include the "-X" flag:

```bash
ssh -X your_rc-username@login.rc.colorado.edu
```

#### Running GUI Applications

Once you have logged into Summit with X11 Forwarding enabled, you will be able to initialize a GUI application by starting an interactive job and running your selected application. The X-window server application installed on your local system will display the window generated on the cluster on your local machine.

If you plan on submitting your interactive job from a compile node, you must also enable x11 forwarding when you ssh into scompile:

```bash
ssh -X scompile
```

From here you will be able to submit your interactive job like normal and x11 forwarding will carry through to the job. 



