## Table of Contents

- [Overview](#overview)
- [The Home Filesystem](#the-home-filesystem)
- [The Projects Filesystem](#the-projects-filesystem)
- [Scratch Filesystems](#scratch-filesystems)
- [Monitoring Disk Usage](#monitoring-disk-usage)
- [Filesystem Backups](#filesystem-backups)
- [Workspace Sharing](#workspace-sharing)

## Overview

All users are allocated space on the `/home` and `/projects` filesystems.  In addition, separate `scratch` directories are visible from Summit and Blanca.  These scratch directories are hosted on separate, high-performance filesystems designed to support intensive, parallel I/O operations.  

Please  note that the use of `/home` or `/projects` for high-performance I/O may negatively affect the environment for all users.  As a result, all compute jobs should write to the appropriate `scratch` filesystem.  **Users performing intensive I/O on the `/home` or `/projects` filesystems will  have their jobs terminated and may have their accounts temporarily disabled.**

### The Home Filesystem
Every user is allocated 2 GB of space on the `/home` filesystem in a subdirectory corresponding to their user name (e.g., `/home/janedoe`).  Home directories are [backed up frequently](#filesystem-backups) and are intended for the use of their owner only; sharing the contents of home directories with other users is strongly discouraged.  Your `/home` directory is a good place to store source code, small compiled programs, and job scripts.  

### The Projects Filesystem

Each user has access to a 250 GB of space in their subdirectory of `/projects` (e.g., `/projects/janedoe`).  As with the `/home` system, these directories are visible from all Research Computing nodes and are regularly backed up. The projects directory is intended to store software builds and smaller data sets. 

### Scratch Filesystems

Summit users are provided a subdirectory on `/scratch/summit`, the high-performance parallel scratch filesystem meant for I/O from jobs running on that system (e.g., `/scratch/summit/janedoe`).  By default, each user is limited to a quota of 10 TB worth of storage space and 20M files and directories. Email rc-help@colorado.edu if you need these limits increased.  Blanca users should write to `/rc_scratch/janedoe` instead of `/scratch/summit`.

Scratch space should be used for all compute jobs run on Summit or Blanca.  These high-performance scratch directories are **not backed up**, and are not appropriate for long-term storage.  Data may be purged at any time subject to overall system needs. Files are automatically removed 90 days after their initial creation.

Users requiring longer-term retention of their files should perform regular backups to their local machine if they have not purchased space on the [PetaLibrary](PetaLibrary).  Inappropriate use of scratch storage, including attempts to circumvent the automatic file purge policy, may result in loss of access to Research Computing resources.

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
## Filesystem Backups

Regular backups are performed for all `/home` and `/projects` directories and at a range of cadences.  Low-cadence backups are retained for longer periods of time than high-cadence backups.  A summary of the backup schedule is provided in the table below.

| Filesystem        | Cadence           | Retention Period  |
| ------------- |------------:| -----:|
| `/home`       | 2 hr          |    25 hr |
| `/home`       | 1 d           |     8 d |
| `/home`       | 1 wk          |    29 d |
| `/projects`   | 6 hr          |    25 hr |
| `/projects`   | 1 d           |    8 d |
| `/projects`   | 1 wk          |   15 d |
| `/scratch`    | **no backups** | N/A |
| `/rc_scratch` | **no backups** | N/A |

If disaster strikes and you need access to a previous version of your `/home` or `/projects` directories, change to that directory and look through the .snapshot subdirectory.   You will see a subdirectory associated with each snapshot of your `/home` or `/projects` directory, named using the time-stamp associated with the snapshot.

## Workspace Sharing
All users have complete control over their personal directory permissions.   While we encourage you to share your `/projects` and `/scratch` directories with collaborators as appropriate, we strongly discourage sharing of your `/home` directory due to the limited space and potentially sensitive information stored there.   

Directories may be shared with all Research Computing users or with only a subset of our users.  In the latter case, a system administrator will need to add your chosen collaborators to your Linux group.  Please email rc-help@colorado.edu if you would like to add users to your Linux group.

In the example that follows, we make our `/projects` directory open to all users and then create subdirectories with select read/write permissions for all users and our chosen collaborators. 

First, we make our `/projects` directory world-readable:
```
[janedoe@shas0136 ~]$ chmod a+rx /projects/janedoe
```
Next, we create a subdirectory that is visible to all users and which is read-only:
```
[janedoe@shas0136 ~]$ cd /projects/janedoe
[janedoe@shas0136 ~]$ mkdir world_read
[janedoe@shas0136 ~]$ chmod a+rx world_read
```
For our collaborators, we may want a writeable directory in addition to a read-only directory:
```
[janedoe@shas0136 ~]$ cd /projects/janedoe
[janedoe@shas0136 ~]$ mkdir group_read
[janedoe@shas0136 ~]$ chmod g+rx group_read
[janedoe@shas0136 ~]$ mkdir group_read_write
[janedoe@shas0136 ~]$ chmod g+rwx group_read_write
```
A similar methodology will need to be followed for all subdirectories you wish to share.  If you make a mistake or change your mind, use the `-` symbol in lieu of `+` to remove privileges.  Note that the `x` is necessary if you want other users to be able to `cd` into your directory.

