# Data Transfer

Research Computing supports several methods of file transfer. File
transfers from a local system can be done through a web-based
application called _Globus_ or through command-line tools such as
secure copy (_scp_), secure ftp (_sftp_) and _rsync_. 

Data transfers using SSH protocols can be done through the 
[CURC data transfer nodes](./node-types.md) (DTN). 
Transfers via the DTNs support all types of transfers, including large and/or frequent file
transfers and automated (passwordless) transfers.

<iframe width="560" height="315" src="https://www.youtube.com/embed/UMBD7pSE0qI" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

## Globus transfers

Globus file transfers are typically initiated through an interactive
web application (command-line access to Globus is also available, but
is beyond the scope of this document). Globus addresses deficiencies
in traditional file-transfer mechanisms by automating large data
transfers, resuming failed transfers, distributing large transfers
across multiple servers, and brokering direct transfers between remote
computing centers. Globus performs an MD5-Checksum for transfer verification.

Globus can be used on macOS, Linux, and Windows operating systems and
is RC's recommended way of transferring data.

[Sign into Globus Connect](https://app.globus.org/) by
selecting "University of Colorado at Boulder" from the dropdown menu
and by logging in using your CU IdentiKey and password.

> **_Note for non-CU Boulder users:_** If you are with an institution other than CU Boulder (e.g. **ACCESS**), your institution may still be available for Globus authentication using the InCommon federation. Look for your institution in the dropdown menu (e.g. instead of `University of Colorado at Boulder` use `ACCESS`) and sign in with your local credentials. If your institution is not listed, you will need to [create a Globus account](https://www.globusid.org/create).

![](https://raw.githubusercontent.com/ResearchComputing/Research-Computing-User-Tutorials/master/File-Transfers/globus-image-1.png)

Research Computing storage resources are available via multiple Globus
"endpoints." You can connect to an RC endpoint using the "collections"
field in the Globus web interface and searching for `CU Boulder
Research Computing`. Log into the endpoint using your Research
Computing credentials.

You must configure a local endpoint in order to transfer files to/from
your local computer. You can easily set up a Globus endpoint by
installing [Globus Connect
Personal](https://www.globus.org/globus-connect-personal)

Using the web app, connect your local workstation endpoint with the
Research Computing endpoint and transfer files easily using the Globus
GUI.

![](https://raw.githubusercontent.com/ResearchComputing/Documentation/4597b5079815b791944251a1645ae91180e22d59/File-Transfers/globus-image-2new.PNG)


## Guest Collections (Globus Shared Endpoints)

Using a Guest Collection (also known as a "Shared Endpoint"), You can share
any file or folder that you have access to with anyone who
has a Globus account. This is particularly useful for PetaLibrary users. PetaLibrary 
allocation owners can nominate a technical contact that is able to create [Globus Guest
Collections](https://docs.globus.org/how-to/share-files/) within their PetaLibrary allocation.

Detailed information on creating Guest Collections is available [at
docs.globus.org](https://docs.globus.org/how-to/share-files/).

## Globus to AWS S3 Bucket connection

CU Research Computing has a trial license for Globus to AWS S3 bucket connections which allow for transfers to/from CURC resources to AWS S3 buckets using the familiar Globus web app. For those that would like to use a command-line tool rclone is also available for transfers to/from AWS S3 buckets (see [rclone example](#rclone)). For _both_ transfer methods it is assumed you already have an AWS S3 bucket already created and available. First search for your S3 bucket in the Globus collections search bar. The first time you establish connection to your S3 bucket you will need to authenticate via 2 sources:

1) Your CU IdentiKey and accept a Duo push
2) Your AWS Credentials (access key and secret key)

Once you have signed in one time, your AWS credentials will be stored on your individual Globus account. You will now be able to explore the file structure like you would any other Globus endpoint. 

> Note: Transfer speeds from S3 buckets to CURC resources are roughly 20-30 times higher than the opposite direction. We are currently investigating this asymmetry, but if you are in need of fast transfer speeds from CURC resources to your S3 bucket we recommend using rclone.



## Filezilla

RC Users also have the option of connecting to RC via _Filezilla_. _Filezilla_ is a file transfer GUI application that can be used on Windows, Mac, and Linux. Simply [install Filezilla](https://filezilla-project.org/) and follow these steps:

1. Fill in the hostname, username, and password fields at the top of the application window.

    - _Data Transfer Node_
      - Host: sftp://dtn.rc.colorado.edu
      - Username: your-rc-username
      - Password: your-rc-password

2. Press Enter. Accept your Duo 2-Factor notification. If the connection succeeds you will see your CURC filesystem on the “Remote Site” tab.
3. Navigate to the file you would like to transfer in either your local filesystem or your CURC filesystem. Right click the file and click "Upload" or "Download".

__Troubleshooting:__
- If your connection is timing out before getting a Duo notification, try increasing the _Timeout_ setting in `File->Settings`.
- If you receive the message 'Insecure FTP Notification', simply click cancel and ensure you have selected 'sftp' as your file transfer method.
- If your connection to a Data Transfer Node is not prompting a Duo notification double check you are connected to the CU Boulder Internal Network (if you are off campus VPN is required to connect to the campus internal network).


## Secure Copy (scp)

The Secure Copy utility, `scp`, can send data to and fetch data
from a remote server.

In the examples here, replace `<path-to-file>` with the path of the
file you wish to copy, `<username>` with your Research Computing
username, and `<target-path>` with the full path to the directory you
would like to send the file to.

```bash
# Copying files from a local workstation to Research Computing
scp <path-to-file> <username>@dtn.rc.colorado.edu:<target-path>   
```

```bash
# Copying files from Research Computing to a local workstation
scp <username>@dtn.rc.colorado.edu:<path-to-file> <target-path>    
``` 

Windows users can access scp through PowerShell or using a GUI
application like [WinSCP](https://winscp.net/eng/docs/protocols).

For more information on secure copy take a [look at some of our listed
resources](#more-reading) or consult the scp manual page.


## Rsync

While `scp` is useful for simple file copy operations, the `rsync`
utility can be used to synchronize files and directories across two
locations. This can often lead to efficiencies in repeat-transfer
scenarios, as rsync only copies files that are different between the
source and target locations (and can even transfer partial files when
only part of a file has changed). This can be very useful in reducing
the amount of copies you may perform when synchronizing two
datasets.

In the examples here, replace `<path-to-file>` with the path of the
file you wish to copy, `<username>` with your Research Computing
username, and `<target-path>` with the full path to the directory you
would like to send the file to.

```bash
# Synchronizing from a local workstation to Research Computing
rsync -r <path-to-directory> <username>@dtn.rc.colorado.edu:<target-path>  
```

```bash
# Synchronizing from Research Computing to a local workstation
rsync -r <username>@dtn.rc.colorado.edu:<path-to-directory> <target-path>  
```

rsync is not available on Windows by default, but [may be installed
individually](https://www.itefix.net/cwrsync) or as part of [Windows
Subsystem for Linux
(WSL)](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

For more information on rsync [check out some of our listed
resources](#more-reading) or consult the rsync manual page.


## Interactive file transfer with sftp

The `sftp` utility is an interactive alternative to `scp` that allows
multiple, bi-directional transfer operations in a single
session. Within an sftp session, a series of domain-specific file
system commands can be used to navigate, move, remove, and copy data
between a local system and Research Computing resources.

```bash
sftp <username>@dtn.rc.colorado.edu
```

We can then use various commands to traverse and manipulate both local
and remote file systems.

Command | Function | Example
--------|--------------------------------------------------------------------|----------
cd      | Changes the directory of the remote computer                       | cd remote_directory
lcd     | Changes the directory of the local computer                        | lcd local_directory
ls      | Lists the contents of the remote directory                         | ls
lls     | Lists the contents of the local directory                          | lls
pwd     | Prints working directory of the remote computer                    | pwd
lpwd    | Prints working directory of the local computer                     | lpwd
get     | Copies a file from the remote directory to the local directory     | get remote_file
put     | Copies a file from the local directory to the remote directory     | put local_file
exit    | Closes the connection to the remote computer and exits the program | exit
help    | Displays application information on using commands                 | help

Windows users can access sftp through PowerShell or using a GUI
application like [WinSCP](https://winscp.net/eng/docs/protocols).

For more information on sftp [check out some of our listed
resources](#more-reading) or consult the sftp manual page.


## Automated scp and rsync

Key-based transfers over the DTNs are only available to CU Boulder, CU Anschutz, and CU Denver users. *You must be on a CU (UCB/AMC/UCD) campus network or logged into the campus VPN to perform passwordless data transfers to CURC.* The `scp` and `rsync` commands both allow a user to transfer files without needing to reenter a password. All that is required is a few
simple setup procedures to prepare your local machine.
  
*Note: these instructions only apply to local macOS and Linux systems. Automating file transfers from Windows is outside of the scope of this document.*

1. Generate a local ssh key pair. You will only need to perform this once per local system. From a local terminal run:

```bash
ssh-keygen -t ed25519
``` 

This creates `~/.ssh/id_ed25519` and `~/.ssh/id_ed25519.pub` on your
local workstation ("~" denotes your home directory). `id_ed25519.pub`
is public, and can be shared with others (including Research
Computing). `id_ed25519` is private and **should never leave the
system that it was generated on.**

2. Follow the instructions [here](../additional-resources/registrycilogon-instructions.md) for requesting access to the CILogon Registry and uploading an ssh key.

3. Use `rsync` or `scp` to transfer files using an ssh key. 

With an ssh key pair generated and uploaded to <https://registry.cilogon.org>,
you are ready to transfer files over the DTNs using `rsync` or `scp`. 

```bash
rsync -av ./myfile.txt dtn.rc.colorado.edu:/projects/ralphie/myfile.txt    # using rsync

scp -v ./myfile23.txt dtn.rc.colorado.edu:/pl/active/crdds/myfile.txt      # using scp
```

## Rclone 

Rclone is a command line program to manage files on cloud storage. It is a feature rich alternative to cloud vendors' web storage interfaces. [Over 40 cloud storage products](https://rclone.org/#providers) support rclone including S3 object stores, business & consumer file storage services, as well as standard transfer protocols. Rclone has powerful cloud equivalents to the unix commands rsync, cp, mv, mount, ls, ncdu, tree, rm, and cat. Rclone's familiar syntax includes shell pipeline support, and `--dry-run` protection. It can be used at the command line, in scripts or via its [API](https://rclone.org/rc/).

### What can rclone do for you?

**Rclone helps you:**
- Backup (and encrypt) files to cloud storage
- Restore (and decrypt) files from cloud storage
- Mirror cloud data to other cloud services or locally
- Migrate data to the cloud, or between cloud storage vendors
- Mount multiple, encrypted, cached or diverse cloud storage as a disk
- Analyse and account for data held on cloud storage using [lsf](https://rclone.org/commands/rclone_lsf/), [ljson](https://rclone.org/commands/rclone_lsjson/), [size](https://rclone.org/commands/rclone_size/), [ncdu](https://rclone.org/commands/rclone_ncdu/) 
- [Union](https://rclone.org/union/) file systems together to present multiple local and/or cloud file systems as one

### Features

- Transfers
	- MD5, SHA1 hashes are checked at all times for file integrity
	- Timestamps are preserved on files
	- Operations can be restarted at any time
	- Can be to and from network, e.g. two different cloud providers
	- Can use multi-threaded downloads to local disk
- [Copy](https://rclone.org/commands/rclone_copy/) new or changed files to cloud storage
- [Sync ](https://rclone.org/commands/rclone_sync/) (one way) to make a directory identical
- [Move](https://rclone.org/commands/rclone_move/) files to cloud storage deleting the local after verification
- [Check](https://rclone.org/commands/rclone_check/) hashes and for missing/extra files
- [Mount](https://rclone.org/commands/rclone_mount/) your cloud storage as a network disk
- [Serve](https://rclone.org/commands/rclone_serve/) local or remote files over HTTP/WebDav/FTP/SFTP/dlna

### How to use rclone with CURC

Since rclone is intended to be used with cloud technologies, any server that can use cloud protocols can use rclone to transfer data. Rclone can be used on the CURC system to connect and transfer data to/from cloud-based storage (e.g. google drive or AWS S3 buckets) as well as locally from your machine to connect to RC storage via ssh/sftp connection.

#### Step 1: Make sure rclone is installed

**On a laptop or desktop:** Before connecting CURC storage resources to your local machine, you will need to first [download](https://rclone.org/downloads/) and [install](https://rclone.org/install/) it according to your system from the rclone [website](https://rclone.org/).

**On CURC:** 
Rclone has been added to the Alpine module stacks. To use rclone first first load the cluster-specific SLURM job scheduler instance (Alpine in this case) from a *login node*, then ssh to a compile or compute node to access the cluster's module stack:

```
$ module load slurm/alpine 	# Load Alpine Slurm Instance
$ sinteractive 			# Access an Alpine compute node via an interactive job
$ module load rclone/1.58.0 	# Load rclone module
```

#### Step 2: Configuring rclone remote connections 

Before using rclone you must set up a configuration file that details the information about the remote server you want to transfer data to. There are two different ways of setting up your rclone configuration file:

**Create the `.conf` file manually**

If you are already familiar with rclone and the options that are available to include into your rclone configuration file, you can simply navigate to your .config folder in your home directory on and create a folder for rclone to create a file to enter these options. Example below:

```
$ cd ~/.config
$ mkdir rclone
$ cd rclone
$ vim rclone-test.conf
```
Example `rclone-test.conf` contents:
```
[my_aws_s3_bucket]
type = s3
provider = S3
access_key_id = <enter your access key here>
secret_access_key = <enter your secret key here>
region = us-west-2
location_contraint = us-west-2
acl = private
```

**Using the rclone prompt to create the .conf file**

Once rclone is available to use run the command `rclone config` to see the options to create the configuration file. This example outlines configuring a connection to an AWS S3 bucket from Research Computing. See our [Google Drive connection](../storage/petalibrary/gdrive.md) and [Local connection to RC](../storage/petalibrary/rclone.md) examples for guides on other rclone connection methods.

> _**Note: This example assumes you have an S3 bucket already set up with AWS credentials.**_

- Enter the value you wish to start with. For the purposes of this example, we are going to start with a new remote connection. So the value we will enter is 'n' and we will give a name to remote we are going to create.
```
$ rclone config
Current remotes:

Name                 Type
====                 ====
gdrive_test          drive
s3_test	    	     s3

e) Edit existing remote
n) New remote
d) Delete remote
r) Rename remote
c) Copy remote
s) Set configuration password
q) Quit config
e/n/d/r/c/s/q>n
name> aws_s3
```
- Next, you will be asked for a type of remote connection. There are *many* connection types (at the time of writing 46) - with new connection types added frequently - so please make sure to read through the options as they will likely change over time. We choose option `5` below for Amazon S3:
```
Option Storage.
Type of storage to configure.
Choose a number from below, or type in your own value.
 1 / 1Fichier
   \ (fichier)
	 ...
 5 / Amazon S3 Compliant Storage Providers including AWS, Alibaba, Ceph, Digital Ocean, Dreamhost, IBM COS, Lyve Cloud, Minio, RackCorp, SeaweedFS, and Tencent COS
   \ (s3)
	 ...
46 / seafile
   \ (seafile)
Storage> 5

```
- Next, you will specify that the config file uses S3, in this case option 1:
```
Option provider.
Choose your S3 provider.
Choose a number from below, or type in your own value.
Press Enter to leave empty.
1 / Amazon Web Services (AWS) S3
   \ (AWS)
	 ...
17 / Any other S3 compatible provider
   \ (Other)
provider> 1 
```
- Next, you will be asked for AWS credentials. At this point we are going to enter “false” because this example assumes you have your AWS S3 Accesskey/Secretkey combo which you will enter at the next step:
```
Option env_auth.
Get AWS credentials from runtime (environment variables or EC2/ECS meta data if no env vars).
Only applies if access_key_id and secret_access_key is blank.
Choose a number from below, or type in your own boolean value (true or false).
Press Enter for the default (false).
 1 / Enter AWS credentials in the next step.
   \ (false)
 2 / Get AWS credentials from the environment (env vars or IAM).
   \ (true)
env_auth> 1
```

- Your Accesskey/Secretkey combo is unique to your AWS S3 Bucket. It is important to keep these secure to keep your data protected. So your entries for each value will be something similar in the faux example below: 
```
Option access_key_id.
AWS Access Key ID.
Leave blank for anonymous access or runtime credentials.
Enter a value. Press Enter to leave empty.
access_key_id> <ACCESS-KEY>     
Option secret_access_key.
AWS Secret Access Key (password).
Leave blank for anonymous access or runtime credentials.
Enter a value. Press Enter to leave empty.
secret_access_key> <SECRET-KEY> 
```

- You will then be prompted to enter your region, here we are going to enter the value of ‘1' (you can set your appropreate region):
```
Option region.
Region to connect to.
Choose a number from below, or type in your own value.
Press Enter to leave empty.
   / The default endpoint - a good choice if you are unsure.
 1 | US Region, Northern Virginia, or Pacific Northwest.
   | Leave location constraint empty.
   \ (us-east-1)
	 ...
region> 1
```

- The next section asks for your endpoint to connect to. We are using AWS as the default endpoint, leave empty.

- Next will be a location prompt, we are going to leave this blank since we choose the default region above.

- The last step in the configuration file setup to choose the acl settings. This part is very important. There are many options for both private and public read/write/delete permissions, take extra care in choosing the value you enter. This example is going to choose the “private” option for informational purposes only. We will enter the value ‘1' hit enter/return.

```
Option acl.
Canned ACL used when creating buckets and storing or copying objects.
This ACL is used for creating objects and if bucket_acl isn't set, for creating buckets too.
For more info visit https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl
Note that this ACL is applied when server-side copying objects as S3
doesn't copy the ACL from the source but rather writes a fresh one.
Choose a number from below, or type in your own value.
Press Enter to leave empty.
   / Owner gets FULL_CONTROL.
 1 | No one else has access rights (default).
   \ (private)
   / Owner gets FULL_CONTROL.
 2 | The AllUsers group gets READ access.
   \ (public-read)
   / Owner gets FULL_CONTROL.
 3 | The AllUsers group gets READ and WRITE access.
   | Granting this on a bucket is generally not recommended.
   \ (public-read-write)
   / Owner gets FULL_CONTROL.
 4 | The AuthenticatedUsers group gets READ access.
   \ (authenticated-read)
   / Object owner gets FULL_CONTROL.
 5 | Bucket owner gets READ access.
   | If you specify this canned ACL when creating a bucket, Amazon S3 ignores it.
   \ (bucket-owner-read)
   / Both the object owner and the bucket owner get FULL_CONTROL over the object.
 6 | If you specify this canned ACL when creating a bucket, Amazon S3 ignores it.
   \ (bucket-owner-full-control)
acl> 1
```
- The following sections specify server side encryption and storage class, we will leave these as defaults.

- Next, choose ‘n' to not continue to advanced settings, 'y' to continue with the setup, and then 'q’ to quit the configuration file set up.
```
Edit advanced config?
y) Yes
n) No (default)
y/n> n
--------------------
[aws_s3]
type = s3
provider = AWS
access_key_id = <ACCESS-KEY>
secret_access_key = <SECRET-KEY> 
region = us-east-1
acl = private
--------------------
y) Yes this is OK (default)
e) Edit this remote
d) Delete this remote
y/e/d> y
Current remotes:

Name                 Type
====                 ====
gdrive_test          drive
s3_test		     s3
aws_s3	       	     s3

e) Edit existing remote
n) New remote
d) Delete remote
r) Rename remote
c) Copy remote
s) Set configuration password
q) Quit config
e/n/d/r/c/s/q> q

```

- Once you have configured your connection you can list out your rclone remote connections:
```
$ rclone listremotes
gdrive_test:
s3_test:
aws_s3:
```

- and test your connection by listing out the contents within that remote connection:
```
$ rclone ls aws_s3:
```

Congratulations! You now have a remote rclone connection set up.


#### Step 3: Basic usage commands for rclone

The basic syntax goes as follows rclone `<function> <source> <destination endpoint>:<bucket>`.

the basic functions are:
- copy
- sync
- move
- check
- mount
- serve

More information on rclone and the transfer functions can be found on [their official documentation](https://rclone.org/docs/). 

Example of a transfer via the rclone copy command from a CURC PetaLibrary allocation to your S3 bucket:
```
$ cd /pl/active/rcops
$ ls
rclonetest.csv
$ rclone copy rclonetest.csv aws_s3:testbucket/
```

## CU Large File Transfer service

OIT also offers a [file transfer
service](http://oit.colorado.edu/safe-transfer) with a web interface
which provides a good way to transfer files to collaborators. Files
are uploaded to a server and a link to download the file can be
emailed to an on- or off-campus user.

## DTN SSH Host Keys

The first time you use `scp`, `sftp`, or `ssh` with a DTN you will be
asked to verify the host key. You can refer to the keys published here
to confirm that you are connecting to a valid data transfer node.

Our DTNs support multiple key types, but only one is used (or displayed)
by your client at any given time.


Fingerprint: `256 SHA256:c8362Adxws21Si5dyqngBp1eCfvo7m/3cjT+gG6Nln4 no comment (ECDSA)`

```
ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBOA0dGntTpowZ/YdjXJzaummHbw59nTRuUQZDXjnPvZXrEtpF+Db31iM9ytWCyjHAfH8FGfKJt/MuPubNcfr1Sg=
```

Fingerprint: `256 SHA256:7o6maYG7Y3Mgw0js7GUTMb2r+FLIrcirXX1cHMOiUeo no comment (ED25519)`

```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKXkp8RQhYvNZMYGYzBpECKwwyB929enmFVz1Jm2LtkG
```

Fingerprint: `2048 SHA256:6ZOTX25SbIBaH2HU3VClSD5GpdScFkeyzl/v4uWpBGI no comment (RSA)`

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC0Pp4D+GvSYfq0GB+dAEBQcKJTkeTkJ5bQlMPzkh1N8Zs1koh3fKymmV6FuMI5chuvP6pnmWogbwaCHuarF8pMKAIiYC6QHGKkMODFeAO1V0+ZBmRpTO0PdkqNCV04Y76lCnYH+VD2/gClqenTcEVS8OD7WZYz9YhlevXFuw/4aQGCMmU0OdpKsJ1bAEGXDGrBasOXRV5uekbX6WrTYphr/ayPOjqltlTfP4/2qhh2YCQhOEH+cKGIj2Tg7asP3PB/7VFqRPKsN7nLrGCYD8tcdmvi6J0A0hmab1zgxYunxbEq+XSlN3gyT4WEy3qb1zu60IWRO4rJbrPD/uParzN3
```

## More reading

* [Indiana University Tutorial on SFTP](https://kb.iu.edu/d/akqg)
* [A Cloud Guru's Tutorial on SSH and SCP](https://acloudguru.com/blog/engineering/ssh-and-scp-howto-tips-tricks)
* [ssh.com's Tutorial on SCP and SFTP](https://www.ssh.com/ssh/sftp/)
* [Linuxize's Tutorial on Rsync](https://linuxize.com/post/how-to-use-rsync-for-local-and-remote-data-transfer-and-synchronization/)
* [Ubuntu's Documentation on Rsync](https://help.ubuntu.com/community/rsync)

