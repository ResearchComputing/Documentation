# Monitoring Allocation Use

## Active and Active+archive allocations

The PetaLibrary active allocation owner and group members can view the usage statistics for their allocation by viewing an hourly-updated file in the allocation base directory called `.cstats`.  The `.cstats` file contains the following information: 

- time and date stamp for most recent usage query
- overall statistics: allocated, available, and used space in the 
allocation; data and snapshot usages reported separately
- user statistics including user name, space used  and number of objects 
(files and directories)

The `.cstats` file is an ordinary text file. It is readable only by users who are members of the group associated with the PetaLibrary allocation. 

When logged into CURC systems, you can query these statistics from the command line as follows: 

```
cat /pl/active/<allocation_name>/.cstats
```

For example, to get the usage information on the `/pl/active/rcops` allocation, enter 

```
cat /pl/active/rcops/.cstats
```

This will produce the following output:

```
-------------------------------------------------------
-------------------------------------------------------
Date/Time: 2022-09-05 04:00:08 PM

Allocation Name: penc3/rcops

-------------------------------------------------------
Overall Statistics:

Allocated Space: 27T

Available Space: 9.9T

Used Space: 18T
  -used by data:       14T
  -used by snapshots:  3.8T

-------------------------------------------------------
User Statistics:

            UserName      UsedData     UsedObjects
            datr2651	      666K	      1007
-------------------------------------------------------
```

```{note}
The `.cstats` file is the most comprehensive and accurate means of assessing usage in a given PetaLibrary active allocation. However, if your `.cstats` file becomes empty, it is likely your active allocation is full (because there is no space available to populate the file). You can confirm whether the allocation is full if the "Use" is 100% according to the output of the command `df -H /pl/active/<allocation_name>`. If the allocation becomes full, please submit a [support request form](https://colorado.service-now.com/req_portal?id=ucb_sc_rc_form) to discuss options. 
```

## Archive and Archive+DR allocations

The PetaLibrary archive allocation owner and group members can view the bulk usage statistics for their allocation as follows:

```
df -H /pl/active/<allocation_name>
```