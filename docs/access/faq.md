# Frequently Asked Questions

See our [Getting Started](./getting_started.md) page for information on core areas of our documentation each user should become familiar with.

1. [I have a new phone. How do I move my Duo onto it?](#i-have-a-new-phone-how-do-i-move-my-duo-onto-it) 
2. [How do I acknowledge use of CURC Resources?](../index.md#acknowledging-rc)
3. [How do I check how full my directories are?](#how-do-i-check-how-full-my-directories-are)  
4. [When will my job start?](#when-will-my-job-start) 
5. [How can I get metics about CURC systems such as how busy they are, wait times, and account usage?](#how-can-i-get-metics-about-curc-systems-such-as-how-busy-they-are-wait-times-and-account-usage) 
6. [How much memory did my job use?](#how-much-memory-did-my-job-use)  
7. [How can I see my current FairShare priority?](#how-can-i-see-my-current-fairshare-priority)  
8. [Why is my job pending with reason `ReqNodeNotAvail`?](#why-is-my-job-pending-with-reason-reqnodenotavail)  
9. [Why do I get an `Invalid Partition` error when I try to run a job on Alpine?](#why-do-i-get-an-invalid-partition-error-when-i-try-to-run-a-job-on-alpine)   
10. [Why do I get an `Invalid Partition` error when I try to run a job on Blanca?](#why-do-i-get-an-invalid-partition-error-when-i-try-to-run-a-job-on-blanca) 
11. [How can I check what allocations I belong to?](#how-can-i-check-what-allocations-i-belong-to)
12. [Why do I get an `LMOD` error when I try to load Slurm?](#why-do-i-get-an-lmod-error-when-i-try-to-load-slurm)
13. [How do I install Python libraries?](#how-do-i-install-python-libraries)  
14. [Why does my PetaLibrary allocation report less storage than I requested?](#why-does-my-allocation-report-less-storage-than-i-requested)
15. [Why is my Jupyter session throwing a `QOSMaxSubmitJobPerUserLimit` error?](#why-is-my-jupyter-session-throwing-a-qosmaxsubmitjobperuserlimit-error)

## I have a new phone. How do I move my Duo onto it?
````{toggle} 

You can add a new device to your duo account by visiting <a href="https://duo.colorado.edu">https://duo.colorado.edu</a>.
After a CU authorization page you will be directed to a Duo authentication page. **Ignore the Duo Push prompt and instead click "Add a new device":** 

![](faq_images/duo_new_device1.png)

Duo will then try to authenticate your account by push notification to verify your identity. Cancel this push notification...  

![](faq_images/duo_new_device2.png)

...and click on "Enter a Passcode", or "Call Me". 
- If you select "Call Me" the simply receive the call and press 1. 
- If you select "Enter a Passcode" then click "Text me new codes" and you will be sent a list of one time passwords. Type in any one of the codes and you will be authenticated. 

Once you have verified your identity, follow the instructions provided by Duo to add your device.

If you cannot authenticate your account (e.g. do not have your old device), contact <rc-help@colorado.edu> for further assistance.

````

## How do I check how full my directories are?

````{toggle} 

You have three directories allocated to your username (`$USER`). These include `/home/$USER` (2 G), `/projects/$USER` (250 G) and `/scratch/alpine/$USER` (10 T).  To see how much space you've used in each, from a login node, type `curc-quota` as follows:

```
[janedoe@login11 ~]$ curc-quota
------------------------------------------------------------------------
									Used         Avail    Quota Limit
------------------------------------------------------------------------
/home/janedoe                          1.7G          339M           2.0G
/projects/janedoe                       67G          184G           250G
/scratch/alpine1                      1050G         8950G         10000G
```

You can also check the amount of space being used by any directory with the `du -sh` command or the directory's contents with the `du -h` command: 

```
[janedoe@c3cpu-a7-u26-3 ~]$ du -h /scratch/alpine/janedoe/WRF
698M	WRF/run
698M	WRF
```

````

## When will my job start?

````{toggle} 

You can pull up information on your job's start time using the `squeue` command: 
```
squeue --user=your_rc-username --start
```
Note that Slurm's estimated start time can be a bit inaccurate. This is because Slurm calculates this estimation off the jobs that are currently running or queued in the system. Any job that is added in later with a higher priority may delay your job.

For more information on the `squeue` command, [take a look at our Useful Slurm Commands tutorial.](../running-jobs/slurm-commands.md) Or visit the Slurm page on [squeue](https://slurm.schedmd.com/squeue.html)

Note that you can also see system level wait times and how they change through time by visiting the [CURC metrics portal](../compute/monitoring-resources.md) at [https://xdmod.rc.colorado.edu](https://xdmod.rc.colorado.edu)

````

## How can I get metics about CURC systems such as how busy they are, wait times, and account usage?

````{toggle} 

Please refer to our [XDMoD](../compute/monitoring-resources.md#xdmod) documentation, which is a portal that allows users to easily see CURC system metrics. 
````

## How much memory did my job use?

````{toggle} 

You can check how much memory your job utilized by using the `sacct` command and refering to the `MaxRSS` metric. This is done as follows where you can replace `YYYY-MM-DD` with the date you ran the job and specify your JobID:

```
sacct --starttime=YYYY-MM-DD --jobs=your_job_id --format=User,JobName,JobId,MaxRSS
```

If you'd like to monitor memory usage on jobs that are currently running, use the `sstat` command:

```
sstat --jobs=your_job_id --format=User,JobName,JobId,MaxRSS
```

For more information on `sstat` or `sacct` commands, [take a look at our Useful Slurm Commands tutorial.](../running-jobs/slurm-commands.md) Or visit the Slurm reference pages on [sstat](https://slurm.schedmd.com/sstat.html) and [sacct](https://slurm.schedmd.com/sacct.html). 

You can also view information related to service unit (SU) usage and CPU & RAM efficiency by using [slurmtools](../compute/monitoring-resources.md#slurmtools). Note that CPU & RAM efficiency statistics will be included in emails sent when a job completes, if requested. 

````

## How can I see my current FairShare priority?

````{toggle} 

There are a couple ways you can check your FairShare priority:

1. Using the `levelfs` tool in the `slurmtools` module. `levelfs` shows the current fair share priority of a specified user.
	
	You can use this tool by first loading in the `slurmtools` module (available from login nodes):
	```
	$ module load slurmtools
	```

	```{tip}
	slurmtools is packed with lots of great features and tools like suacct, suuser, jobstats, seff, etc._
	```

	Then using `levelfs` on your username:
	```
	$ levelfs $USER
	```
	* A value of 1 indicates average priority compared to other users in an account.
	* A value of < 1 indicates lower than average priority (longer than average queue waits) 
	* A value of > 1 indicates higher than average priority (shorter than average queue waits)
<br/><br/>
2. Using the `sshare` command:
	```
	sshare -U -l
	```
	The `sshare` command will print out a table of information regarding your usage and priority on all allocations. The `-U` flag will specify the current user and the `-l` flag will print out more details in the table. The field we are looking for is the _LevelFS_. The LevelFS holds a number from 0 to infinity that describes the fair share of an association in relation to its other siblings in an account. Over-serviced accounts will have a LevelFS between 0 and 1. Under-serviced accounts will have a LevelFS greater than 1. Accounts that haven't run any jobs will have a LevelFS of infinity (inf).

	For more information on fair share the `sshare` command, [take a look at Slurm's documentation on fair share](https://slurm.schedmd.com/fair_tree.html) Or [check out the Slurm reference page on sshare](https://slurm.schedmd.com/sshare.html)

````

## Why is my job pending with reason `ReqNodeNotAvail`?

````{toggle} 

The `ReqNodeNotAvail` message usually means that your node has been reserved for maintenance during the period you have requested within your job script. This message often occurs in the days leading up to our regularly scheduled maintenance, which is performed the first Wednesday of every month. So, for example, if you run a job with a 72 hour wall clock request on the first Monday of the month, you will receive the `ReqNodeNotAvail` error because the node is reserved for maintenance within that 72-hour window. You can confirm whether the requested node has a reservation by typing `scontrol show reservation` to list all active reservations. 

If you receive this message, the following solutions are available: 
1. Run a shorter job or modify your current job's time so that it does not intersect with the maintenance window. One can modify your current job's time by using the `scontrol` command:

	```bash
	$ scontrol update jobid=<jobid> time=<time>
	```
2. Wait until after maintenance window has finished. Once maintenance has completed, your job will resume automatically.
````

## Why do I get an `Invalid Partition` error when I try to run a job on Alpine?

````{toggle}

This error usually means users do not have an allocation that would provide the service units (SUs) required to run a job.  This can occur if a user has no valid allocation, specifies an invalid allocation, or specifies an invalid partition.  Think of SUs as "HPC currency": you need an allocation of SUs to use the system. Allocations are free. New CU users should automatically get added to a `ucb-general` allocation upon account creation which will provide a modest allocation of SUs for running small jobs and testing/benchmarking codes. However, if this allocation expires and you do not have a new one you will see this error.  `ucb-general` allocations are intended for benchmarking and testing and it is expected that users will move to a project allocation.  To request a Project and apply for a Project Allocation visit our [allocation documentation](../clusters/alpine/allocations.md).

````

## Why do I get an `Invalid Partition` error when I try to run a job on Blanca?

````{toggle} 

If you are getting an `Invalid Partition` error on a Blanca job which you know you have access to or have had access to before, you may have the `slurm/alpine` module loaded. From a login node, run `module load slurm/blanca` to access the Slurm job scheduler instance for Blanca, then try to resubmit your job.

````

## How can I check what allocations I belong to?

````{toggle} 

You can check the allocations you belong to with the `sacctmgr` command. This can be done by typing the following from a login or compute node:
```bash
sacctmgr -p show associations user=$USER
```
This will print out an assortment of information including allocations and QoS available to you. For more information on sacctmgr, please refer to [Slurm's documentation](https://slurm.schedmd.com/sacctmgr.html). 

````

## Why do I get an `LMOD` error when I try to load Slurm?

````{toggle} 

The `slurm/alpine` and `slurm/blanca` module environments cannot be loaded from compute nodes. It should only be loaded from login nodes when attempting to switch between Blanca and Alpine environments. This error can be disregarded, as no harm is done.

````

## How do I install Python libraries?

````{toggle} 

For individuals that need to install Python libraries not included in our base Python or Anaconda modules, we recommend using Conda environments through the Anaconda module. Instructions for creating a custom Conda environment can be found on our [Python and R with Anaconda](../software/python.md) documentation page. 

````

## Why does my allocation report less storage than I requested?

````{toggle} 

Every ZFS-based PetaLibrary allocation has snapshots enabled by default. ZFS snapshots are read-only representations of a ZFS filesystem at the time the snapshot is taken. For more information on ZFS Snapshots, please refer to our [ZFS Snapshots](../storage/petalibrary/zfs_snapshots.md) documentation. 

PetaLibrary allocation sizes are set with quotas, and ZFS snapshot use does count against your quota. Removing a file from your filesystem will only return free space to your filesystem if no snapshots reference the file. Filesystem free space does not increase until a file on a filesystem and all snapshots referencing said file are removed. Because snapshots can cause confusion about how space is utilized within an allocation, the default snapshot schedule discards snapshots that are more than one week old.

If you would like to set a custom snapshot schedule for your allocation, please contact <rc-help@colorado.edu>. Note that the longer you retain snapshots, the longer it will take to free up space by deleting files from your allocation.

````

## Why is my Jupyter session throwing a `QOSMaxSubmitJobPerUserLimit` error?

````{toggle} 

Some of our Open OnDemand applications allocate resources, which can be limited to one session. All Open OnDemand applications that submit jobs to Alpine's `ahub` partition have this limitation. Currently, all applications utilizing the presets configurations will be submitted to the `ahub` partition. This partition provides users with rapid start times, but limits users to one Jupyter session (or any one job using the partition). In order to spawn another Jupyter session, you first need to close the current job. You can do so by shutting down your current Jupyter session or by [canceling your job manually](../running-jobs/slurm-commands.md#stopping-jobs-with-scancel). 

````