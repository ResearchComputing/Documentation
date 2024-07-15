# Adding Petalibrary to a Local Machine

Users with Petalibrary allocations may access and transfer files to/from their local desktop workstatation within the CU internal network without needing to formally tranfer files via traditional methods such as `scp`, `sftp` `rsync` or `Globus`. This form of data access is referred to as _mounting_ and can be done on any operating system in a variety of ways.

## SMB mounting to Petalibrary

SMB (Secure Message Block) is a cross platform network sharing protocol that allows users to mount their Petalibrary allocations onto their local machines. SMB is supported on all major operating systems and all it takes to mount is a simple connection to CURC's network.

**You must be on the CU Boulder VPN to establish an SMB mount, even if you are already on a campus network.**

**Note:** SMB support for individual Petalibrary allocations is limited at the moment and requires additional setup from a system administrator. Please contact rc-help@colorado.edu if you’d like to set up SMB support with your Petalibrary Allocation.

### Mounting with SMB on Mac

Mounting on Mac is a relatively simple procedure and can be accomplished in a few steps:
First, navigate to Finder and click “Connect to Server” under the “Go” menu:


![](https://raw.githubusercontent.com/ResearchComputing/Documentation/dev/Petalibrary/Mounting/smbmac1.png)


In the 'Server Address' field, provide the hostname to a RC's internal server appended wity your Petalibrary allocation. RC will provide you the hostname needed when requesting access to SMB.
```
smb://<RC-provided-hostname>/<your-pl-allocation>
```

![](https://raw.githubusercontent.com/ResearchComputing/Documentation/dev/Petalibrary/Mounting/smbmac2.png)


You will be prompted for your RC Username and Password. Type in the required information and click Connect. Accept your Duo notification and you Petalibrary Allocation will be mounted. 



### Mounting with SMB on Windows

Mounting on Windows is a little more involved then on a Mac or Linux counterpart. First ensure you are connected to the CU VPN. Navigate to `This PC` and click on `Computer` -> `Add a network location`.

![](https://raw.githubusercontent.com/ResearchComputing/Documentation/dev/Petalibrary/Mounting/smb1.PNG)

This will bring up a setup utility. Continue through the prompt, selecting `Choose a custom network location` when prompted. This will bring up a text field asking for an Internet or Network Address. Provide the hostname to a RC's internal server appended with your Petalibrary allocation. RC will provide you the hostname needed when requesting access to SMB.
```
\\<RC-provided-hostname>\<your-pl-allocation>
```
And click next.

![](https://raw.githubusercontent.com/ResearchComputing/Documentation/dev/Petalibrary/Mounting/smb2.PNG)

Lastly you will be prompted to provide your credentials. Type your credentials as such:

```
Username: AD\<your-rc-username>
Password: <your-rc-password>
```

![](https://raw.githubusercontent.com/ResearchComputing/Documentation/dev/Petalibrary/Mounting/smb3.PNG)


## `sshfs` mounting to Petalibrary

Sshfs provides another solution in mounting your Petalibrary allocation to a local machine. Like SMB you will need to be connected to CU's internal network to access this utility. Sshfs is primarily supported on Unix based operating systems but can be run on a Windows operating system with a bit more effort. 

### `sshfs` on Mac
Sshfs on Mac can easily be done with the installation of fuse and the sshfs package. To install the package simply download both [from the macFuse homepage and follow the provided install instructions.](https://osxfuse.github.io/)

After installing both simply open a terminal and navigate to your desired mount location. Create a directory to be your mountpoint and run the command 

```
sshfs <your-rc-username>@dtn.rc.colorado.edu:/pl/active/<your-pl-directory> <local-directory>
```

You will be prompted for your password after execution. Type your password and accept the duo prompt.
Your selected directory will now be mounted to your Petalibrary allocation.

### `sshfs` on Windows
Sshfs on Windows comes from the installation of 2 applications. First install the application sshfs-win: Installation instructions and files [can be found here.](https://github.com/billziss-gh/sshfs-win)

Next install the sshfs graphical user interface (GUI) frontend. Installation instructions and files [can be found here.](https://github.com/evsar3/sshfs-win-manager)

Once both applications are installed, run the application “sshfs-win manager”. A window will pop up showing you a list of all sshfs connections you have saved. 

![](https://raw.githubusercontent.com/ResearchComputing/Documentation/dev/Petalibrary/Mounting/sshfsmenu.PNG)

Click on `Add a connection`. This will bring up a menu outlining the parameters for your mount. Give the connection a name and set the `IP/Host` to dtn.rc.colorado.edu. Add your RC username for `User` field and click the dropdown menu on `Password` and select: *Password (ask on connect)*. Lastly set `PATH` to `/pl/active/<your-petalibrary-space>` and select a drive letter.

![](https://raw.githubusercontent.com/ResearchComputing/Documentation/dev/Petalibrary/Mounting/sshfs.PNG)

Once this is done click the connect button. You will be prompted for a password. Type in your password and accept your two-factor authentication to be mounted. You will now see your selected drive letter mounted to your Petalibrary allocation in “This PC.”

#### Troubleshooting
- The sshfs-win manager application may point to the incorrect sshfs binary by default. You can correct this in the "Settings" menu and adding the correct path to the application.
- You may run into an issue where sshfs fails to wait for your Duo response. To correct this, open the "Settings" menu and increase the 'Process Timeout' field.

