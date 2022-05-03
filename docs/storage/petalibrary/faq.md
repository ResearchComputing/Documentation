## FAQ

1. [Why does my allocation report less storage than I requested?](#why-does-my-allocation-report-less-storage-than-i-requested)
2. [I am a BioKEM facility user, how do I have my data deposited to my PetaLibrary Allocation?](#biokem-facility-data-deposit)

### Why does my allocation report less storage than I requested?

PetaLibrary allocation sizes are set with quotas, and snapshot use does count against your quota. Removing a file from your filesystem will only return free space to your filesystem if no snapshots reference the file. Filesystem free space does not increase until a file on a filesystem and all snapshots referencing said file are removed. Because snapshots can cause confusion about how space is utilized within an allocation, the default snapshot schedule discards snapshots that are more than one week old.

If you would like to set a custom snapshot schedule for your allocation, please contact rc-help@colorado.edu. Note that the longer you retain snapshots, the longer it will take to free up space by deleting files from your allocation.

### BioKem Facility Data Deposit

If you are a BioKEM facility user, you can choose to have your data deposited directly into your PetaLibrary allocations. This process involves creating a biokem-deposit directory in your allocation’s root directory and setting permissions to a biokem specific owner and group. Visit [our documentation](../../additional-resources/biokem-facility.html) on the BioKEM facility to learn about the process.





Couldn't find what you need? [Provide feedback on these docs!](https://docs.google.com/forms/d/1WoP_KtLp9lnTEsgW7Os-we45_JbEt3aUgS6j61jARnk/edit)
