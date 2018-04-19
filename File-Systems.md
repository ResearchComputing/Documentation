- [Overview](#overview)
- [Best Practices](#best-practices)
- [Accounting](#accounting)

## Overview

You have three directories allocated to your username ($USER).  These include `/home/$USER` (2 G), `/projects/$USER` (250 G) and `/scratch/summit/$USER` (10 T).  

## Accounting

To see how much space you've used in each directory, from a Summit *scompile* node, run the `curc-quota` command:

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

## Best Practices
- Ensure that your compute jobs perform output to your /scratch/summit or /rc_scratch (for Blanca) directories only.  Users whose jobs perform excessive I/O to /home or /projects may have their jobs killed and their accounts temporarily disabled.
- Store frequently used input data on /projects
- Don't forget to backup data written to /scratch.  Files older than 90 days are wiped daily!

