- [Overview](#overview)
- [Best Practices](#best-practices)
- [Accounting](#accounting)

## Overview

All Research-Computing users are allocated space on the `home` and `projects` file systems.  Additionally, separate `scratch` file systems are visible from Summit and Blanca and are made available to users of those systems.

# The Home File System
Every user is allocated 2G
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

## Best Practices
- Ensure that your compute jobs perform output to your /scratch/summit or /rc_scratch (for Blanca) directories only.  Users whose jobs perform excessive I/O to /home or /projects may have their jobs killed and their accounts temporarily disabled.
- Store frequently used input data on /projects
- Don't forget to backup data written to /scratch.  Files older than 90 days are wiped daily!

