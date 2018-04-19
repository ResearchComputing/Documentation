- [Overview](#overview)
- [Monitoring Disk Usage](#monitoring-disk-usage)
- [Backups](#backups)
- [Best Practices](#best-practices)
- [Sharing Directories](#sharing-directories)

## Overview

All users are allocated space on the `/home` and `/projects` file systems.  In addition, separate `scratch` directories are visible from Summit and Blanca.  These scratch directories are provided to high-performance and/or parallel I/O for jobs running on those two systems.  

Please  note that the use of `/home` or `/scratch` for high-performance I/O may negatively affect the environment for all users.  As a result, all compute jobs should write to the appropriate `scratch` file system.  **Users performing intensive I/O on the `/home` or `/projects` file systems will  have their jobs terminated and may have their accounts temporarily disabled.**

### The Home File System
Every user is allocated 2 GB of space on the `/home` file system in a subdirectory corresponding to their user name (e.g., `/home/janedoe`).  Home directories are [backed up frequently](#backups) and are intended for the use of their owner only; sharing the contents of home directories with other users is strongly discouraged.  Your `/home` directory is a good place to store source code, small compiled programs, and job scripts.  

### The Projects File System

Each user has access to a 250 GB of space in their subdirectory of `/projects` (e.g., `/projects/janedoe`).  As with the `/home` system, these directories are visible from all Research Computing nodes and are regularly backed up. The projects directory is intended to store software builds and smaller data sets.  Projects directories may be [shared with other RC users](#sharing-directories).  

### Scratch File Systems

Summit users are provided a subdirectory on `/scratch/summit`, the high-performance parallel scratch file system meant for I/O from jobs running on that system (e.g., `/scratch/summit/janedoe`).  By default, each user is limited to a quota of 10 TB worth of storage space and 20M files and directories. Email rc-help@colorado.edu if you need these limits increased.

Summit scratch should be used for all compute jobs running on Summit.  These high-performance scratch directories are **not backed up**, and are not appropriate for long-term storage.  Data may be purged at any time subject to overall system needs. Files are automatically removed 90 days after their initial creation.

Users requiring longer-term retention of their files should perform regular backups to their local machine if they have not purchased space on the [PetaLibrary](PetaLibrary).  Inappropriate use of Summit scratch, including attempts to circumvent the automatic file purge policy, may result in loss of access to Summit.

## Monitoring Disk Usage

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

## Sharing Directories

## Best Practices
- Ensure that your compute jobs perform output to your /scratch/summit or /rc_scratch (for Blanca) directories only.  Users whose jobs perform excessive I/O to /home or /projects may have their jobs killed and their accounts temporarily disabled.
- Store frequently used input data on /projects
- Don't forget to backup data written to /scratch.  Files older than 90 days are wiped daily!

