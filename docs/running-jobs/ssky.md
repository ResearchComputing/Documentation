# Using the Summit `ssky` Condo Partition

Summit has 20 Intel Skylake nodes that were provisioned through contributions by individual research groups. These Skylake "condo" nodes are members of the `ssky` partition.  Condo contributors have preemptive access to their contributed nodes (collectively 15-of-the-20 nodes). All Summit users have access to a general-access pool of `ssky` nodes (5-of-the-20 nodes contributed by CU and CSU), and preemptable access to all `ssky` nodes. 

Each Skylake node has 24 cores, 174.6 GB of available memory, and employs the AVX-512 instruction set. By comparison the Summit Haswell nodes have 24 cores, 113 GB available memory, and employ the AVX2 instruction set.

## Access for condo contributors

Summit condo contributors have access to a summit condo contributor account with the format:  

`ucb-summit-{group}`  or  `csu-summit-{group}` 

For example if the RC operations group had contributed nodes then their condo account would be: `ucb-summit-rcops` (note: the `rcops` group is just used here for the sake of example). You can determine what accounts you are affiliated with using the command: 

```
sacctmgr list associations cluster=summit user=$USER format=Account -p
```

Contributed condo nodes have been placed into discrete partitions, with a name based on the contributor account name and node type; for example, `ssky-ucb-rcops` for RC operations contributed Skylake compute nodes. You can see the list of all ssky partitions using the command:

```
scontrol show partition | grep PartitionName=ssky
```

To submit a job (in this case assuming your group is `rcops`), specify the account and partition in your job script or interactive job command (e.g., `--account=ucb-summit-rcops` and `--partition=ssky-ucb-rcops`).

Jobs submitted with condo accounts/partitions will immediately preempt jobs running on a given condo partition that were submitted via the `ssky-preemptable` partition (see below). 

_Tip:_ If it is appropriate for your jobs, you can use a an ordered list of preferred partitions when submitting your jobs to `ssky`. E.g., `--partition=ssky-ucb-rcops,ssky` or (if you are willing to run preemtably) `--partition=ssky-ucb-rcops,ssky,ssky-preemptable`. If your first choice of partition is not available, the next partition in the list will be attempted, and so on.

## General and preemptable access for all Summit users

All Summit users, including condo contributors, can submit jobs to either general-access (e.g., `ssky`) partitions or preemptable (e.g., `ssky-preemptable`) partitions. Jobs submitted to the `ssky` partition will not be preempted, but are limited to the five general-access nodes. Jobs submitted to the `ssky-preemptable` partition may run on any `ssky` node, but are subject to being preempted by a job submitted by a condo contributor, as described above.

To submit a job to `ssky`, users would simply change the "partition" flag in their job script or interactive job command to either `--partition=ssky` or `--partition=ssky-preemptable`.  Other flags in their job script would remain the same, though users may want to tweak flags or recompile code (optimized for AVX-512) per the specifications of `ssky` nodes (see above).

## Summary

| *Partition* | *Description* |
|-----------------|-------------------------------------------------------|
| `ssky-ucb-rcops` | Contributor access; preempts `ssky-preemptable` |
| `ssky` | General access |
| `ssky-preemptable` | General access; all nodes; preempted by `ssky-{ucb,csu}-{group}`|




