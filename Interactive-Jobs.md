## Table of Contents
- [Overview](#overview)
- [Videos](#videos)
- [General Interactive Jobs](#general-interactive-jobs)
- [Interactive GUI Applications](#interactive-gui-applications)

## Overview

Interactive jobs are jobs that allow a user to interact with applications in our HPC environment in real time. With interactive jobs, applications such as Python or Matlab can be ran in an interactive environment. Summit supports X11 forwarding and can thus run GUI applications remotely.

## Videos

### General Interactive Jobs
[![General interactive jobs video](https://raw.githubusercontent.com/ResearchComputing/Research-Computing-User-Tutorials/master/Interactive-Jobs/Interactive-Jobs-Video.jpg)](https://www.youtube.com/watch?v=hpdYdBsPynQ)  

### Interactive GUI applications
[![Running GUI applications through interactive jobs video](https://raw.githubusercontent.com/ResearchComputing/Research-Computing-User-Tutorials/master/Interactive-Jobs/Gui-Applications-Video.jpg)](https://www.youtube.com/watch?v=vSYNKlEKg3Y) 

## General Interactive Jobs
To run an interactive job load the slurm module into the enviornment with:

```bash
module load slurm/summit
```

and request an interactive session by utilizing the `sinteractive` command. 
The `sinteractive` command can take any number of flags that could be used with the `sbatch` command when submitted to slurm but the primary flags we will use are the `qos` flag and the `time` flag. These flags will specify quality of service and amount of time the job will run for respectively. We can run the command like so:

```bash
sinteractive --qos=debug --time=00:10:00
``` 

This will load us into an interactive session that will run on one core of one node on the debug quality of service for 10 minutes. From here you can run any interactive terminal application you may need.

## Interactive GUI Applications

To run an interactive General User Interface application, we must enable X11 forwarding on our personal computer.
Once you've enabled X11 forwarding you will be able to run GUI applications through interactive jobs.

### Windows

On Windows we must first install an X window server application to allow Summit to forward the GUI information to our local system. For Windows, we will use an application called Xming to accomplish this. [Download the Xming here](https://sourceforge.net/projects/xming/).

Next we must enable X11 forwarding on the PuTTY application. Download and install the [PuTTY application](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) here if you have not done so already. 

Expand the SSH tab on the left side of the application and click X11.

![Putty-Image-1](https://raw.githubusercontent.com/ResearchComputing/Research-Computing-User-Tutorials/master/Interactive-Jobs/putty-1.png)

In the X11 Menu check the "Enable X11 Forwarding" checkbox and type "localhost:0" in the X display location field.
Clicking open will open a terminal window where you can login.

![Putty-Image-2](https://raw.githubusercontent.com/ResearchComputing/Research-Computing-User-Tutorials/master/Interactive-Jobs/putty-2.png)

### Mac

On Mac, we will also need to install an X window server application to allow Summit to forward GUI information to our local system. For Mac, we will use an application called XQuartz to accomplish this. [Download and install XQuartz here](https://www.xquartz.org/).

Opening the application will bring up a terminal window. On this window type:
```bash
ssh login.rc.colorado.edu -l your_rc-username -X
``` 
