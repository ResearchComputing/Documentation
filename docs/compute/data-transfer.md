## Data transfer

Research Computing supports several methods of file transfers onto
Summit. File transfers from a local machine can be done via two ways:
Through [Globus](https://www.globus.org/) or through SSH protocols.

<iframe width="560" height="315" src="https://www.youtube.com/embed/UMBD7pSE0qI" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

---

### Globus

On Globus, file transfers are handled through an interactive web
application. Globus addresses deficiencies in secure copy requests by
automating large data transfers, resuming failed transfers, and
simplifying the implementation of high performance transfers between
computing centers.

[Sign into Globus Connect](https://www.globus.org/app/login) by
selecting "University of Colorado at Boulder" from the dropdown menu
and by logging in using your CU IdentiKey and password.

* If you're with an institution outside of the University of Colorado
  at Boulder that is registered with Globus, sign in with your
  appropriate credentials.

* If your institution is not registered with Globus, you will need to
  [make an account](https://www.globusid.org/create) with Globus.

![](https://raw.githubusercontent.com/ResearchComputing/Research-Computing-User-Tutorials/master/File-Transfers/globus-image-1.png)

Files can easily be transferred from Summit to your local computer with Globus.

* Research Computing resources are installed with a Globus
  endpoint. You can connect to this endpoint by clicking the
  "endpoint" field and searching for the endpoint: `CU Boulder
  Research Computing`. Log into the end point by using your Research
  computing credentials.

* Your local computer must also have an endpoint. You can easily set
  up a Globus endpoint by installing [Globus Connect
  Personal](https://www.globus.org/globus-connect-personal) on your
  local machine.

Using the web app, connect your local workstation endpoint with the
Research Computing endpoint and transfer files easily using the Globus
GUI.

![](https://raw.githubusercontent.com/ResearchComputing/Research-Computing-User-Tutorials/master/File-Transfers/globus-image-2.png)

### Secure Copy `scp`

The Secure Copy protocol or `scp` allows users to send and receive
data to the server remotely via a terminal command. The command
appears as:

```bash
# Command to copy files from a local workstation to Research Computing resources

# Replace <path-to-file> with the path of the file you wish to copy
# Replace <username> with your Research Computing username
# Replace <target-path> with the full path to the directory you would like to send the file to.

scp <path-to-file> <username>@login.rc.colorado.edu:<target-path>
```

```bash
# Command to copy files from Research Computing resources to a local workstation

# Replace <path-to-file> with the path of the file you wish to copy
# Replace <username> with your Research Computing username
# Replace <target-path> with the full path to the directory you would like to send the file to.

scp <username>@login.rc.colorado.edu:<path-to-file> <target-path>
```

For more information on secure copy take a [look at some of our listed
resources](#more-reading) or consult the scp man page.

### Using `rsync` on Summit
Another popular file transfer utility that can be used is the `rsync` command. While similar in function to scp, the major differences between rsync and scp are how the  commands approach data transfer. **Scp will bindly copy files from one server to another. Rsync aims to synchronize 2 files/directories to be the same.** Because of this approach, rsync only copies files that are different from the source and target directories. This can be very useful in reducing the amount of copies you may perform whem synchronizing two datasets. On a local machine, the command is called as follows:

```bash
# Command to synchronizing from a local machine to Research Computing resources

# Replace <path-to-file> with the path of the file you wish to copy
# Replace <username> with your Research Computing username
# Replace <target-path> with the full path to the directory you would like to send the file to.

rsync -r <path-to-directory> <username>@login.rc.colorado.edu:<target-path>
```

```bash
# Command to synchronizing from Research Computing resources to a local machine

# Replace <path-to-file> with the path of the file you wish to copy
# Replace <username> with your Research Computing username
# Replace <target-path> with the full path to the directory you would like to send the file to.

rsync -r <username>@login.rc.colorado.edu:<path-to-directory> <target-path>
```

For more information on rsync [check out some of our listed resources](#more-reading) or consult the rsync man page.

### Secure File Transfer Protocol: `sftp`

The Secure File Transfer Protocol is an interactive terminal solution
to transfer data to and from research computing resources. SFTP works
much like moving files in a terminal, we use a series of file system
commands to navigate, move, remove, and copy information from a
client's personal machine to research computing resources. To invoke
SFTP type the command:

```bash
sftp <username>@login.rc.colorado.edu
```

We can then use various commands to traverse and manipulate both file
systems. A list of commands are listed below:

Command | Function | Example
--------|----------|----------
cd | Changes the directory of the remote computer | cd remote_directory
lcd | Changes the directory of the local computer | lcd local_directory
ls | Lists the contents of the remote directory | ls
lls | Lists the contents of the local directory | lls
pwd | Prints working directory of the remote computer | pwd
lpwd | Prints working directory of the local computer | lpwd
get | Copies a file from the remote directory to the local directory | get remote_file
put | Copies a file from the local directory to the remote directory | put local_file
exit | Closes the connection to the remote computer and exits the program | exit
help | Displays application information on using commands | help

### Passwordless `scp` and `rsync`

The `scp` and `rsync` commands both allow a user to transfer files without needing to reenter a password. All that is required is a few simple set up procedures to prepare your local machine.  
  
*Note: Passwordless data transfers are only available for Mac and Linux users. You must be [logged into the campus VPN](https://oit.colorado.edu/services/network-internet-services/vpn) to perform passwordless data transfers to CURC*

#### Generate an ssh keypair on your local laptop/desktop

You only need to perform this step once. From a local terminal run:

```
ssh-keygen -t ed25519
``` 

This will create `~/.ssh/id_ed25519` and `~/.ssh/id_ed25519.pub` on your local machine (_note: the "~" denotes your home directory_). 

#### Copy the public key to ~/.ssh/authorized_keys on a CURC login node 

You only need to perform this step once. From a local terminal run:

```
cat ~/.ssh/id_ed25519.pub | ssh <your-username>@login.rc.colorado.edu -T "cat >> ~/.ssh/authorized_keys"
```
...where you should substitute your CURC username for `<your-username>`; you will be required to enter your password and accept a Duo push in order to transfer the key.

_Note: If you have trouble running the command above, you can also just login to a CURC login node, open `~/.ssh/authorized_keys` and paste the text from `~/.ssh/id_ed25519.pub` that resides on your local machine._

#### Use `rsync` or `scp` to transfer files without a password

Now you are ready to transfer files. Make sure you are logged on campus or logged into CU VPN and run rsync or scp. Examples:

User "ralphie" employs _rsync_ to tranfer `myfile.txt` to `/projects/ralphie` on CURC:

```
rsync -av ./myfile.txt dtn-new-data.rc.int.colorado.edu:/projects/ralphie/myfile.txt
```

User "ralphie" employs _scp_ to transfer `myfile.txt` from Ralphie's local machine to a PetaLibrary allocation called "crdds" that Ralphie has access to:

```
scp ./myfile.txt dtn-new-data.rc.int.colorado.edu:/pl/active/crdds/myfile.txt
```


### Other Options

OIT also offers a file transfer service with a web interface which
provides a good way to transfer files to collaborators. Files are
uploaded to a server and a link to download the file can be emailed to
an on, or off-campus, user: [http://oit.colorado.edu/safe-transfer](http://oit.colorado.edu/safe-transfer)

### DTN SSH Host Keys

```
ecdsa-sha2-nistp256
AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBOA0dGntTpowZ/YdjXJzaummHbw59nTRuUQZDXjnPvZXrEtpF+Db31iM9ytWCyjHAfH8FGfKJt/MuPubNcfr1Sg=
```

```
ssh-ed25519
AAAAC3NzaC1lZDI1NTE5AAAAIKXkp8RQhYvNZMYGYzBpECKwwyB929enmFVz1Jm2LtkG
```

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC0Pp4D+GvSYfq0GB+dAEBQcKJTkeTkJ5bQlMPzkh1N8Zs1koh3fKymmV6FuMI5chuvP6pnmWogbwaCHuarF8pMKAIiYC6QHGKkMODFeA
O1V0+ZBmRpTO0PdkqNCV04Y76lCnYH+VD2/gClqenTcEVS8OD7WZYz9YhlevXFuw/4aQGCMmU0OdpKsJ1bAEGXDGrBasOXRV5uekbX6WrTYphr/ayPOjqltlTfP4/2qhh2YCQhOEH+
cKGIj2Tg7asP3PB/7VFqRPKsN7nLrGCYD8tcdmvi6J0A0hmab1zgxYunxbEq+XSlN3gyT4WEy3qb1zu60IWRO4rJbrPD/uParzN3
```

### More reading

* [Indiana University Tutorial on SFTP](https://kb.iu.edu/d/akqg)
* [Linux Academy's Tutorial on SSH and SCP](https://linuxacademy.com/blog/linux/ssh-and-scp-howto-tips-tricks/)
* [ssh.com's Tutorial on SCP and SFTP](https://www.ssh.com/ssh/sftp/)
* [Linuxize's Tutorial on Rsync](https://linuxize.com/post/how-to-use-rsync-for-local-and-remote-data-transfer-and-synchronization/)
* [Ubuntu's Documentation on Rsync](https://help.ubuntu.com/community/rsync)
