# Mounting a remote filesystem from a CUmulus Virtual Machine

___Learning Objectives:___
* [Install the software needed to remotely mount a CURC PetaLibrary allocation](https://github.com/ResearchComputing/CUmulus_tutorials/edit/main/tutorial4/README.md#part-1-install-sshfs)
* [Establish the remote mount to PetaLibrary](https://github.com/ResearchComputing/CUmulus_tutorials/edit/main/tutorial4/README.md#part-2-mount-petalibrary-with-sshfs)
* [Test that you can view files and copy files to/from PetaLibrary](https://github.com/ResearchComputing/CUmulus_tutorials/edit/main/tutorial4/README.md#part-3-test-your-mount)
* [Remove the remote mount](https://github.com/ResearchComputing/CUmulus_tutorials/edit/main/tutorial4/README.md#part-4-remove-your-mount)

## Introduction

Remote filesystems on CURC can be mounted as filesystems on CUmulus VMs.  This enables access to large datasets that may not otherwise be practical to place on the CUmulus VM, where storage is more limited. This tutorial demonstrates this capability. As a prerequisite, it is assumed you have already "spun-up" a CUmulus VM, as covered in [Tutorial 1](./cumulus1.md).

## Tutorial

Completing the steps below requires that you have first [logged into your VM](./cumulus1.md#part-3-logging-into-your-instance)

###  Part 1: Install `sshfs`

The [sshfs](https://osxfuse.github.io) software package provides an open-source solution for mounting your Petalibrary allocation to your CUmulus VM. 

If you are on an _Ubuntu_ or _Debian_ VM, `sshfs` can be installed as follows:

```bash
sudo apt-get install sshfs
```

...or, if you are on a _Centos_ or _Redhat_ VM, `sshfs` can be installed as follows:

```bash
yum install fuse-sshfs
```

...or, if you are on a _Windows_ VM, see our documentation [here](https://curc.readthedocs.io/en/latest/storage/petalibrary/mounting.html?highlight=sshfs#sshfs-on-windows)

###  Part 2: Mount PetaLibrary with `sshfs`


Create a folder on the VM where you would like to mount your PetaLibrary allocation.  For simplicity, we will create a folder called `mypetalibrary` in our home (`~`) directory, but you could place the directory anywhere and call it anything you want:

```bash
mkdir ~/mypetalibrary
```

Now mount your PetaLibrary allocation to the directory.  The generic syntax is:

```bash
sshfs <your-rc-username>@dtn.rc.colorado.edu:/pl/active/<your-pl-directory> <local-directory>
```

For example if your CURC username is `ralphie` and you want to mount your PetaLibrary allocation called `rcops` to `~/mypetalibrary`: 

```bash
sshfs ralphie@dtn.rc.colorado.edu:/pl/active/rcops ~mypetalibrary
```

You will be prompted for your password after execution. Type your password and accept the duo prompt.
Your selected directory will now be mounted to your Petalibrary allocation.

###  Part 3: Test your mount

Can you _see_ the files in your PetaLibrary allocation? 

```bash
ubuntu@198.59.83.67:$ ls -l ~/mypetalibrary/
drwxr-sr-x 1  411465 1000000        2 Jun  8  2021  gtest
drwxr-sr-x 1  416810 1000000        8 Feb 20  2020  ior-testing
-rw-r--r-- 1 root    root     4194304 Oct  8  2020  testfile
```

...yes!  

Can you copy a file _from_ the PetaLibrary allocation? 

```bash
ubuntu@198.59.83.67:$ cp ~/mypetalibrary/testfile .
ubuntu@198.59.83.67:$ ls -l .
total 4100
drwxrws--x 1 1000000 1000000      70 Mar  2 16:07 mypetalibrary
-rw-r--r-- 1 ubuntu  ubuntu  4194304 Mar 11 19:13 testfile
```

...yes! Can you create a new file and copy it _to_ the PetaLibrary allocation?

```bash
ubuntu@198.59.83.67:$ touch newtestfile
ubuntu@198.59.83.67:$ cp newtestfile ~/mypetalibrary/
ubuntu@198.59.83.67:$ ls -l ~/mypetalibrary/newtestfile
-rw-r--r-- 1 122971 1000000 0 Mar 11 19:14 /home/ubuntu/mypetalibrary/newtestfile
```

...yes!  Note that the user and group IDs (UID/GID) don't map from CURC to CUmulus by default. so these will show up as numbers that correspond with the username under which you established the ssh mount (i.e., `122971` maps to `ralphie` in the example above).

### Part 4: Remove your mount

Should you need to remove your mount, type the following, for example:

```bash
sshfs umount ~/mypetalibrary
```

## Additional Information

  * [CUmulus documentation](../cloud/cumulus/cumulus.md)
  * [OpenStack User Documentation](https://docs.openstack.org/horizon/latest/user/index.html)
  * [PetaLibrary Documentation](../storage/petalibrary/index.md)


> This work has been funded in part by the National Science Foundation under grant OAC-1925766
