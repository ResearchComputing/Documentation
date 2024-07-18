# Filesystems

<iframe width="560" height="315" src="https://www.youtube.com/embed/xfeRDnZQrJ4" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

All users are allocated space on the `/home` and `/projects`
filesystems. In addition, separate `scratch` directories are visible
from Alpine and Blanca. These scratch directories are hosted on
separate, high-performance filesystems designed to support intensive,
parallel I/O operations.

Please note that the use of `/home` or `/projects` for
high-performance I/O may negatively affect the environment for all
users. As a result, all compute jobs should write to the appropriate
`scratch` filesystem. **Users performing intensive I/O on the `/home`
or `/projects` filesystems will have their jobs terminated and may
have their accounts temporarily disabled.**


## The Home Filesystem

Every user is allocated 2 GB of space on the `/home` filesystem in a
subdirectory corresponding to their user name (e.g., `/home/janedoe`).
Home directories are [backed up frequently](#backups) and
are intended for the use of their owner only; sharing the contents of
home directories with other users is strongly discouraged. Your
`/home` directory is a good place to store source code, small compiled
programs, and job scripts.


## The Projects Filesystem

Each user has access to a 250 GB of space in their subdirectory of
`/projects` (e.g., `/projects/janedoe`). As with the `/home` system,
these directories are visible from all Research Computing nodes and
are regularly backed up. The projects directory is intended to store
software builds and smaller data sets.


## Scratch Filesystems

Alpine users are provided a subdirectory on `/scratch/alpine`, the
high-performance parallel scratch filesystem meant for I/O from jobs
running on that system (e.g., `/scratch/alpine/janedoe`). By default,
each user is limited to a quota of 10 TB worth of storage space and
20M files and directories. If you need these limits increased, see our [Scratch Quota Increases policy](../additional-resources/policies.md#alpine-scratch-quota-increases). Blanca users should write to
`/rc_scratch/janedoe` instead of `/scratch/alpine`.

Scratch space should be used for all compute jobs run on Alpine or
Blanca. These high-performance scratch directories are **not backed
up**, and are not appropriate for long-term storage. Data may be
purged at any time subject to overall system needs. Files are
automatically removed 90 days after their initial creation.

Users requiring longer-term retention of their files should perform
regular backups to their local machine if they have not purchased
space on the [PetaLibrary](../storage/petalibrary/index.md). Inappropriate use of scratch
storage, including attempts to circumvent the automatic file purge
policy, may result in loss of access to Research Computing resources.

### Local Scratch on Alpine and Blanca
All Alpine nodes and most Blanca nodes have a local scratch area exceeding 100GB ideal for heavily used temporary files.  This directory can be accessed in a job script with the `$SLURM_SCRATCH` variable.  To ensure local scratch space remains free for subsequent jobs files placed in this directory will be removed automatically on job completion (successful or otherwise) and cannot be recovered.  Therefore, before your job script exits it is important to copy any newly created files to a persistent file system such as your `/projects/$USER` directory. 

As an example of how to use `$SLURM_SCRATCH`, the following code copies a file to the temporary directory, operates on the file in some fashion creating a new file, then copies that new file back to the projects directory before the job ends.

```
cp /projects/user1234/job/tmp_file $SLURM_SCRATCH
# Do stuff to tmp_file and generate new_file
cp new_file /projects/user1234/job/new_file
```

## Best practices for using CURC filesystems

### Storage spaces on CURC, ordered by preference/performance for doing data Input/Output (I/O) during jobs:

1. `$SLURM_SCRATCH` (local SSD)
  * Approximately 300 GB/node
  * Lowest contention of all RC storage resources (only shared with other jobs on the same node)
  * Deleted when job terminates

2. `/scratch/alpine/$USER` (Alpine only) or `/rc_scratch/$USER` (Blanca only)
  * 10 TB/user (Alpine) or ~2 TB/user (Blanca)
  * Data purged after 90 days

3. `/pl/active/<group>`
  * Fee-based compute-capable storage platform

4. `/projects/$USER`
  * 250 GB/user
  * Only use if you have a few small files to do I/O on. 


### How to increase I/O performance: 

1. If you are running a job array and each job in the array will be reading the same dataset, `/pl/active` is not an optimal place for simultaneous reads (or writes).  Instead, copy the data to `/scratch/alpine/$USER` (Alpine) or `/rc_scratch/$USER` (Blanca) first.  

2. If you need to read data from `/pl/active` more than once during a job, copy it to `$SLURM_SCRATCH` at the beginning of the job and read it from there. Or. if the dataset is too big for `$SLURM_SCRATCH`, copy it to `/scratch/alpine/$USER` (Alpine) or `/rc_scratch/$USER` (Blanca) and read it from there. 

3. If output files from one job need to be read by other compute jobs, write to `/scratch/alpine/$USER` (Alpine) or `/rc_scratch/$USER` (Blanca). 

4. All filesystems struggle to be performant with small file I/O. If you can choose between one file and 100 files for storing the same amount of data, you will see far better performance from the single large file.

5. PetaLibrary (`/pl/active`) is backed by ZFS, which is a Copy on Write filesystem. This means that ZFS does not ever modify a block in place. If you make a small change to a file, ZFS doesn’t change the underlying block, it copies the entire block and makes your change to the new block. Over time this leads to fragmentation and poor performance. When possible, copy data from `/pl/active` to `/scratch/alpine/$USER` (Alpine) or `/rc_scratch/$USER` (Blanca), compute against it, and copy data back to `/pl/active`. This helps to avoid fragmentation and write amplification.

6.  If you reuse data within code, try to read it in once and keep it stored as a variable in memory, rather than repeatedly opening the same file each time you need the data (i.e., move file reads outside of “do loops”)

7. Complex codes such as conda environments may not run optimally out of `/pl/active`, although simple codes should be fine.  If you have code on PetaLibrary and suspect the performace is being impacted, make a copy on `/projects/$USER` and use that copy. 


## Monitoring Disk Usage

### The `curc-quota` command
Disk usage may be checked using the `curc-quota` command. When run
from a login node or Alpine `compile node`, you will see output similar to:

```
[janedoe@c3cpu-a7-u26-3 ~]$ curc-quota
------------------------------------------------------------------------
                                       Used         Avail    Quota Limit
------------------------------------------------------------------------
/home/janedoe                          1.7G          339M           2.0G
/projects/janedoe                       67G          184G           250G
/scratch/alpine1                        29G        10211G         10240G
```

_note to Blanca users: the `curc-quota` command can be run on Blanca nodes if you "module load curc-quota" first._

### The `du` command
The space occupied by a particular directory and its
subdirectories can be obtained via the `du -h` command:

```
[janedoe@c3cpu-a7-u26-3 ~]$ du -h /scratch/alpine/janedoe/WRF
698M	WRF/run
698M	WRF
```


## Backups

Regular backups are performed for all `/home` and `/projects`
directories and at a range of cadences. Low-cadence backups are
retained for longer periods of time than high-cadence backups. A
summary of the backup schedule is provided in the table below.

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

If disaster strikes and you need access to a previous version of your
`/home` or `/projects` directories, change to that directory and look
through the `.snapshot` hidden subdirectory. You will see a subdirectory
associated with each snapshot of your `/home` or `/projects`
directory, named using the time-stamp associated with the snapshot.

> Note: The `.snapshot` directory is not visible to any utilities that list directory contents, so an `ls -a` of the parent directory will not show `.snapshot`, although you can `cd` to it and list its contents with e.g. `ls -l $HOME/.snapshot`.

## File permissions, ownership, and group membership

In the Linux/Unix system, files are organized into hierarchical trees, similar to a filing cabinet. Files can have several different types, The most important for everyday use are directories and files, which can be data or executable files (programs).  Note that each file has an owner, a group, and a class of others (those not owners or group members). File permissions can be different for each of the above depending on the permissions specified for that file.

Using the `ls -l` command will list the most important attributes of the files in a directory:  
  
```
total 2712  
drwxr-xr-x 2 brwe2321 brwe2321pgrp      66 Mar 15 12:58 alpine_scratch_config  
drwxr-xr-x 2 brwe2321 brwe2321pgrp     454 May  3 14:25 bin  
drwxr-xr-x 4 brwe2321 brwe2321pgrp      53 Dec 10 17:13 codes  
-rwxrwxr-- 1 brwe2321 brwe2321pgrp      98 Dec  9 17:08 dirtest.sh  
-rw-r--r-- 1 brwe2321 brwe2321pgrp 1687552 May 18 10:53 perm_study  
drwxrwx--- 4 brwe2321 brwe2321grp       87 May 24 11:25 foobar  
drwxr-xr-x 3 brwe2321 brwe2321pgrp      74 Feb 25 13:02 packages  
-rw-r--r-- 1 brwe2321 brwe2321pgrp     563 Jun 12  2017 README.mdwn  
-rwxr-xr-x 1 brwe2321 rcopspgrp        174 May 18 17:10 test_alloc.sh

---------------------------------------------------------------------- 
permissions  lnk   owner  group  size   date/time            name
```


In the above listing:

·      the first field  is the file permissions flags (bits)

·      the second field is a count of the number of links to contents

·      the third field is the owner ID

·      the fourth field is the group ID

·      the fifth field is the size of the file (in bytes when not otherwise specified)

·      the sixth and seventh fields are the latest modification time/date of the file

·      the eighth field is the file name

The file permissions flags are arranged in four groups, the first character of the string, followed by 3 groups of 3 characters each:

·     the first character can be either  a ’-’ or a ‘d’. the ‘-’ indicates the entry is a file. The  ‘d’ indicates the entry is a directory (which can contain other files and/or directories). The ‘l’ indicate the file entry is a symbolic link to another file.

·      In each of the following three groups of three characters, ‘r’ indicates the file/directory is readable, ‘w’ indicates the file/directory is writable, and the ‘x’ indicates a file that is executable, or a directory that permits programs to execute within itself. These letters are also referred to as permission “bits” for historical reasons.

·      The three groups of permissions condition the actions of three different groups of users. The first (or left-most) group is the file/directory owner’s permissions, the next group (middle) is the permissions granted to members of the group associated with the file, and the last group (right-most) is permissions granted to all others (not owners or group members).

Note: For files, the owner and group execute flags(bits) can occasionally be replaced with an ‘s’. In the owner’s permissions bits, an ‘x’ replaced with an ‘s’ indicates the file is executable but will execute with an effective user ID of the file owner. The ‘S’ replacing the ‘x’ in the group permission bits indicates the file can execute but with effective group  set to the group of the directory. Essentially this means that new files and directories created under this directory will inherit the group of this directory. Finally, the “other” execute bit if set to ‘t’ or ‘T’, indicates that files in this directory can only be moved or deleted by the owner of the file.

For a more comprehensive and detailed exposition of the UNIX file system permissions, see the Traditional Unix permissions section of [https://en.wikipedia.org/wiki/File-system_permissions](https://en.wikipedia.org/wiki/File-system_permissions).


**How to turn on/off the execute bits**

Turn on all execute bits for `<file_pathname>`<br />
`chmod a+x <file_pathname>`

Turn off all execute bits for `<file_pathname>`<br />
`chmod a-x <file_pathname>`

Turn on “other” execute bits for `<file_pathname>`<br />  
`chmod o+x <file_pathname>`

Turn off “other” execute for `<file_pathname>`<br /> 
`chmod o-x <file_pathname>`

Turn on “group” execute bits for `<file_pathname>`<br /> 
`chmod g+x <file_pathname>`

Turn off “group” execute bits for `<file_pathname>`<br />   
`chmod g-x <file_pathname>`

Turn on “owner” execute bits for `<file_pathname>`<br /> 
`chmod u+x <file_pathname>`

Turn off “owner” execute bits for `<file_pathname>`<br /> 
`chmod u-x <file_pathname>`

See the man page for `chmod` for a complete exposition of controlling the permission bits.

**Umask and the _mode creation mask_**

The `umask` environment variable will override indicated permission bits. That is, if a bit is set in the `umask`, the corresponding permissions bit is stripped from default permissions a file or directory would otherwise be created with. This latter default permission set is known as the _mode creation mask_, a parameter each process in the Unix/Linux OS has.
 
The `umask` is usually represented by a string of octal numbers. So, for example, a `umask` of `007` will turn off the 3 permission bits for “other” in a file or directory created. `070` likewise would turn off the group permissions. The octal numbers correspond directly with the permission bits described above, so <br />
7 = rwx<br /> 
6 = rw-<br />
5 = r-x<br /> 
4 = r--<br /> 
3 = -wx<br /> 
2 = -w-<br /> 
1 = --x<br /> 

The man page for `umask` explains the details of this parameter.

**Creating and copying directories and files**

`mkdir <new_directory_name>`<br />
A directory with the specified name is created having permissions defined by the user’s default _mode creation mask_, modified by the user’s `umask`.

`cp <source_file> <destination_file>`<br /> 
The destination file will have the same permissions as the source file unless those are modified by the user’s `umask`. Note that more sophisticated copy programs can modify the destination permissions, again subject to the user’s `umask`.

`rsync -var <source_file/directory>/ <destination_file/directory/`<br />  
See our [Data Transfer](../compute/data-transfer.md#rsync) page for more information about `rsync`.

## Workspace Sharing

All users have complete control over their personal directory
permissions. While we encourage you to share your `/projects` and
`/scratch` directories with collaborators as appropriate, we strongly
discourage sharing of your `/home` directory due to the limited space
and potentially sensitive information stored there.

Directories may be shared with all Research Computing users or with
only a subset of our users. In the latter case, a system
administrator will need to add your chosen collaborators to your Linux
group. Please email <rc-help@colorado.edu> if you would like to add
users to your Linux group.

In the example that follows, we make our `/projects` directory open to
all users and then create subdirectories with select read/write
permissions for all users and our chosen collaborators.

First, we make our `/projects` directory world-readable:

```
[janedoe@c3cpu-a2-u32-4 ~]$ chmod a+rx /projects/janedoe
```

Next, we create a subdirectory that is visible to all users and which
is read-only:

```
[janedoe@c3cpu-a2-u32-4 ~]$ cd /projects/janedoe
[janedoe@c3cpu-a2-u32-4 ~]$ mkdir world_read
[janedoe@c3cpu-a2-u32-4 ~]$ chmod a+rx world_read
```

For our collaborators, we may want a writeable directory in addition
to a read-only directory:

```
[janedoe@c3cpu-a2-u32-4 ~]$ cd /projects/janedoe
[janedoe@c3cpu-a2-u32-4 ~]$ mkdir group_read
[janedoe@c3cpu-a2-u32-4 ~]$ chmod g+rx group_read
[janedoe@c3cpu-a2-u32-4 ~]$ mkdir group_read_write
[janedoe@c3cpu-a2-u32-4 ~]$ chmod g+rwx group_read_write
```

A similar methodology will need to be followed for all subdirectories
you wish to share. If you make a mistake or change your mind, use the
`-` symbol in lieu of `+` to remove privileges. Note that the `x` is
necessary if you want other users to be able to `cd` into your
directory.

