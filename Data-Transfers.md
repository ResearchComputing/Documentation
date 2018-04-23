## Table of Contents
- [Overview](#overview)
- [Video Tutorial](#video-tutorial)
- [Globus](#globus)
- [SSH Protocols](#ssh-protocols)

## Overview

Research Computing supports several methods of file transfers onto Summit. File transfers from a local machine can be done via two ways: Through [Globus](https://www.globus.org/) or through SSH protocols.  

## Video Tutorial
[![Data-Transfer-Video](https://raw.githubusercontent.com/ResearchComputing/Research-Computing-User-Tutorials/master/File-Transfers/file-transf-vid.jpg)](https://www.youtube.com/watch?v=BGgOVBh6rQY)

## Globus

On Globus, file transfers are handled through an interactive web application. Globus addresses deficiencies in secure copy requests by automating large data transfers, resuming failed transfers, and simplifying the implementation of high performance transfers between computing centers.  

[Sign into Globus Connect](https://www.globus.org/app/login) by selecting "University of Colorado at Boulder" using your CU IdentiKey and password.  
* If you're with an institution outside of the University of Colorado at Boulder that is registered with Globus, sign in with your appropriate credentials.
* If you're institution is not registered with Globus, you will need to [make an account](https://www.globusid.org/create) with Globus.

<br>

![alt text](https://raw.githubusercontent.com/ResearchComputing/Research-Computing-User-Tutorials/master/File-Transfers/globus-image-1.png)

Files can be transferred easily by setting up a Globus endpoint on your local workstation.
* You can easily set up a Globus endpoint by installing [Globus Connect Personal](https://www.globus.org/globus-connect-personal) on your local machine.  
Using the web app, connect your local workstation endpoint with the Research Computing endpoint and transfer files easily using the Globus GUI.  

<br>

![alt text](https://raw.githubusercontent.com/ResearchComputing/Research-Computing-User-Tutorials/master/File-Transfers/globus-image-2.png)

## SSH Protocols

SSH protocols also provide two additional means of file transfers onto Research Computing resources.

### Secure Copy (SCP)

The Secure Copy protocol or `scp` allows users to send and receive data to the server remotely via a terminal command. The command appears a so:

#### Command to copy files from a local workstation to research computing resources
```bash

# Replace source_file with the file you wish to copy

# Replace rc_username with your research computing username

# Replace target_directory with the directory you would like 
# to send the file to within your rc home directory.  

scp source_file rc_username@login.rc.colorado.edu:~/target_directory
```

#### Command to copy files from research computing resources to a local workstation

```bash

# Replace source_file with the file you wish to copy

# Replace rc_username with your research computing username

# Replace source_directory with the directory you would like
# to copy from within your rc home directory.  

scp rc_username@login.rc.colorado.edu:~/source_directory/source_file .
```
For more information on secure copy take a look at some of our listed resources or consult the man page with the command:
```bash
man scp
```

**Resources:**  
[Indiana University Tutorial on SCP](https://kb.iu.edu/d/agye)  
[Linux Academy's Tutorial on SSH and SCP](https://linuxacademy.com/blog/linux/ssh-and-scp-howto-tips-tricks/)  
[ssh.com's Tutorial on SCP and SFTP](https://www.ssh.com/ssh/sftp/)

### Secure File Transfer Protocol (SFTP)

The Secure File Transfer Protocol is an interactive terminal solution to transfer data to and from research computing resources. SFTP works much like moving files in a terminal, we use a series of file system commands to navigate, move, remove, and copy information from a client's personal machine to research computing resources. To invoke SFTP type the command:
```bash
sftp rc_username@login.rc.colorado.edu
```

We can then use various commands to traverse and manipulate both file systems. A list of commands are listed below:

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

**Resources:**  
[Indiana University Tutorial on SFTP](https://kb.iu.edu/d/akqg)  
[ssh.com's Tutorial on SCP and SFTP](https://www.ssh.com/ssh/sftp/)  