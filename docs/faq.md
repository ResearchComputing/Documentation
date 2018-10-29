## Frequently Asked Questions

See our documentation [homepage](https://github.com/ResearchComputing/Research-Computing-User-Tutorials/wiki) for information about our most common topics.

1. [I have a new phone. How do I move my Duo onto it?](#i-have-a-new-phone-how-do-i-move-my-duo-onto-it) 
2. [How do I check how full my Summit directories are?](#how-do-i-check-how-full-my-summit-directories-are)  
3. [When will my job start?](#when-will-my-job-start)  
4. [How much memory did my job use?](#how-much-memory-did-my-job-use)  
5. [Where is my current fair share priority level at?](#where-is-my-current-fair-share-priority-level-at)  
6. [Why is my job pending with reason 'ReqNodeNotAvail'?](#why-is-my-job-pending-with-reason-reqnodenotavail)  
7. [Why do I get the following 'Invalid Partition' error when I submit my job?](#why-do-i-get-an-invalid-partition-error-when-i-try-to-submit-a-job):   
    `sbatch: error: Batch job submission failed: Invalid partition name specified.`
8. [How can I check what allocations I belong to?](#how-can-i-check-what-allocations-i-belong-to)
9. [Why do I get the following 'LMOD' error when I try to load slurm/summit?](#why-do-i-get-an-lmod-error-when-i-try-to-load-slurm):  
    `Lmod has detected the following error:  The following module(s) are unknown: "slurm/summit"`
10. [How do I install my own python library?](#how-do-i-install-my-own-python-library)  

### I have a new phone. How do I move my Duo onto it?

You can add a new device to your duo account by visiting <a href="https://duo.colorado.edu">https://duo.colorado.edu</a>. After a CU authorization page you will be directed to a Duo authentication page. From here, click "Menu": 

![](https://raw.githubusercontent.com/ResearchComputing/Documentation/master/FAQ/duo-management1edit.png)

...and then click "Add a new device.":

![](https://raw.githubusercontent.com/ResearchComputing/Documentation/master/FAQ/duo-management2edit.png)

Duo will then try to authenticate your account by push notification, text message, or phone number. Choose one of the authentication methods and follow the instructions provided by duo to add your device.

If you cannot authenticate your account, contact rc-help@colorado.edu for further assistance.

### How do I check how full my Summit directories are?

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

### When will my job start?

You can pull up information on your job's start time using the `squeue` command: 
```
squeue --user=your_rc-username --start
```
Note that Slurm's estimated start time can be a bit inaccurate. This is because Slurm calculates this estimation off the jobs that are currently running or queued in the system. Any job that is added in later with a higher priority may delay your job.

For more information on the `squeue` command, [take a look at our Useful Slurm Commands tutorial.](running-jobs/slurm-commands.html) Or visit the Slurm page on [squeue](https://slurm.schedmd.com/squeue.html)

### How much memory did my job use?

You can check how much memory your job used by using the `sacct` command. Simply replace `YYYY-MM-DD` with the date you ran the job:

```
sacct --starttime=YYYY-MM-DD --jobs=your_job-id --format=User,JobName,JobId,MaxRSS
```

If you'd like to monitor memory usage on jobs that are currently running, use the `sstat` command:

```
sstat --jobs=your_job-id --format=User,JobName,JobId,MaxRSS
```

For more information on `sstat` or `sacct` commands, [take a look at our Useful Slurm Commands tutorial.](running-jobs/slurm-commands.html) Or visit the Slurm reference pages on [sstat](https://slurm.schedmd.com/sstat.html) and [sacct](https://slurm.schedmd.com/sacct.html).

### Where is my current fair share priority level at?

You can check your current fair share priority level using the `sshare` command:
```
sshare -U -l
```
The `sshare` command will print out a table of information regarding your usage and priority on all allocations. The -U flag will specify the current user and the -l flag will print out more details in the table. The field we are looking for is the _LevelFS_. The LevelFS holds a number from 0 to infinity that describes the fair share of an association in relation to its other siblings in an account. Over serviced accounts will have a LevelFS that's between 0 and 1. Under serviced accounts will have a LevelFS that's greater than 1. Accounts that haven't run any jobs will have a LevelFS of infinity (inf).

For more information on fair share the `sshare` command, [take a look at Slurm's documentation on fair share](https://slurm.schedmd.com/fair_tree.html) Or [check out the Slurm reference page on sshare](https://slurm.schedmd.com/sshare.html)

### Why is my job pending with reason 'ReqNodeNotAvail'?

The 'ReqNodeNotAvail' message usually means that your node has been reserved for maintenance during the period you have requested within your job script. This message often occurs in the days leading up to our regularly scheduled maintenance, which is performed the first Wednesday of every month. So, for example, if you submit a job with a 72 hour wall clock request on the first Monday of the month, you will receive the 'ReqNodeNotAvail' error because the node is reserved for maintenance within that 72-hour window. You can confirm whether the requested node has a reservation by typing `scontrol show reservation` to list all active reservations. 

If you receive this message, the following solutions are available: 1) submit a shorter job that does not intersect the maintenance window; or 2) wait until after maintenance. 

### Why do I get an 'Invalid Partition' error when I try to submit a job?

This error usually means users do not have an allocation that would provide the service units (SUs) required to submit a job.  This can occur if a user has no valid allocation, specifies an invalid allocation, or specifies an invalid partition.  Think of SUs as "HPC currency": you need an allocation of SUs to use the system. Allocations are free. New CU users should automatically get added to a 'ucb-general' allocation upon account creation which will provide a modest allocation of SUs for running small jobs and testing/benchmarking codes. However, if this allocation expires and you do not have a new one you will see this error.  'ucb-general' allocations are intended for benchmarking and testing, and it is expected that users will move to a project allocation.  To request a Project and apply for a Project Allocation visit our [allocation site](https://www.colorado.edu/rc/userservices/allocations).

### How can I check what allocations I belong to?

You can check the allocations you belong to with the `sacctmgr` command. Simply type:
```bash
sacctmgr -p show associations user=$USER
```
...from a login or compile node. This will print out an assortment of information including allocations and QoS available to you. For more information on sacctmgr, [check out the Slurm's documentation](https://slurm.schedmd.com/sacctmgr.html)

### Why do I get an 'LMOD' error when I try to load Slurm?

Using the Summit module environment from login nodes requires typing `module load slurm/summit`. However, the slurm/summit module environment is already pre-loaded on Summit scompile and compute nodes. Therefore, if you are on a Summit 'scompile' node, in a Summit 'sinteractive' job, or submitting a job to a Summit compute node (via a job script) and you load 'slurm/summit' you will get the 'LMOD' error. This error can be disregarded, as no harm is done.  

### How do I install my own python library?

Research Computing provides commonly used Python libraries as modules. This guide covers installing a local Python library (pyDOE) which is not included in the Research Computing modules. One prerequisite assumption is that you are using the [new module system](compute/modules.html). That being said, this guide can be tweaked to be used on the older modules as well.

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
