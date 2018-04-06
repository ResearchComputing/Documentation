## Frequently Asked Questions:

1. [I have a new phone. How do I move my Duo onto it?](#i-have-a-new-phone-how-do-i-move-my-duo-onto-it) 
2. [How do I check how full my Summit directories are?](#how-do-i-check-how-full-my-summit-directories-are)  
3. [When will my job start?](#when-will-my-job-start)  
4. [How much memory did my job use?](#how-much-memory-did-my-job-use)  
5. [Where is my current fair share priority level at?](#where-is-my-current-fair-share-priority-level-at)  
6. [Why is my job pending with reason 'ReqNodeNotAvail'?](#why-is-my-job-pending-with-reason-reqnodenotavail)  
7. [Why do I get the following 'Invalid Partition' error when I submit my job?](#why-do-i-get-an-invalid-partition-error-when-i-try-to-submit-a-job):   
    `sbatch: error: Batch job submission failed: Invalid partition name specified.`
8. [Why do I get the following 'LMOD' error when I try to load slurm/summit?](#why-do-i-get-an-lmod-error-when-i-try-to-load-slurm):  
    `Lmod has detected the following error:  The following module(s) are unknown: "slurm/summit"`
9. [How do I install my own python library?](#how-do-i-install-my-own-python-library)  

## I have a new phone. How do I move my Duo onto it?

Visit <a href="https://duo.colorado.edu">https://duo.colorado.edu</a> and add your new device via the 'manage devices' link. 

## How do I check how full my Summit directories are?

You have three directories allocated to your username ($USER).  These include `/home/$USER` (2 G), `/projects/$USER` (250 G) and `/scratch/summit/$USER` (10 T).  To see how much space you've used in each, from a Summit 'scompile' node, type `curc-quota` as follows:

```
[janedoe@shas0136 ~]$ curc-quota
------------------------------------------------------------------------
                                       Used         Avail    Quota Limit
------------------------------------------------------------------------
/home/janedoe                          1.7G          339M           2.0G
/projects/janedoe                       67G          184G           250G
/scratch/summit                         29G        10211G         10240G
```

You can also check the amount of space being used by any directory with the `du -h` command: 

```
[janedoe@shas0136 ~]$ du -h /scratch/summit/janedoe/WRF
698M	WRF/run
698M	WRF
```

## When will my job start?

You can pull up your job's start time using the command: 
```
squeue --user=your_rc-username --start
```
Note that this start time can vary substantially because Slurm calculates this time based off of what jobs are currently in the system. Any job that is added in later with a higher priority may delay your job.

For detailed information on the squeue command, [take a look at our Job Tools tutorial](Job Tools)

## How much memory did my job use?
You can check how much memory your job used by using 

```
sacct --format=MaxRSS
```

## Where is my current fair share priority level at?

## Why is my job pending with reason 'ReqNodeNotAvail'?

The 'ReqNodeNotAvail' message usually means that your node has been reserved for maintenance during the period you have requested within your job script.  This message often occurs in the days leading up to our regularly scheduled maintenance, which is performed the first Wednesday of every month. So, for example, if you submit a job with a 72 hour wall clock request on the first Monday of the month, you will receive the 'ReqNodeNotAvail' error because the node is reserved for maintenance within that 72-hour window. You can confirm whether the requested node has a reservation by typing `scontrol show reservation` to list all active reservations. 

If you receive this message, the following solutions are available: 1) submit a shorter job that does not intersect the maintenance window; or 2) wait until after maintenance. 

## Why do I get an 'Invalid Partition' error when I try to submit a job?

The 'Invalid Partition' error is common among new account holders.  It usually means users have not requested an Allocation that would provide the service units (SUs) required to submit a job.  Think of SUs as "HPC currency": you need an allocation of SUs to use the system.  Allocations are free. New CU users can request a 'ucb-general' allocation (by emailing rc-help@colorado.edu) which will provide a modest allocation of SUs for running small jobs and testing/benchmarking codes.  Users requiring more resources can <a href="https://www.rc.colorado.edu/support/user-guide/allocations.html">request a Project and apply for a Project Allocation</a>.

## Why do I get an 'LMOD' error when I try to load Slurm?

Using the Summit module environment from login nodes requires typing `module load slurm/summit`. However, the slurm/summit module environment is already pre-loaded on Summit scompile and compute nodes. Therefore, if you are on a Summit 'scompile' node, in a Summit 'sinteractive' job, or submitting a job to a Summit compute node (via a job script) and you load 'slurm/summit' you will get the 'LMOD' error. This error can be disregarded, as no harm is done.  

## How do I install my own python library?

Research Computing provides commonly used Python libraries as modules. This guide covers installing a local Python library (pyDOE) which is not included in the Research Computing modules. One prerequisite assumption is that you are using the <a href="https://www.rc.colorado.edu/support/user-guide/modules.html">new module system</a>. That being said, this guide can be tweaked to be used on the older modules as well.

First login to a login node and then ssh to a compile node.

```
@login01$ ssh scompile
```

Next load the version of Python you'd like to add a library too. For this guide we'll be using Intel and Python 2.7.11.

```
@scompile1 ~]$ ml intel/17.4
@scompile1 ~]$ ml python/2.7.11
```

Before installing, create a directory in which to keep your local Python libraries. It is recommended that the /projects directory be used as it has more space.

```
@scompile1 ~]$ mkdir /projects/$USER/python_libs
```

You can now install your local python library.

```
@scompile1 ~]$ pip install --prefix="/projects/$USER/python_libs" pyDOE
```

In order to use your newly installed library it needs to be added to your PYTHONPATH. Use the following export command:

```
@scompile1 ~]$ export PYTHONPATH=$PYTHONPATH:/projects/$USER/python_libs/lib/python2.7/site-packages/
```

You can quickly check if your install worked with the following:

```
@scompile1 ~]$ python -c "import pyDOE"
```

Every time you log out you will need to rerun the above export to use your Python library (don't forget to load Python as well). Two ways of avoiding this are to add the export command to your bashrc. `vim ~/.bashrc`. An alternative is to make your own modulefile.

One final item of note is a Python virtualenv. Virtualenvs allow you to keep multiple Python environments with separate versions of packages. There are plenty of guides available online such as this one: [http://docs.python-guide.org/en/latest/dev/virtualenvs/](http://docs.python-guide.org/en/latest/dev/virtualenvs/). These are especially handy if you have several projects which require different versions of the same Python library.