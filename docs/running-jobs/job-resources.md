# Slurm Flags, Partitions, and QoS

Slurm allows the use of flags to specify resources needed for a job. Below is a table describing some of the most common Slurm resource flags, followed by tables describing available partitions and Quality of Service (QoS) options.

## Slurm Resource Flags

Job scripts, the `sbatch` command, and the `sinteractive` command support many different resource requests in the form of flags. These flags are available to all forms of jobs. To review all possible flags for these commands, please visit the [Slurm page on sbatch](http://slurm.schedmd.com/sbatch.html). Below, we have listed some useful flags to consider when running your job script.

| Type               | Description                                         | Flag                       |
| :----------------- | :-------------------------------------------------- | :------------------------- |
| [Allocation](../clusters/alpine/allocations.md)  | Specify an allocation account  | `--account=allocation`       |
| Partition          | Specify a partition ([see table below](#partitions)) | `--partition=partition` |
| Sending email      | Receive an email at the beginning or the end of a job | `--mail-type=type`           |
| Email address      | Email address to receive the email                  | `--mail-user=user`           |
| Number of nodes    | The number of nodes needed to run the job           | `--nodes=nodes`              |
| Number of tasks    | The ***total*** number of processes needed to run the job | `--ntasks=processes`   |
| Tasks per node     | The number of processes you wish to assign to each node | `--ntasks-per-node=processes` |
| Total memory       | The total memory (per node requested) required for the job. <br> Using --mem does not alter the number of cores allocated <br> to the job, but you will be charged for the number of cores <br> corresponding to the proportion of total memory requested. <br> Units of --mem can be specified with the suffixes: K,M,G,T (default M)| `--mem=memory` |
| Quality of service | Specify a QoS ([see table below](#quality-of-service)) | `--qos=qos`               |
| Wall time          | The max amount of time your job will run for        | `--time=wall time`           |
| Job Name           | Name your job so you can identify it in the queue   | `--job-name=jobname`         |


## Partitions

Nodes with the same hardware configuration are grouped into partitions. You will need to specify a partition using `--partition` in your job script in order for your job to run on the appropriate type of node. A list of partitions available on Alpine can be found in our page on [Alpine Hardware](../clusters/alpine/alpine-hardware.md#partitions). 

## Quality of Service

Quality of Service (QoS) is used to constrain or modify the characteristics that a job can have. This could come in the form of specifying a QoS to request for a longer run time or a high priority queue for condo owned nodes. For example, by selecting the `long` QoS, a user can place the job in a lower priority queue with a max wall time increased from 24 hours to 7 days. 

```{note}
Normally, this slurm directive does not need to be set for most jobs. Only set a QoS when requesting a long or condo (Blanca) job.
```
