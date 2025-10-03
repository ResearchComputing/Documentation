# Data Transfer

There are numerous ways to transfer data to/from PetaLibrary. Select the option below that best serves your needs. 

```{toctree}
:maxdepth: 1

./data_transfer/mounting.md

```
* Documentation on use of `SMB` for mounting PetaLibrary as a local volume.
* Documentation on use of `sshfs` for mounting PetaLibrary as a local volume.

```{toctree}
:maxdepth: 1

./data_transfer/rclone.md

```
* Documentation on using `Rclone` to backup local data.
* Additional documentation on scheduling recurring backups to PetaLibrary.

```{toctree}
:maxdepth: 1

./data_transfer/gdrive.md

```
* Specific documentation on using `Rclone` to transfer data from Google Drive to PetaLibrary.

```{toctree}
:maxdepth: 1

./data_transfer/onedrive.md

```
* Specific documentation on using `Rclone` to transfer data from Onedrive to PetaLibrary.
* Additional documentation on using Globus to transfer data from Onedrive to PetaLibrary.

```{toctree}
:maxdepth: 1

./data_transfer/synology.md

```
* Documentation on transferring data from a local Synology network attached storage device to PetaLibrary.
* additional documentation on scheduling recurring backups to PetaLibrary.

```{note}
In addition to the methods outlined above, data can also be transferred to/from PetaLibrary via common command line utilities such as `rsync`, `scp`, and `sftp`, as well as via `Globus`, a user-friendly browser-based file transfer tool.  Documentation on these methods can be found in our [General Data Transfer documentation](../compute/data-transfer.md).
```
