## Slurm Flags, Partitions, and QoS

Slurm allows the use of flags to specify resources needed for a job. Below is a table describing some of the most common Slurm resource flags, followed by tables describing available partitions and Quality of Service (QoS) options.

### Slurm Resource Flags

Job scripts, the `sbatch` command, and the `sinteractive` command support many different resource requests in the form of flags. These flags are available to all forms of jobs. To review all possible flags for these commands, please visit the [Slurm page on sbatch](http://slurm.schedmd.com/sbatch.html). Below, we have listed some useful flags to consider when running your job script.

| Type               | Description                                         | Flag                       |
| :----------------- | :-------------------------------------------------- | :------------------------- |
| [Allocation](../access/allocations.html)    | Specify an allocation account  | --account=allocation       |
| Partition          | Specify a partition ([see table below](#partitions)) | --partition=partition |
| Sending email      | Receive email at beginning or end of job completion | --mail-type=type           |
| Email address      | Email address to receive the email                  | --mail-user=user           |
| Number of nodes    | The number of nodes needed to run the job           | --nodes=nodes              |
| Number of tasks    | The ***total*** number of processes needed to run the job | --ntasks=processes   |
| Tasks per node     | The number of processes you wish to assign to each node | --ntasks-per-node=processes |
| Total memory       | The total memory (per node requested) required for the job. <br> Using --mem does not alter the number of cores allocated <br> to the job, but you will be charged for the number of cores <br> corresponding to the proportion of total memory requested. <br> Units of --mem can be specified with the suffixes: K,M,G,T (default M)| --mem=memory |
| Quality of service | Specify a QoS ([see table below](#quality-of-service)) | --qos=qos               |
| Wall time          | The max amount of time your job will run for        | --time=wall time           |
| Job Name           | Name your job so you can identify it in the queue   | --job-name=jobname         |


### Partitions

Nodes with the same hardware configuration are grouped into partitions. You will need to specify a partition using `--partition` in your job script in order for your job to run on the appropriate type of node.

These are the partitions available on Alpine.

| Partition | Description                  | # of nodes | cores/node | RAM/core (GB) | Billing weight | Default/Max Walltime     |
| --------- | ---------------------------- | ---------- | ---------- | ------------- | -------------- | ------------------------ |
| amilan    | AMD Milan (default)          | 184        | 64         |   3.74        | 1              | 24H, 24H                 |
| ami100    | GPU-enabled (3x AMD MI100)   | 8          | 64         |   3.74        | tbd            | 24H, 24H                 |
| aa100     | GPU-enabled (3x NVIDIA A100) | 8          | 64         |   3.74        | tbd            | 24H, 24H                 |
| amem<sup>1</sup> | High-memory           | 4          | 48         | 21.486        | tbd            |  4H,  7D                 |
| csu       | Nodes contributed by CSU     | 77         | 32 or 48   |   3.74        | 1              | 24H, 24H                

> <sup>1</sup> The `amem` partition is limited to 96 cores (2 entire nodes) across *all running amem jobs.* For example, you can run one 96-core job or up to two 48-core jobs, four 24-core jobs, ninty-six 1-core jobs, etc.  If you need more memory or cores, please contact <rc-help@colorado.edu>.
> 

In addition to these partitions, Research Computing also provides specialized partitions for interactive and test jobs, as well as compilation. These partitions allow quick access to a reserved set of cores provided for testing and interactive use. 

| Partition        | Description       | Max Nodes | Max cores | Billing weight | Default/Max Walltime     |
| ---------------- | ----------------- | --------- | --------- | -------------- | ------------------------ |
| atesting <sup>3</sup> | Testing      | Up to 2   | 32        | 1              | 0.5H, 3H                 |
| acompile         | Compile           | 1         | 4         | 4              | 1H, 12H                  |
| ainteractive     | Interactive Jobs  | 1         | 1         | 4              | 1H, 12H                  |

> <sup>3</sup> The `atesting` partition is limited to 32 cores total. These cores can come from up to 2 nodes, but a user is limited to maximum of 32 cores per job.

To run a job longer than 24 hours on the `amilan`, `ami100`, or `aa100` partitions, use the `long` QOS.

More details about each type of node can be found [here](https://curc.readthedocs.io/en/latest/clusters/alpine/alpine-hardware.html).

### Quality of Service

Quality of Service (QoS) is used to constrain or modify the characteristics that a job can have. This could come in the form of specifying a QoS to request for a longer run time or a high priority queue for condo owned nodes. For example, by selecting the `long` QoS, a user can place the job in a lower priority queue with a max wall time increased from 24 hours to 7 days. 

**Normally, this slurm directive does not need to be set for most jobs. Only set a QoS when requesting a long or condo job.**

The available QoS's for Alpine are:

| QOS name    | Description                | Max walltime    | Max jobs/user | Node limits        | Partition limits | Priority Adjustment  |
| ----------- | -------------------------- | --------------- | ------------- | ------------------ | ---------------- | ---------------------|
| normal      | Default                    | 1D              | tbd           | tbd                | n/a              | 0                    |
| long        | Longer wall times          | 7D              | tbd           | tbd                | tbd              | 0                    |
| mem         | High-memory jobs           | 7D              | tbd           | 12                 | amem only        | 0                    |

Couldn't find what you need? [Provide feedback on these docs!](https://forms.gle/bSQEeFrdvyeQWPtW9)
