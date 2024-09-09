# Backing up local data to PetaLibrary

This guide details the process of making a backup for local data on your laptop or lab server to a PetaLibrary allocation. The method employs the software _rclone_, which is a command line application that is available for many architectures. While the following tutorial is tailored for a MacOS user, the general steps to follow are the same and are relevant for Windows and Linux users too.

## Generate public/private keypair for CURC resources 

```{note}
Presently passwordless access is only available to users affiliated with the CU system.
```

In order to allow for passwordless access to CURC, which will enable you to seamlessly back up data, you need to generate a keypair for our system. This is a straightforward process and it is outlined in our [Uploading an SSH Key to CILogon Registry](../../additional-resources/registrycilogon-instructions.md) documentation. Please follow this documentation first before proceeding with the remaining steps. Note that generating a keypair yourself and placing it in `~/.ssh` on CURC resources will not work -- you must follow the documentation linked above. 

```{important}
Windows users should copy client (e.g. Globus, WinSCP, WSL2, ect) as Admin. Change directories to rclone file location and run `.\rclone.exe config`, then select `n) New Remote`.
```

## Install rclone on the backup source host

The rclone application is available for a variety of architectures. [Download rclone](https://rclone.org/downloads/) and follow Rclone's provided instructions to setup the application.   

```{important}
You must have adminstrative priveleges on your laptop or lab server in order to install software. If you do not, you'll need to ask your system administrator._
```

```{note}
If you use Windows, download rclone and manually unzip the compressed files to your desired install location. Take note of this install location since you will need to manually access these binaries to setup and run rclone. 
```

## Configure rclone

The rclone application will require you to configure endpoints. Once your endpoints are configured, you can copy data to/from your local system to configured endpoints. Please note that rclone should only ever be connected to an RC Data Transfer Node (DTN). Because of this, we will configure an sftp endpoint in rclone that points to RC's DTN hosts. You must be connected to [CU's Network](https://oit.colorado.edu/services/network-internet-services/vpn) for this connection to work. For more information on DTNs, [check out our documentation on data transfers.](../../compute/data-transfer.md)


In this example we use rclone to create an sftp endpoint with the following settings:
```
name: cu_rc_dtn
type: sftp
host: dtn.rc.colorado.edu
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
host> dtn.rc.colorado.edu
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
key_file> 
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
host = dtn.rc.colorado.edu
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


## Verify rclone config

You can verify your settings by running 'rclone config show'. The results from the example above looked like this after running through the initial configuration:

```
$ rclone config show
```

**Windows:** Windows host users
```$ .\rclone.exe config```

```
[cu_rc_dtn]
type = sftp
host = dtn.rc.colorado.edu
user = jesse
md5sum_command = none
sha1sum_command = none
```


## Test rclone

_Example_: The syntax for using rclone to synchronize a local directory `/tmp/local_backup_dir` to a directory `pl_backup_dir` in a PetaLibrary allocation named `pl_allocation`, the command (executed from your laptop or lab server) would be:

```$ rclone sync /tmp/local_backup_dir cu_rc_dtn:/pl/active/pl_allocation/pl_backup_dir```

This should synchronize the data in the two directories (note that _rclone_ does not report on the transfer so it will look like your terminal is "frozen" until the transfer is complete). The source directory will not be modified, and `pl_backup_dir` will have files added/removed to match the contents of `local_backup_dir`. 

## Run rclone on a schedule
On Mac or Linux hosts, you can set up a cron job to run the rclone sync job regularly (this step assumes you have set up an ssh key for passwordless transfers). To create a crontab entry type:

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

