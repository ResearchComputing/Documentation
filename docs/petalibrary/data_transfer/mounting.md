# Mounting on a Local Machine

Users with Petalibrary allocations may access and transfer files to/from their local desktop computer within the CU internal network without needing to formally tranfer files via traditional methods such as `scp`, `sftp` `rsync` or `Globus`. This form of data access is referred to as _mounting_ and can be done on any operating system via `SMB` or `sshfs`.

(tabset-ref-ucb-pl-mounting-types)=
`````{tab-set}
:sync-group: tabset-ucb-pl-mounting-types

````{tab-item} SMB
:sync: tabset-ucb-pl-mounting-types-smb

SMB (Secure Message Block) is a cross platform network sharing protocol that allows users to mount their PetaLibrary allocations onto their local machines. SMB is supported on all major operating systems and all it takes to mount is a simple connection to CURC's network.

```{note}
SMB support for individual PetaLibrary allocations is limited to CU Boulder customers and requires additional setup from a system administrator. You must be on the CU Boulder VPN to establish an SMB mount, even if you are already on a campus network. Please submit a [support request form](https://colorado.service-now.com/req_portal?id=ucb_sc_rc_form) if you’d like to set up SMB support with your PetaLibrary Allocation.
```

### Mounting with SMB on Mac

Mounting on Mac is a relatively simple procedure and can be accomplished in a few steps:
First, navigate to Finder and click “Connect to Server” under the “Go” menu:

```{image} ../images_and_html/smbmac1.png
:alt: An image of the "Go" menu from the menu bar of Finder on a Mac. The bottom option, "Connect to Server..." is highlighted in blue.
```

In the `Server Address` field, provide the hostname to a RC's internal server appended with your PetaLibrary allocation. RC will provide you the hostname needed when requesting access to SMB.
```
smb://<RC-provided-hostname>/<your-pl-allocation>
```

```{image} ../images_and_html/smbmac2.png
:alt: An image of the macOS "Connect to Server" dialog box, showing the SMB hostname typed into the "Server Address" box, an empty list of "Favorite Servers", and the Connect button highlighted in blue. The example SMB hostname is "smb://pl-enc04.rc.int.colorado.edu/rcops_samba".
```

You will be prompted for your RC username and password. Type in the required information and click `Connect`. Accept your Duo notification and your PetaLibrary Allocation will be mounted. 

### Mounting with SMB on Windows

Mounting on Windows is a little more involved than on a Mac or Linux system. First, ensure you are connected to the CU VPN. Navigate to `This PC` and click on `Computer` -> `Add a network location`.

```{image} ../images_and_html/smb1.png
:alt: An image of the "This PC" window in the Windows File Explorer. The "Computer" tab at the top is highlighted, showing the button "Add a network location", among other options.
```

This will bring up a setup utility. Continue through the prompt, selecting `Choose a custom network location` when prompted. This will bring up a text field asking for an Internet or Network Address. Provide the hostname to a RC's internal server appended with your Petalibrary allocation. RC will provide you the hostname needed when requesting access to SMB.
```
\\<RC-provided-hostname>\<your-pl-allocation>
```
And click `next`.

```{image} ../images_and_html/smb2.png
:alt: An image of the "Add Network Location" wizard in Windows, with the SMB hostname typed into the box labeled "Internet or network address:", and the "Next" button highlighted at the bottom-right of the window, next to the "Cancel" button. The example SMB hostname is "\\pl-enc04.rc.int.colorado.edu\rcops_samba".
```

Lastly you will be prompted to provide your credentials. Type your credentials as follows:

```
Username: AD\<your-rc-username>
Password: <your-rc-password>
```

```{image} ../images_and_html/smb3.png
:alt: An image of the "Enter network credentials" dialog box in Windows, showing a username and password field, and "OK" and "Cancel" options.
```

````

````{tab-item} sshfs
:sync: tabset-ucb-pl-mounting-types-sshfs

Use of `sshfs` provides an alternate solution for mounting your Petalibrary allocation to a local machine. Like SMB you will need to be connected to CU's internal network to access this utility. The `sshfs` utility is primarily supported on Unix-based operating systems, but can be run on a Windows operating system with a bit more effort. 

### sshfs on Mac
Enabling `sshfs` on Mac is done by installing the fuse and the sshfs packages. To install the packages simply download both [from the macFuse homepage and follow the provided install instructions.](https://osxfuse.github.io/)

After installing both simply open a terminal and navigate to your desired mount location. Create a directory to be your mountpoint and run the command 

```
sshfs <your-rc-username>@dtn.rc.colorado.edu:/pl/active/<your-pl-directory> <local-directory>
```

You will be prompted for your password after execution. Type your password and accept the duo prompt. Your selected directory will now be mounted to your Petalibrary allocation.

### sshfs on Windows
Enabling `sshfs` on Windows requires the installation of 2 applications. First install the application sshfs-win: [see installation instructions and files here.](https://github.com/billziss-gh/sshfs-win)

Next install the sshfs graphical user interface (GUI) frontend. [see installation instructions and files here.](https://github.com/evsar3/sshfs-win-manager)

Once both applications are installed, run the application `sshfs-win manager`. A window will pop up showing you a list of all sshfs connections you have saved. 

```{image} ../images_and_html/sshfsmenu.png
:alt: An image of the "SSHFS-Win Manager" application on Windows, showing an empty list of servers, a button in the top-right to "Add connection", and buttons in the bottom-right for "Settings" and "About". The "Edit mode" and "Delete mode" buttons below "Add connection" are greyed out and unavailable.
```


Click on `Add a connection`. This will bring up a menu outlining the parameters for your mount. Give the connection a name and set the `IP/Host` to `dtn.rc.colorado.edu`. Add your RC username for `User` field and click the dropdown menu on `Password` and select: *Password (ask on connect)*. Lastly set `PATH` to `/pl/active/<your-petalibrary-space>` and select a drive letter.

```{image} ../images_and_html/sshfs.png
:alt: An image of the "Add Connection" dialog box in the SSHFS-Win Manager application for Windows. The "Basic" tab is selected, and the "Advanced" tab is not open. Input boxes for "Name", "IP/Host", "Port", "User", "Authentication Method", "Path", and "Drive Letter" are shown, with "Cancel" and "Save" buttons in the bottom-right. Suggested values for the input boxes are provided in the section "sshfs on Windows". 
```


Once this is done click the `connect` button. You will be prompted for a password. Type in your password and accept the Duo two-factor authentication to be mounted. You will now see your selected drive letter mounted to your Petalibrary allocation in `This PC`.

#### Troubleshooting
- The sshfs-win manager application may point to the incorrect `sshfs` binary by default. You can correct this in the "Settings" menu and adding the correct path to the application.
- You may run into an issue where `sshfs` fails to wait for your Duo response. To correct this, open the `Settings` menu and increase the `Process Timeout` field.

````

`````
