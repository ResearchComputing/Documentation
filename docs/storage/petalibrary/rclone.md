## Backing up local data to PetaLibrary

This guide details the process of making a backup for local data on your laptop or lab server to a PetaLibrary allocation. The method employs the software _rclone_, which is a command line application that is available for many architectures. While the following tutorial is tailored for a MacOS user, the general steps to follow are the same and are relevant for Windows and Linux users too.

### Generate public/private keypair on login.rc.colorado.edu

In this step you will login to an RC login node (`ssh login.rc.colorado.edu`) and generate an ssh keypair. You don't need to complete this step on a login node if you have ssh-keygen installed on your system. Be sure to generate a key in PEM format. Here is the command to generate a key in PEM format with a uniquename, after you have logged in:
```
$ ssh-keygen -f ~/.ssh/rclone_ssh_key -m PEM
```
You will be prompted to enter a passphrase to protect the key. For automated backups, you will either want a key with no passphrase, or to set a passphrase and use something like ssh-agent to hold the key in memory. The easiest option is to not set a passphrase. Here is sample output from running ssh-ksygen:

```
$ ssh-keygen -f ~/.ssh/rclone_ssh_key -m PEM
Generating public/private rsa key pair.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/jesse/.ssh/rclone_ssh_key.
Your public key has been saved in /home/jesse/.ssh/rclone_ssh_key.pub.
The key fingerprint is:
SHA256:ftryJYQ2LRnNQ/fSzm+iB0Tg8/LkePqVyeDky2z3JvA jesse@login10
The key's randomart image is:

+---[RSA 2048]----+
|          o..    |
|         = ..o   |
|        . *.. o  |
|         = +.+   |
|        S +.= o  |
|       o + Xoo + |
|        . + B+* o|
|        .+ B.+Eo.|
|        .o+o*o +.|
+----[SHA256]-----+
```

Your home directory should now have the files `~/.ssh/rclone_ssh_key` and `~/.ssh/rclone_ssh_key.pub`. The `rclone_ssh_key` is your private key, be careful with it as anyone with this key can access resources that trust the public key.

### Copy public key to your authorized_keys file

Copy the newly generated public key rclone_ssh_key.pub to your authorized_keys file:
```
$ cat ~/.ssh/rclone_ssh_key.pub >> ~/.ssh/authorized_keys
```
This will append the contents of `rclone_ssh_key.pub` to the file `authorized_keys` (authorized_keys will be created if it does not exist). Now anyone with your private key (`rclone_ssh_key`) can login to hosts that mount home directories from RC core storage.

### Copy private key to the backup source host

This next step can't be documented exactly as every client system will be different, but use a secure method (such as scp or sftp) to copy the private key in `~/.ssh/rclone_ssh_key` to the system that you want to back up to PetaLibrary (e.g., your laptop or lab server).

**Windows:** Windows users should copy client (e.g. Globus, WinSCP, WSL2, ect) as Admin. Change directories to rclone file location and run:

<!--
```$ .\rclone.exe config```
...then select n) New Remote
-->

### Install rclone on the backup source host

The rclone application is available download here for a variety of architectures. [Download rclone here](https://rclone.org/downloads/) and follow Rclone's provided instructions to setup the application.   

_Note: You must have adminstrative priveleges on your laptop or lab server in order to install software. If you do not, you'll need to ask your system administrator._

**Windows:** Download rclone and manually unzip the compressed files to your desired install location. Take note of this install location since you will need to manually access these binaries to setup and run rclone. 


### Configure rclone

The rclone application will require you to configure endpoints. Once your endpoints are configured, you can copy data to/from your local system to configured endpoints. Please note that rclone should only ever be connected to an RC Data Transfer Node (DTN). Because of this, we will configure an sftp endpoint in rclone that points to RC's DTN hosts. You must be connected to [CU's Network](https://oit.colorado.edu/services/network-internet-services/vpn) for this connection to work. For more information on DTN nodes, [check out our documentation on data transfers.](../../compute/data-transfer.html)


In this example we use rclone to create an sftp endpoint with the following settings:
```
name: cu_rc_dtn
type: sftp
host: dtn-data.rc.int.colorado.edu
key_file = /Users/jesse/.ssh/rclone_ssh_key
user = jesse
```
The rclone application is interactive and will prompt you for all of the above information. Here is the ouput of an example interactive session when creating an endpoint with the above settings:

```$  rclone config```     

**Windows:** From the Command Prompt, navagate to rclone file location and run:
```$ .\rclone.exe config```

```
2020/05/18 15:00:00 NOTICE: Config file "/Users/jesse/.config/rclone/rclone.conf" not found - using defaults
No remotes found - make a new one
n) New remote
s) Set configuration password
q) Quit config
n/s/q> n
name> cu_rc_dtn               
Type of storage to configure.
Enter a string value. Press Enter for the default ("").
Choose a number from below, or type in your own value
 1 / 1Fichier
   \ "fichier"
 2 / Alias for an existing remote
   \ "alias"
 3 / Amazon Drive
   \ "amazon cloud drive"
 4 / Amazon S3 Compliant Storage Provider (AWS, Alibaba, Ceph, Digital Ocean, Dreamhost, IBM COS, Minio, etc)
   \ "s3"
 5 / Backblaze B2
   \ "b2"
 6 / Box
   \ "box"
 7 / Cache a remote
   \ "cache"
 8 / Citrix Sharefile
   \ "sharefile"
 9 / Dropbox
   \ "dropbox"
10 / Encrypt/Decrypt a remote
   \ "crypt"
11 / FTP Connection
   \ "ftp"
12 / Google Cloud Storage (this is not Google Drive)
   \ "google cloud storage"
13 / Google Drive
   \ "drive"
14 / Google Photos
   \ "google photos"
15 / Hubic
   \ "hubic"
16 / In memory object storage system.
   \ "memory"
17 / JottaCloud
   \ "jottacloud"
18 / Koofr
   \ "koofr"
19 / Local Disk
   \ "local"
20 / Mail.ru Cloud
   \ "mailru"
21 / Mega
   \ "mega"
22 / Microsoft Azure Blob Storage
   \ "azureblob"
23 / Microsoft OneDrive
   \ "onedrive"
24 / OpenDrive
   \ "opendrive"
25 / Openstack Swift (Rackspace Cloud Files, Memset Memstore, OVH)
   \ "swift"
26 / Pcloud
   \ "pcloud"
27 / Put.io
   \ "putio"
28 / QingCloud Object Storage
   \ "qingstor"
29 / SSH/SFTP Connection
   \ "sftp"
30 / Sugarsync
   \ "sugarsync"
31 / Transparently chunk/split large files
   \ "chunker"
32 / Union merges the contents of several remotes
   \ "union"
33 / Webdav
   \ "webdav"
34 / Yandex Disk
   \ "yandex"
35 / http Connection
   \ "http"
36 / premiumize.me
   \ "premiumizeme"
Storage> 29
** See help for sftp backend at: https://rclone.org/sftp/ **

SSH host to connect to
Enter a string value. Press Enter for the default ("").
Choose a number from below, or type in your own value
 1 / Connect to example.com
   \ "example.com"
host> dtn-data.rc.int.colorado.edu
SSH username, leave blank for current username, jesse
Enter a string value. Press Enter for the default ("").
user> 
SSH port, leave blank to use default (22)
Enter a string value. Press Enter for the default ("").
port> 
SSH password, leave blank to use ssh-agent.
y) Yes type in my own password
g) Generate random password
n) No leave this optional password blank (default)
y/g/n> 
Path to PEM-encoded private key file, leave blank or set key-use-agent to use ssh-agent.
Enter a string value. Press Enter for the default ("").
key_file> /Users/jesse/.ssh/rclone_ssh_key
The passphrase to decrypt the PEM-encoded private key file.

Only PEM encrypted key files (old OpenSSH format) are supported. Encrypted keys
in the new OpenSSH format can't be used.
y) Yes type in my own password
g) Generate random password
n) No leave this optional password blank (default)
y/g/n> 
When set forces the usage of the ssh-agent.

When key-file is also set, the ".pub" file of the specified key-file is read and only the associated key is
requested from the ssh-agent. This allows to avoid `Too many authentication failures for *username*` errors
when the ssh-agent contains many keys.
Enter a boolean value (true or false). Press Enter for the default ("false").
key_use_agent> 
Enable the use of insecure ciphers and key exchange methods. 

This enables the use of the the following insecure ciphers and key exchange methods:

- aes128-cbc
- aes192-cbc
- aes256-cbc
- 3des-cbc
- diffie-hellman-group-exchange-sha256
- diffie-hellman-group-exchange-sha1

Those algorithms are insecure and may allow plaintext data to be recovered by an attacker.
Enter a boolean value (true or false). Press Enter for the default ("false").
Choose a number from below, or type in your own value
 1 / Use default Cipher list.
   \ "false"
 2 / Enables the use of the aes128-cbc cipher and diffie-hellman-group-exchange-sha256, diffie-hellman-group-exchange-sha1 key exchange.
   \ "true"
use_insecure_cipher> 
Disable the execution of SSH commands to determine if remote file hashing is available.
Leave blank or set to false to enable hashing (recommended), set to true to disable hashing.
Enter a boolean value (true or false). Press Enter for the default ("false").
disable_hashcheck> 
Edit advanced config? (y/n)
y) Yes
n) No (default)
y/n> 
Remote config
--------------------
[cu_rc_dtn]
type = sftp
host = dtn-data.rc.int.colorado.edu
key_file = /Users/jesse/.ssh/rclone_ssh_key
--------------------
y) Yes this is OK (default)
e) Edit this remote
d) Delete this remote
y/e/d> 
Current remotes:

Name                 Type
====                 ====
cu_rc_dtn            sftp

e) Edit existing remote
n) New remote
d) Delete remote
r) Rename remote
c) Copy remote
s) Set configuration password
q) Quit config
e/n/d/r/c/s/q>
```


### Verify rclone config

You can verify your settings by running 'rclone config show'. The results from the example above looked like this after running through the initial configuration:

```
$ rclone config show
```

**Windows:** Windows host users
```$ .\rclone.exe config```

```
[cu_rc_dtn]
type = sftp
host = dtn-data.rc.int.colorado.edu
key_file = /Users/jesse/.ssh/rclone_ssh_key
user = jesse
md5sum_command = none
sha1sum_command = none
```


### Test rclone

_Example_: The syntax for using rclone to synchronize a local directory `/tmp/local_backup_dir` to a directory `pl_backup_dir` in a PetaLibrary allocation named `pl_allocation`, the command (executed from your laptop or lab server) would be:

```$ rclone sync /tmp/local_backup_dir cu_rc_dtn:/pl/active/pl_allocation/pl_backup_dir```

This should synchronize the data in the two directories (note that _rclone_ does not report on the transfer so it will look like your terminal is "frozen" until the transfer is complete). The source directory will not be modified, and `pl_backup_dir` will have files added/removed to match the contents of `local_backup_dir`. 

### Run rclone on a schedule
On Mac or Linux hosts, you can set up a cron job to run the rclone sync job regularly. To create a crontab entry type:

```$ crontab -e```

And then add the line for the automated job you want to run, e.g.:
```
0 4 * * 1 rclone sync /tmp/local_backup_dir cu_rc_dtn:/pl/active/pl_allocation/pl_backup_dir
```
This would run the rclone sync command every Monday at 4am. The syntax for a crontab entry is:

```
* * * * * command
* - minute (0-59)
* - hour (0-23)
* - day of the month (1-31)
* - month (1-12)
* - day of the week (0-6, 0 is Sunday)
command - command to execute
(from left-to-right)
```

Windows systems can set up scheduled tasks to run rclone automatically.

**Windows:** Windows host users, if you do not have WSL2 installed use taskschd.msc (Task Scheduler) as Admin and run Action=>Create Basic Task

Couldn't find what you need? [Provide feedback on these docs!](https://forms.gle/bSQEeFrdvyeQWPtW9)
