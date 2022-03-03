### Copy data from a Synology Network Attached Storage (NAS) device to Petalibrary

CU Research Computing (CURC) PetaLibrary allocations can be accessed via the data transfer node (DTN) hosts using _rsync_ over _ssh_. This document shows how to copy data from a Synology NAS device running DiskStation Manager (DSM) version 4.2 with hostname mylabstorage.colorado.edu to a PetaLibrary allocation named “peta_test” with RC account “RC_identikey.”  A typical use case is where a university laboratory stores data on a local Synology server in the lab, and wants to back up the data to PetaLibrary.

#### Step 1: Connect to Synology via _ssh_ 

The following accounts are available for SSH remote login:
* DSM 6.0 and later: anyone in the administrators group
* DSM 5.2 and earlier/SRM: admin or root

_Note: You may need to use the _sudo_ command to gain administrative access._

```bash
$ ssh mylabstorage.colorado.edu -l admin
admin@mylabstorage.colorado.edu's password:


BusyBox v1.16.1 (2013-04-16 20:13:10 CST) built-in shell (ash)
Enter 'help' for a list of built-in commands.

mylabstorage>
```


#### Step 2: Run _ash_ to break out of restricted shell

```bash
mylabstorage> ash


BusyBox v1.16.1 (2013-04-16 20:13:10 CST) built-in shell (ash)
Enter 'help' for a list of built-in commands.

/volume1/homes/admin $
```

#### Step 3: Use _telnet_ to verify that we can talk to the CURC DTN _ssh_ port

```bash
/volume1/homes/admin $ telnet dtn.rc.int.colorado.edu 22

_Note: if the above command does not yield an SSH banner (such as ‘SSH-2.0-OpenSSH_7.4’), ssh connectivity from the Synology to the DTN hosts is not working._
```
_Note: These instructions assume you are on a CU Boulder campus network._

#### Step 4: Use _ssh-keygen_ to generate an _ssh_ key for connecting to PetaLibrary 

_(Note for below: Press return when prompted for a passphrase to select “empty”)._

```bash
/volume1/homes/admin $ ssh-keygen -t rsa -b 4096 -C 'mylab synology'
Generating public/private rsa key pair.
Enter file in which to save the key (/var/services/homes/admin/.ssh/id_rsa):
Created directory '/var/services/homes/admin/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /var/services/homes/admin/.ssh/id_rsa.
Your public key has been saved in /var/services/homes/admin/.ssh/id_rsa.pub.
The key fingerprint is:
...
```

Note that _ssh-keygen_ will create two “keys”, one that is _private_ and the other that is _public_. The _private_ key will stay on the Synology and the _public_ key will be copied to any host you want to access, in this case the CURC system.  For those with interest in how  SSH public key authentication works, see the [_ssh_ documentation](https://www.ssh.com/academy/ssh/public-key-authentication).

#### Step 5: Add the public key from synology to CURC

On synology:

```bash
$ cat .ssh/id_rsa.pub
```
_This command will dump the contents of the public keys file to your screen. Now copy the new key to your clipboard._
```bash
$ ssh RC_identikey@login.rc.colorado.edu
$ mkdir -p ~/.ssh
```

Now open the file _~/.ssh/authorized_keys_ in your favorite Linux editor (e.g., _nano_, _vi_ or _emacs_) and paste output from your clipboard obtained from the _cat_ command above. Save the file and exit.

#### Step 6: test connectivity from Synology to DTN

```bash
/volume1/homes/admin $ sftp RC_identikey@dtn.rc.int.colorado.edu
```

_Note: if the above command does not yield an `sftp>` prompt, ssh authentication from the Synology to the DTN hosts is not working._

#### Step 7: Transfer the data with _rsync_

From synology:
```bash
$ rsync --protocol=29 -Havx "/volume1/mylabstorage/mylabfiles/." RC_identikey@dtn.rc.int.colorado.edu:/pl/active/peta_test/.
```

_Note: If _rsync_ does not produce any errors, log in to login.rc.colorado.edu and check that /pl/active/peta_test contains the files you wanted to copy._

Adjust the source and destination directories as appropriate. In the above example, any files in `/volume1/mylabstorage/mylabfiles` on the Synology will be copied to `/pl/active/peta_test` on the DTNs. You can add the `--delete` argument to the _rsync_ command, which will remove any files from /pl/active/peta_test that are not present in /volume1/mylabstorage/mylabfiles.

#### Step 8 (optional): Schedule regular backups

If you want your backups to occur at a specified time each day or week, please refer to the [Synology Task Scheduler documentation](https://www.synology.com/en-global/knowledgebase/DSM/help/DSM/AdminCenter/system_taskscheduler).  

#### Useful links

* [Synology documentation](https://www.synology.com/en-us/support/documentation?query=&type=All&section=All&p=1)
* [CURC data transfer documentation](https://curc.readthedocs.io/en/latest/compute/data-transfer.html)
