## ZFS Snapshots

### Overview

Every ZFS-based PetaLibrary allocation has snapshots enabled by default.
ZFS snapshots are read-only representations of a ZFS filesystem at the
time the snapshot is taken. Many allocations still reside in BeeGFS where
snapshots are not available; we expect to complete migrations from BeeGFS
to ZFS by the end of 2021.

### How to access snapshots

Snapshots are accessible in the root of the filesystem. If, for example,
your allocation is located in `/pl/active/rcops`, your snapshots are
accessible in `/pl/active/rcops/.zfs/snapshot`. Note that the `.zfs` directory
is not visible to any utilities that list directory contents, so an 'ls'
of the `.zfs` directory will fail, although you can 'cd' to it.

Snapshots times are in UTC, which is not affected by daylight savings
time. To convert from UTC to MDT, subtract six hours, and to convert
from UTC to MST, subtract seven hours.

### How snapshots affect free space in your allocation

PetaLibrary allocation sizes are set with quotas, and snapshot use does
count against your quota. Removing a file from your filesystem will
only return free space to your filesystem if no snapshots reference the
file. Filesystem free space does not increase until a file on a filesystem
and all snapshots referencing said file are removed. Because snapshots
can cause confusion about how space is utilized within an allocation,
the default snapshot schedule discards snapshots that are more than one
week old.

### Default snapshot schedule

The default snapshot schedule is as follows:

 - take snapshots every 15 minutes, save most recent 9 snapshots (two
   hours worth)

 - take snapshots every hour, save most recent 25 snapshots (one day
   worth)

 - take snapshots every day, save more recent 8 snapshots (one week worth)

If you would like to set a custom snapshot schedule for your allocation,
please contact rc-help@colorado.edu. Note that the longer you retain
snapshots, the longer it will take to free up space by deleting files
from your allocation.

Couldn't find what you need? [Provide feedback on these docs!](https://forms.gle/bSQEeFrdvyeQWPtW9)
