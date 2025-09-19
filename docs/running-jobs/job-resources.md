# Slurm Flags, Partitions, and QoS

Slurm allows the use of flags to specify resources needed for a job. Below is a table describing some of the most common Slurm resource flags, followed by tables describing available partitions and Quality of Service (QoS) options.

## Slurm Resource Flags

Job scripts, the `sbatch` command, and the `sinteractive` command support many different resource requests in the form of flags. These flags are available to all forms of jobs. To review all possible flags for these commands, please visit the [Slurm page on sbatch](http://slurm.schedmd.com/sbatch.html). Below, we have listed some useful flags to consider when running your job script.

| Type                    | Description                                    | Flag                       | Example                       |
| :---------------------- | :--------------------------------------------- | :------------------------- | :---------------------------- |
| [Allocation](../clusters/alpine/allocations.md)  | Specify an allocation account  | `--account=<allocation_name>` <br> | `--account=ucb###_asc1` <br>    |
| Partition          | Specify a partition ([see table below](#partitions)) | `--partition=<partition_name>` <br> | `--partition=amilan` <br>  |
| Sending email      | Receive an email at the beginning or the end of a job | `--mail-type=<type>` <br> | `--mail-type=BEGIN,END` <br>     |
| Email address      | Email address to receive the email                  | `--mail-user=<email_address>`  <br> | `--mail-user=ralphie@colorado.edu` <br>    |
| Number of nodes    | The number of nodes needed to run the job           | `--nodes=<#>` <br>  | `--nodes=1` <br>   |
| Number of tasks    | The ***total*** number of processes needed to run the job | `--ntasks=<#>` <br>  | `--ntasks=4`  <br>  |
| Tasks per node     | The number of processes you wish to assign to each node (only needed for multi-node jobs) | `--ntasks-per-node=<#>` <br> | `--ntasks-per-node=4` <br>  |
| Total memory       | The total memory (per node requested) required for the job. <br> Using `--mem` does not alter the number of cores allocated to the job, but you will be charged for the number of cores corresponding to the proportion of total memory requested. <br> Units of `--mem` can be specified with the suffixes: K,M,G,T (default M)| `--mem=<#><unit (optional)>` <br>  |`--mem=25G` <br>  |
| Quality of service | Specify a QoS ([see table below](#quality-of-service)) | `--qos=<qos_name>` <br>  | `--qos=normal`   <br>   |
| Wall time          | The max amount of time your job will run for        | `--time=<D-HH:MM:SS>`  <br> | `--time=03:00:00` <br>   |
| Job Name           | Name your job so you can identify it in the queue   | `--job-name=<job_name>` <br> | `--job-name=Census-Data-Analysis` <br>   |
| Job Array          | Specify the range of values to use for the Job Array indexes. | `--array=<START>-<STOP>`  | `--array=0-5` <br>. |

## Partitions

Nodes with the same hardware configuration are grouped into partitions. You will need to specify a partition using `--partition` in your job script in order for your job to run on the appropriate type of node. A list of partitions available on Alpine can be found on our [Alpine Hardware](../clusters/alpine/alpine-hardware.md#partitions) page. 

## Quality of Service

Quality of Service (QoS) is used to constrain or modify the characteristics that a job can have. This could come in the form of specifying a QoS to request for a longer run time or a high priority queue for condo owned nodes. For example, by selecting the `long` QoS, a user can place the job in a lower priority queue with a max wall time increased from 24 hours to 7 days. A list of QoS codes available on Alpine can be found on our [Alpine Hardware](../clusters/alpine/alpine-hardware.md#quality-of-service-qos) page. 


