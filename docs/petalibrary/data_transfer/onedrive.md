# Data Transfer to/from OneDrive


(tabset-ref-ucb-pl-onedrive-types)=
`````{tab-set}
:sync-group: tabset-ucb-pl-onedrive-types

````{tab-item} Globus
:sync: tabset-ucb-pl-onedrive-types-globus

### Step 1: Log into the Globus Web App
Visit [https://app.globus.org](https://app.globus.org) and log in with your Colorado.edu credentials

```{image} ../images_and_html/Globus_Login.png
:alt: An image of the Globus login page, with "University of Colorado at Boulder" selected in the drop-down menu under "Use your existing organizational login". A blue "Continue" button is available just below the drop-down menu box.
```

### Step 2: Open your OneDrive
In the Collection Search, enter: "OneDrive CU Boulder" - this should show your OneDrive contents if you are logged in. You may need to authenticate with your OneDrive account.

```{image} ../images_and_html/onedrivesearch.png
:alt: An image of the "Collection Search" pane of the Globus File Manager. "onedrive CU" is typed into the "Collection" search box, and the collection result "OneDrive CU Boulder" is visible below the search box.
```

### Step 3: Open CURC (right pane)
Click the 2nd option in the Panel selection on the top right of the page to enter split view. In the Collection Search (right pane), enter: "CU Boulder Research Computing"

* You'll be asked to log in using your CURC Credentials by selecting `Authenticate`.

```{image} ../images_and_html/splitview.png
:alt: An image of the Split View of the Globus File Manager, with the "OneDrive CU Boulder" collection open in the left pane, and "CU Boulder Research Computing" collection open in the right pane. Messages about authentication being required are visible in both endpoints, with no files or folders yet visible.
```

* Once authenticated, you should see your CURC home directory - to access Petalibrary click "Up One Directory" and then select `/pl` and proceed to your allocation. 

```{image} ../images_and_html/Globus_CURC_Collection.png
:alt: A closer view of the right side of the collection and file path boxes in the Globus Split View. The collection is "CU Research Computing", and the current file path is "/~/", the home directory.
```

### Step 4: Select files/folders from OneDrive to be transferred and initiate the transfer
* In the left pane, select the file or folder you'd like to transfer and click Start - this will initiate a Globus Transfer job.

```{image} ../images_and_html/Globus_Initiate_Transfer_OneDrive.png
:alt: A closer view of the left side of the Split View in Globus, showing a folder selected, and a blue "Start" button in the middle to initiate data transfer to the location shown on the right side of the Split View. The right side is not visible in this image.
```

* View progress of your transfer under the Activity tab in the Globus App

```{image} ../images_and_html/Globus_Activity_OneDrive.png
:alt: An image of the transfer status page under the "Activity" tab in Globus, showing a successful transfer from OneDrive to CU Boulder Research Computing. Information is shown about the transfer, including a name, Task ID, status, speed, and size metrics for the transfer.
```

````

````{tab-item} Rclone
:sync: tabset-ucb-pl-onedrive-types-rclone

### Step 1: Login to a compile node on Alpine

* Login to Alpine
* Load module Slurm, then start a compile job, then load module rclone
	```
	$ module load slurm
	$ acompile
	$ module load rclone
	```
* To test, run `rclone --version` at your prompt; if the software is installed a version number will be reported back to you, similar to:

	```
	$ rclone --version
	rclone v1.58.0
	```

### Step 2: configure OneDrive remote configuration

The steps below are also outlined in the [Rclone Documentation for OneDrive](https://rclone.org/onedrive/). We only list the critical steps. If a step is left out, assume you can select the default setting.

* Type `rclone config` to create a new profile for transferring files between OneDrive and PetaLibrary
* When prompted for whether to configure a “new” or “existing” profile, type `n` for "new remote"
* When prompted to name the new profile provide any descriptive name you like (e.g., `onedrive_johndoe_cu`)
* When prompted for the type of storage to configure, select the number of the option for "Microsoft OneDrive" (e.g., the number is "28" for _rclone v1.58.0_)
* When prompted for Client ID, leave the field blank
* When prompted for Client Secret, leave the field blank
* When prompted choose national cloud region for OneDrive, select the number of the option for "Microsoft Cloud Global (global)" (e.g., the number is "1" for _rclone v1.58.0_)
* When prompted with "Edit Advanced config?”, choose "n" for no (default). 
* When prompted with "Use Auto config?”, choose "n" for no (default). 
* You will then need to use your local machine's terminal to run 
	```
	$ rclone authorize "onedrive"
	```
	This will open a window in your your browser (you may be asked to authenticate to your Microsoft account). You will then be asked to allow `Rclone` to access the files in your `onedrive`. Complete this step to grant access.  If successful you'll receive a "success" message. 
* When prompted for Type of connection. Choose the appropriate answer, most likely "OneDrive Personal or Business (onedrive)" (e.g., the number is "1" for _rclone v1.58.0_)
* When prompted for the drive you want to use, choose the appropriate answer.
* When prompted asking if that drive is OK, choose the appropriate answer.
* Finally, you will be prompted to review the configuration and confirm whether it is okay. If everything looks okay, choose `yes` (default)
* Now type, `q` to quit the configuration. 

#### Now test your OneDrive remote!

On the Alpine compile node type:
```bash
$ rclone ls onedrive_johndoe_cu:
```
If this step fails, your OneDrive remote is not configured properly. Try reconfiguring your OneDrive remote again or submit a [support request form](https://colorado.service-now.com/req_portal?id=ucb_sc_rc_form) for assistance.

### Step 3: Create your PetaLibrary remote configuration

See instructions for creating an [Rclone remote configuration for PetaLibrary](./rclone.md)
````

`````
