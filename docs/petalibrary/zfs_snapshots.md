# Data Recovery

ZFS snapshots are read-only representations of a ZFS filesystem at the time the snapshot is taken. Snapshots enable users to recover data that they have unintentionally deleted, during a specified [retention period](#default-snapshot-schedule). Every PetaLibrary allocation has snapshots enabled by default. 

## How to access snapshots

Snapshots are accessible in the root of the filesystem. If, for example,
your allocation is located in `/pl/active/rcops`, your snapshots are
accessible in `/pl/active/rcops/.zfs/snapshot`. Snapshot times are in UTC, which is not affected by daylight savings time. To convert from UTC to MDT, subtract six hours. To convert from UTC to MST, subtract seven hours.

```{note}
The `.zfs` directory is not visible to any utilities that list directory contents, so an `ls` of the `.zfs` directory will fail, although you can `cd` to it.
```

## How to recover data from snapshots

The easiest way to demonstrate snapshot recovery is by example. Assume that on 2025-09-24 you deleted a file called `test.txt` , in the top level directory of your petalibrary allocation named `/pl/active/rcops`. Now, on 2025-09-30 you realize that you need to recover the file!   

::::{dropdown} Show steps for snapshot recovery 
:icon: note

### Step 1: choose the snapshot from which you want to recover

```
$ ls /pl/active/rcops/.zfs/snapshot
autosnap_2025-09-23_00:00:17_daily   autosnap_2025-09-30_03:00:12_hourly  autosnap_2025-09-30_18:00:15_hourly
autosnap_2025-09-24_00:00:34_daily   autosnap_2025-09-30_04:00:25_hourly  autosnap_2025-09-30_18:30:04_frequently
autosnap_2025-09-25_00:02:50_daily   autosnap_2025-09-30_05:00:07_hourly  autosnap_2025-09-30_18:45:04_frequently
autosnap_2025-09-26_00:00:07_daily   autosnap_2025-09-30_06:00:30_hourly  autosnap_2025-09-30_19:00:10_frequently
autosnap_2025-09-27_00:00:01_daily   autosnap_2025-09-30_07:00:13_hourly  autosnap_2025-09-30_19:00:10_hourly
autosnap_2025-09-28_00:00:22_daily   autosnap_2025-09-30_08:00:21_hourly  autosnap_2025-09-30_19:15:02_frequently
autosnap_2025-09-29_00:00:08_daily   autosnap_2025-09-30_09:00:14_hourly  autosnap_2025-09-30_19:30:04_frequently
autosnap_2025-09-29_20:00:23_hourly  autosnap_2025-09-30_10:00:18_hourly  autosnap_2025-09-30_19:45:10_frequently
autosnap_2025-09-29_21:00:33_hourly  autosnap_2025-09-30_11:00:23_hourly  autosnap_2025-09-30_20:00:07_frequently
autosnap_2025-09-29_22:00:18_hourly  autosnap_2025-09-30_12:00:20_hourly  autosnap_2025-09-30_20:00:07_hourly
autosnap_2025-09-29_23:00:18_hourly  autosnap_2025-09-30_13:00:18_hourly  autosnap_2025-09-30_20:15:03_frequently
autosnap_2025-09-30_00:00:39_daily   autosnap_2025-09-30_14:00:01_hourly  autosnap_2025-09-30_20:30:12_frequently
autosnap_2025-09-30_00:00:39_hourly  autosnap_2025-09-30_15:00:07_hourly  autosnap_2025-09-30_20:45:09_frequently
autosnap_2025-09-30_01:00:12_hourly  autosnap_2025-09-30_16:00:06_hourly
autosnap_2025-09-30_02:00:33_hourly  autosnap_2025-09-30_17:00:24_hourly
```

From the above, you note that there is a snapshot from 2025-09-23 that would likely contain the deleted file.  

### Step 2: Confirm the deleted file is available in the snapshot

Look in the top level of the snapshot directory, which is analagous to the top level of your PetaLibrary allocation: 
```
$ ls -l /pl/active/rcops/.zfs/snapshot/autosnap_2025-09-23_00:00:17_daily/test.txt
-rw-r--r--. 1 janedoe rcopspgrp 597 Sep 20  2024 /pl/active/rcops/.zfs/snapshot/autosnap_2025-09-23_00:00:17_daily/test.txt
```

Good news, the file exists!  Now let's recover it...

### Step 3: Copy the file back to your PetaLibrary allocation

Use the linux `cp` command:

```
$ cp /pl/active/rcops/.zfs/snapshot/autosnap_2025-09-23_00:00:17_daily/test.txt /pl/active/rcops/
```

...and confirm the copy was successful:

```
$ ls -l /pl/active/rcops/test.txt
-rw-r--r--. 1 janedoe rcopspgrp 597 Sep 30 15:03 /pl/active/rcops/test.txt
```

You have successfully recovered your file from snapshots. 

::::

## How snapshots affect free space in your allocation

PetaLibrary allocation sizes are set with quotas, and snapshot use does
count against your quota. Removing a file from your filesystem will
only return free space to your filesystem if no snapshots reference the
file. Filesystem free space does not increase until a file on a filesystem
and all snapshots referencing said file are removed. Because snapshots
can cause confusion about how space is utilized within an allocation,
the default snapshot schedule discards snapshots that are more than one
week old.

## Default snapshot schedule

The default snapshot schedule is 1 week, at the following time frequencies:

 - take snapshots every 15 minutes, save most recent 9 snapshots (two
   hours worth)

 - take snapshots every hour, save most recent 25 snapshots (one day
   worth)

 - take snapshots every day, save more recent 8 snapshots (one week worth)

If you would like to set a custom snapshot schedule for your allocation,
please contact <rc-help@colorado.edu>. 

```{warning}
The longer you retain snapshots, the longer it will take to free up space by deleting files from your allocation.
```

