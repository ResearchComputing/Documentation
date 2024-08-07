# Files application 

The **Files** application allows users to easily make modifications to directories and files across the CURC filesystem. All [filesystems](../compute/filesystems.md) accessible through the login nodes (e.g `/home`, `/projects`, `/scratch/alpine` , and `/pl`) will be available in this application. To access your directories, select the **Files** tab at the top of the Open OnDemand page (pictured left), this will open up a drop-down menu where you can select the directory you want to navigate to. Once a directory is selected, the full **Files** application will open up (pictured right). 

```{eval-rst}
.. figure:: ./OnDemand/files_app_main_drop_down.png
   :align: center
```

```{important}
The **Files** application should not be used if you are downloading or uploading files larger than 1 GB in size. Please use Globus (a GUI application) or another [data transfer technique](../compute/data-transfer.md) for large file transfers. These alternative methods are specifically designed to handle these types of workloads. 
```

## Files application features

From the picture provided above, one can see that there are several convenient features provided in the **Files** application. These functionalities are as follows: 
- `_> Open in Terminal` -- Opens up a [terminal application](./terminal_app.md) in the directory you are in, within the **Files** application.
- `New File` -- Will open up a pop-up menu where a user can enter the file name they would like to create. This file will be placed in the current directory. 
- `New Directory` -- Will open up a pop-up menu where a user can enter the directory name they would like to create. This directory will be placed in the current directory.
- `Upload` -- Opens a pop-up menu where users can drag and drop or select a file on their system. Once an item is provided, this will automatically upload the file to the directory you are in, within the **Files** application. 
- `Download` -- For those items selected within the **Files** application, this button will automatically download those items to your local machine. 
- `Delete` -- Deletes the items selected within the **Files** application. 
- `Copy/Move` -- Allows users to copy or move data. To use this application, select items you would like to move or copy. Next, click the `Copy/Move` button. This will open a box on the left (pictured below). You may then click the different directories presented in this box to specify where you would like to move or copy the data. In the provided picture we are copying or moving data to **"/scratch/alpine/breyes@xsede.org"**. When the directories are selected, the **Files** application to the right will update and you may even select directories within the directory you initially selected. 
```{eval-rst}
.. figure:: ./OnDemand/files_app_copy_move.png
   :align: center
```
- Renaming, downloading, and deleting files or directories can be done from the drop-down menu next to the data. Additionally, one can view and edit files using this drop-down menu. The menu can be found by selecting the three vertical dots next to the data (pictured below). 
```{eval-rst}
.. figure:: ./OnDemand/files_app_view_edit.png
   :align: center
```

```{note}
For additional documentation on the **Files** application visit [OSC's File Transfer and Management help page](https://www.osc.edu/resources/online_portals/ondemand/file_transfer_and_management).
```
