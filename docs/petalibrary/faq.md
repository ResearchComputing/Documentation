## PetaLibrary FAQ

1. [Why does my allocation report less storage than I requested?](#why-does-my-allocation-report-less-storage-than-i-requested)

### Why does my allocation report less storage than I requested?

PetaLibrary allocation sizes are set with quotas, and snapshot use does count against your quota. Removing a file from your filesystem will only return free space to your filesystem if no snapshots reference the file. Filesystem free space does not increase until a file on a filesystem and all snapshots referencing said file are removed. Because snapshots can cause confusion about how space is utilized within an allocation, the default snapshot schedule discards snapshots that are more than one week old.

If you would like to set a custom snapshot schedule for your allocation, please contact rc-help@colorado.edu. Note that the longer you retain snapshots, the longer it will take to free up space by deleting files from your allocation.




