# Copy data from a Synology Network Attached Storage (NAS) device to Petalibrary

CU Research Computing (CURC) PetaLibrary allocations can be accessed via the data transfer node (DTN) hosts using _rsync_ over _ssh_. This document shows how to copy data from a Synology NAS device running DiskStation Manager (DSM) version 4.2 with hostname mylabstorage.colorado.edu to a PetaLibrary allocation named “peta_test” with RC account “RC_identikey.”  A typical use case is where a university laboratory stores data on a local Synology server in the lab, and wants to back up the data to PetaLibrary.

## Step 1: Connect to Synology via _ssh_ 

The following accounts are available for SSH remote login:
* DSM 6.0 and later: anyone in the administrators group
* DSM 5.2 and earlier/SRM: admin or root

```
$ ssh mylabstorage.colorado.edu -l admin
admin@mylabstorage.colorado.edu's password:


BusyBox v1.16.1 (2013-04-16 20:13:10 CST) built-in shell (ash)
Enter 'help' for a list of built-in commands.

mylabstorage>
```

```{note}
You may need to use the _sudo_ command to gain administrative access.
```

## Step 2: Run _ash_ to break out of restricted shell

```bash
mylabstorage> ash


BusyBox v1.16.1 (2013-04-16 20:13:10 CST) built-in shell (ash)
Enter 'help' for a list of built-in commands.

/volume1/homes/admin $
```

## Step 3: Use _telnet_ to verify that we can talk to the CURC DTN _ssh_ port

```bash
/volume1/homes/admin $ telnet dtn.rc.colorado.edu 22
```

```{note}
If the above command does not yield an SSH banner (such as ‘SSH-2.0-OpenSSH_7.4’), ssh connectivity from the Synology to the DTN hosts is not working.
```

```{important}
These instructions assume you are on a CU System campus network.
```

## Step 4: Generate keypair for connecting to PetaLibrary 

In order to allow for passwordless access to the system, which will enable you to seamlessly back up data, you need to generate a keypair for our system. This is a straightforward process and it is outlined in our [Uploading an SSH Key to CILogon Registry](../../additional-resources/registrycilogon-instructions.md) documentation. Please follow this documentation first before proceeding with the remaining steps. Note that generating a keypair yourself and placing it in `~/.ssh` on our resources will not work, you must follow the documentation linked above. 
When following this documentation you should be generating the ssh key on the Synology server. For example, you could do the following:


```bash
/volume1/homes/admin $ ssh-keygen -t rsa -b 4096 -C 'mylab synology'
```
```{note}
Press return when prompted for a passphrase to select “empty”).
```
```{note}
Passwordless data transfers are presently only available to CU System users.
```

## Step 5: test connectivity from Synology to DTN

```bash
/volume1/homes/admin $ sftp RC_identikey@dtn.rc.colorado.edu
```

```{note}
If the above command does not yield an `sftp>` prompt, ssh authentication from the Synology to the DTN hosts is not working.
```

## Step 6: Transfer the data with _rsync_

From synology:
```bash
$ rsync --protocol=29 -Havx "/volume1/mylabstorage/mylabfiles/." RC_identikey@dtn.rc.colorado.edu:/pl/active/peta_test/.
```

```{note}
If _rsync_ does not produce any errors, log in to `login.rc.colorado.edu` and check that `/pl/active/peta_test` contains the files you wanted to copy.
```

Adjust the source and destination directories as appropriate. In the above example, any files in `/volume1/mylabstorage/mylabfiles` on the Synology will be copied to `/pl/active/peta_test` on the DTNs. You can add the `--delete` argument to the _rsync_ command, which will remove any files from /pl/active/peta_test that are not present in /volume1/mylabstorage/mylabfiles.

## Step 7 (optional): Schedule regular backups

If you want your backups to occur at a specified time each day or week, please refer to the [Synology Task Scheduler documentation](https://www.synology.com/en-global/knowledgebase/DSM/help/DSM/AdminCenter/system_taskscheduler).  

## Useful links

* [Synology documentation](https://www.synology.com/en-us/support/documentation?query=&type=All&section=All&p=1)
* [CURC data transfer documentation](../../compute/data-transfer.md)

