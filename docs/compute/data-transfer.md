## Data transfer

Research Computing supports several methods of file transfer. File
transfers from a local system can be done through a web-based
application called _Globus_ or through command-line tools such as
secure copy (_scp_), secure ftp (_sftp_) and _rsync_. Some
command-line tools may be unavailable on Windows, though alternative
applications exist. (e.g., WinSCP, FileZilla)

Data transfers using SSH protocols can be done via CURC login nodes or
through the CURC data transfer nodes (DTN). Transfers via the login
nodes work well for small and/or infrequent file transfers, and do not
require users to be connected to the CU network. Transfers via DTN
support all types of transfers, including large and/or frequent file
transfers and automated (passwordless) transfers.

<iframe width="560" height="315" src="https://www.youtube.com/embed/UMBD7pSE0qI" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

---


### Globus transfers

Globus file transfers are typically initiated through an interactive
web application. (Command-line access to Globus is also available, but
is beyond the scope of this document.) Globus addresses deficiencies
in traditional file-transfer mechanisms by automating large data
transfers, resuming failed transfers, distributing large transfers
across multiple servers, and brokering direct transfers between remote
computing centers.

Globus can be used on macOS, Linux, and Windows operating systems and
is RC's recommended way of transfering data.

[Sign into Globus Connect](https://www.globus.org/app/login) by
selecting "University of Colorado at Boulder" from the dropdown menu
and by logging in using your CU IdentiKey and password.

*If you're with an institution other than CU Boulder (e.g. XSEDE), your institution
 may still be available for Globus authentication using the InCommon
 federation. Look for your institution in the list and sign in with
 your local credentials. If your institution is not listed, you will
 need to [create a Globus account](https://www.globusid.org/create).*

![](https://raw.githubusercontent.com/ResearchComputing/Research-Computing-User-Tutorials/master/File-Transfers/globus-image-1.png)

Research Computing storage resources are available via multiple Globus
"endpoints." You can connect to an RC endpoint using the "endpoint"
field in the Globus web interface and searching for "CU Boulder
Research Computing". Log into the end point using your Research
Computing credentials.

You must also configure a local endpoint to transfer files to or from
your local computer. You can easily set up a Globus endpoint by
installing [Globus Connect
Personal](https://www.globus.org/globus-connect-personal)

Using the web app, connect your local workstation endpoint with the
Research Computing endpoint and transfer files easily using the Globus
GUI.

![](https://raw.githubusercontent.com/ResearchComputing/Documentation/june-updates/File-Transfers/globus-image-2new.PNG)


### Guest Collections (Globus Shared Endpoints)

PetaLibrary allocation owners can nominate a technical contact that is
able to create [Globus Guest
Collections](https://docs.globus.org/how-to/share-files/). Using a
Guest Collection (also known as a "Shared Endpoint"), You can share
any PetaLibrary file or folder that you have access to with anyone who
has a Globus account.

Detailed information on creating Guest Collections is available [at
docs.globus.org](https://docs.globus.org/how-to/share-files/).

### Filezilla

RC Users also have the option of connecting to RC via _Filezilla_. _Filezilla_ is a file transfer GUI application that can be used on Windows, Mac, and Linux. Simply [install Filezilla](https://filezilla-project.org/) and follow these steps:

1. Fill in the hostname, username, and password fields at the top of the application window. Note: RC Users have the choice of selecting a login or data transfer node. You must be on CU Boulder’s internal network if you want to access a data transfer node.

    - _Login Node_
      - Host: sftp://login.rc.colorado.edu
      - Username: your-rc-username
      - Password: your-rc-password
    - _Data Transfer Node_
      - Host: sftp://dtn.rc.int.colorado.edu
      - Username: your-rc-username
      - Password: your-rc-password

2. Press Enter. Accept your Duo 2-Factor notification. If the connection succeeds you will see your CURC filesystem on the “Remote Site” tab.
3. Navigate to the file you would like to transfer in either your local filesystem or your CURC filesystem. Right click the file and click "Upload" or "Download".

__Troubleshooting:__
- If your connection is timing out before getting a Duo notification, try increasing the _Timeout_ setting in `File->Settings`.
- If you receive the message 'Insecure FTP Notification', simply click cancel and ensure you have selected 'sftp' as your file transfer method.
- If your connection to a Data Transfer Node is not prompting a Duo notification double check you are connected to the CU Boulder Internal Network (if you are off campus VPN is required to connect to the campus internal network).


### Secure Copy (scp)

The Secure Copy utility, `scp`, can send data to and fetch data
from a remote server.

In the examples here, replace `<path-to-file>` with the path of the
file you wish to copy, `<username>` with your Research Computing
username, and `<target-path>` with the full path to the directory you
would like to send the file to.

```bash
# Copying files from a local workstation to Research Computing

scp <path-to-file> <username>@login.rc.colorado.edu:<target-path>    # using a login node
scp <path-to-file> <username>@dtn.rc.int.colorado.edu:<target-path>  # using DTN while on campus network
scp <path-to-file> <username>@dtn.rc.colorado.edu:<target-path>      # using DTN while outside campus network
```

```bash
# Copying files from Research Computing to a local workstation

scp <username>@login.rc.colorado.edu:<path-to-file> <target-path>    # using a login node
scp <username>@dtn.rc.int.colorado.edu:<path-to-file> <target-path>  # using DTN while on campus network
scp <username>@dtn.rc.colorado.edu:<path-to-file> <target-path>      # using DTN while outside campus network
``` 

Windows users can access scp through PowerShell or using a GUI
application like [WinSCP](https://winscp.net/eng/docs/protocols).

For more information on secure copy take a [look at some of our listed
resources](#more-reading) or consult the scp manual page.


### rsync

While `scp` is useful for simple file copy operations, the `rsync`
utility can be used to synchronize files and directories across two
locations. This can often lead to efficiencies in repeat-transfer
scenarios, as rsync only copies files that are different between the
source and target locations (and can even transfer partial files when
only part of a file has changed). This can be very useful in reducing
the amount of copies you may perform whem synchronizing two
datasets.

In the examples here, replace `<path-to-file>` with the path of the
file you wish to copy, `<username>` with your Research Computing
username, and `<target-path>` with the full path to the directory you
would like to send the file to.

```bash
# Synchronizing from a local workstation to Research Computing

rsync -r <path-to-directory> <username>@login.rc.colorado.edu:<target-path>    # using a login node
rsync -r <path-to-directory> <username>@dtn.rc.int.colorado.edu:<target-path>  # using DTN while on campus network
rsync -r <path-to-directory> <username>@dtn.rc.colorado.edu:<target-path>      # using DTN while outside campus network
```

```bash
# Synchronizing from Research Computing to a local workstation

rsync -r <username>@login.rc.colorado.edu:<path-to-directory> <target-path>    # using a login node
rsync -r <username>@dtn.rc.int.colorado.edu:<path-to-directory> <target-path>  # using DTN while on campus network
rsync -r <username>@dtn.rc.colorado.edu:<path-to-directory> <target-path>      # using DTN while outside campus network
```

rsync is not available on Windows by default, but [may be installed
individually](https://www.itefix.net/cwrsync) or as part of [Windows
Subsystem for Linux
(WSL)](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

For more information on rsync [check out some of our listed
resources](#more-reading) or consult the rsync manual page.


### Interactive file transfer with sftp

The `sftp` utility is an interactive alternative to `scp` that allows
multiple, bi-directional transfer operations in a single
session. Within an sftp session, a series of domain-specific file
system commands can be used to navigate, move, remove, and copy data
between a local system and Research Computing resources.

```bash
sftp <username>@login.rc.colorado.edu    # using a login node
sftp <username>@dtn.rc.int.colorado.edu  # using DTN while on campus network
sftp <username>@dtn.rc.colorado.edu      # using DTN while outside campus network
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


### Automated scp and rsync

The `scp` and `rsync` commands both allow a user to transfer files
without needing to reenter a password. All that is required is a few
simple set up procedures to prepare your local machine.
  
*These instructions only apply to local macOS and Linux
 systems. Automating file transfers from Windows is outside of the
 scope of this document.*

*You must be on a campus network or [logged into the campus
 VPN](https://oit.colorado.edu/services/network-internet-services/vpn)
 to perform passwordless data transfers to CURC.*


#### Generate a local ssh key pair

You only need to perform this step once per local system.

From a local terminal run:

```bash
ssh-keygen -t ed25519
``` 

This creates `~/.ssh/id_ed25519` and `~/.ssh/id_ed25519.pub` on your
local workstation. ("~" denotes your home directory.) `id_ed25519.pub`
is public, and can be shared with others (including Research
Computing). `id_ed25519` is private and **should never leave the
system that it was generated on.**


#### Copy the public key to CURC

You only need to perform this step once per local system.

From a local terminal run:

```bash
cat ~/.ssh/id_ed25519.pub | ssh <your-username>@login.rc.colorado.edu -T "cat >> ~/.ssh/authorized_keys"
```

Substitute your Research Computing username for `<your-username>`.

You will be required to enter your password and accept a Duo push in
order to transfer the key.

*If you have trouble running the command above, you can also just
 login to a CURC login node, open `~/.ssh/authorized_keys` and paste
 the text from `~/.ssh/id_ed25519.pub` that resides on your local
 machine.*


#### Use `rsync` or `scp` to transfer files using an ssh key

With an ssh key pair generated and configured in Research Computing,
you are ready to transfer files. Key-based transfers are only
supported via DTN. Make sure you are within the CU network and
transfer with scp or rsync.

```bash
rsync -av ./myfile.txt dtn.rc.int.colorado.edu:/projects/ralphie/myfile.txt  # using rsync

scp -v ./myfile.txt dtn.rc.int.colorado.edu:/pl/active/crdds/myfile.txt      # using scp
```


### CU Large File Transfer service

OIT also offers a [file transfer
service](http://oit.colorado.edu/safe-transfer) with a web interface
which provides a good way to transfer files to collaborators. Files
are uploaded to a server and a link to download the file can be
emailed to an on- or off-campus user.


### DTN SSH Host Keys (as of 9 February 2021)

The first time you use `scp`, `sftp`, or `ssh` with DTN you will be
asked to verify the host key. You can refer to the keys published here
to confirm that you are connecting to a valid data transfer node.

DTN supports multiple key types, but only one is used (or displayed)
by your client at any given time.

---

Fingerprint: `256 SHA256:c8362Adxws21Si5dyqngBp1eCfvo7m/3cjT+gG6Nln4 no comment (ECDSA)`

```
ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBOA0dGntTpowZ/YdjXJzaummHbw59nTRuUQZDXjnPvZXrEtpF+Db31iM9ytWCyjHAfH8FGfKJt/MuPubNcfr1Sg=
```

---

Fingerprint: `256 SHA256:7o6maYG7Y3Mgw0js7GUTMb2r+FLIrcirXX1cHMOiUeo no comment (ED25519)`

```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKXkp8RQhYvNZMYGYzBpECKwwyB929enmFVz1Jm2LtkG
```

---

Fingerprint: `2048 SHA256:6ZOTX25SbIBaH2HU3VClSD5GpdScFkeyzl/v4uWpBGI no comment (RSA)`

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC0Pp4D+GvSYfq0GB+dAEBQcKJTkeTkJ5bQlMPzkh1N8Zs1koh3fKymmV6FuMI5chuvP6pnmWogbwaCHuarF8pMKAIiYC6QHGKkMODFeAO1V0+ZBmRpTO0PdkqNCV04Y76lCnYH+VD2/gClqenTcEVS8OD7WZYz9YhlevXFuw/4aQGCMmU0OdpKsJ1bAEGXDGrBasOXRV5uekbX6WrTYphr/ayPOjqltlTfP4/2qhh2YCQhOEH+cKGIj2Tg7asP3PB/7VFqRPKsN7nLrGCYD8tcdmvi6J0A0hmab1zgxYunxbEq+XSlN3gyT4WEy3qb1zu60IWRO4rJbrPD/uParzN3
```

### More reading

* [Indiana University Tutorial on SFTP](https://kb.iu.edu/d/akqg)
* [Linux Academy's Tutorial on SSH and SCP](https://linuxacademy.com/blog/linux/ssh-and-scp-howto-tips-tricks/)
* [ssh.com's Tutorial on SCP and SFTP](https://www.ssh.com/ssh/sftp/)
* [Linuxize's Tutorial on Rsync](https://linuxize.com/post/how-to-use-rsync-for-local-and-remote-data-transfer-and-synchronization/)
* [Ubuntu's Documentation on Rsync](https://help.ubuntu.com/community/rsync)
