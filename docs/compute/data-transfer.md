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

![](https://raw.githubusercontent.com/ResearchComputing/Documentation/june-updates/File-Transfers/globus-image-2new.PNG)

### Globus Shared Endpoints
With Globus you can share files with users outside of your organization by creating shared endpoints. You can share any file/folder that you have access to.  The user you are sharing with has to have a Globus account.

To learn how to setup a shared endpoint:
[Globus Shared Endpoint Documentation](https://docs.globus.org/how-to/share-files/)

### Secure Copy (SCP)

The Secure Copy protocol or `scp` allows users to send and receive
data to the server remotely via a terminal command. The command
appears as:

```bash
# Command to copy files from a local workstation to research computing resources

# Replace <path-to-file> with the file you wish to copy

# Replace <username> with your Research Computing username

# Replace <target_directory> with the full path to the directory you would like
# to send the file to.

scp <path-to-file> <username>@login.rc.colorado.edu:<target-path>
```

```bash
# Command to copy files from research computing resources to a local workstation

# Replace <path-to-file> with the file you wish to copy

# Replace <username> with your Research Computing username

# Replace <target_directory> with the full path to the directory you would like
# to send the file to.

scp <username>@login.rc.colorado.edu:<path-to-file> <target-path>
```

For more information on secure copy take a look at some of our listed
resources or consult the man page with the command:

```bash
man scp
```

### Secure File Transfer Protocol (SFTP)

The Secure File Transfer Protocol is an interactive terminal solution
to transfer data to and from Research Computing resources. SFTP works
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
