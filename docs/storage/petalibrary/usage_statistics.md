## Allocation Statistics 

### `alloc_stats`
Research Computing has implemented a background task called `alloc_stats` 
on the PetaLibrary cluster hosts to allow a PetaLibrary allocation owner 
and group members to view the usage statistics and the sizes of individual 
subdirectories in their allocation. This process collects this information 
hourly and deposits it in a file in the allocation base directory called 
`.cstats`.

### `.cstats`
The usage statistics file for an allocation contains the following 
information:

- time and date of latest `alloc_stats` run
- overall statistics: allocated, available, and used space in the 
allocation; data and snapshot usages reported separately
- user statistics including user name, space used  and number of objects 
(files and directories)

The `.cstats` file is an ordinary text file. It is readable only by users 
who are members of the group associated with the PetaLibrary allocation. 

When logged into CURC systems, you can query these statistics from the 
command line as follows: 

```
cat /pl/active/<allocation_name>/.cstats
```

For example, to get the usage information on the `/pl/active/rcops` 
allocation, enter 

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

Couldn't find what you need? [Provide feedback on these 
docs!](https://forms.gle/bSQEeFrdvyeQWPtW9)
