- [File Systems Overview](#file-systems-overview)
- [Best Practices](#best-practices)
- [Accounting](#accounting)
- [Backups](#backups)

## File Systems Overview

All users are allocated space on the `home` and `projects` file systems.  Additionally, separate `scratch` file systems are visible from Summit and Blanca and are made available to users of those systems.  The scratch directories are provided to support high-performance I/O on Summit and Blanca.  Use of non-scratch directories during a high-performance or parallel compute jobs may negatively affect the environment for all users.  **Running compute jobs that involve intensive I/O on the `/home` or `/projects` file systems will result in termination of the job and may result in restricted access to Research Computing resources.**

 A summary of the capacity and intended purpose of each file system is provided below.  

### The Home File System
Every user is allocated 2 GB of space on the `home` filesystem in a subdirectory corresponding to their user name (e.g., `/home/janedoe`).  Home directories are not stored on a high-performance file-system and, as such, they are not intended to be written to by compute jobs. 

A hidden .snapshot/ directory is available in each home directory (and in each subdirectory) and contains recent copies of the files at 2-hour, daily, and weekly intervals. These snapshots can be used to recover files after accidental deletion or corruption.

Home directories are intended for the use of their owner only; sharing the contents of home directories with other users is strongly discouraged. 

### The Projects File System

All users are allocated 250 GB of space on the scratch file system.  
You have three directories allocated to your username ($USER).  These include `/home/$USER` (2 G), `/projects/$USER` (250 G) and `/scratch/summit/$USER` (10 T).  

## Accounting

Disk usage may be checked using the `curc-quota` command.  When run from a Summit `compile node`, you will see output similar to:

```
[janedoe@shas0136 ~]$ curc-quota
------------------------------------------------------------------------
                                       Used         Avail    Quota Limit
------------------------------------------------------------------------
/home/janedoe                          1.7G          339M           2.0G
/projects/janedoe                       67G          184G           250G
/scratch/summit                         29G        10211G         10240G
```
If the command is run from a `login node`, information concerning /scratch/summit will be omitted.

Note that the space occupied by a particular directory and its subdirectories can be obtained via the `du -h` command: 

```
[janedoe@shas0136 ~]$ du -h /scratch/summit/janedoe/WRF
698M	WRF/run
698M	WRF
```
## Backups

Text

## Best Practices
- Ensure that your compute jobs perform output to your /scratch/summit or /rc_scratch (for Blanca) directories only.  Users whose jobs perform excessive I/O to /home or /projects may have their jobs killed and their accounts temporarily disabled.
- Store frequently used input data on /projects
- Don't forget to backup data written to /scratch.  Files older than 90 days are wiped daily!

