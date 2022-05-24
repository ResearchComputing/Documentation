## Slurm Flags, Partitions, and QoS

Slurm allows the use of flags to specify resources needed for a job. Below is a table describing some of the most common Slurm resource flags, followed by tables describing available Summit partitions and Quality of Service (QoS) options.

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
| Total Memory       | The total memory (per node requested) required to complete the job. <br> The number of cores allocated to your job does not scale with the total memory requested, <br> but you will be charged # cores = total memory / RAM per core. <br> Units can be specified with the suffixes: K,M,G,T (default M)| --mem=memory |
| Quality of service | Specify a QOS ([see table below](#quality-of-service)) | --qos=qos               |
| Wall time          | The max amount of time your job will run for        | --time=wall time           |
| Job Name           | Name your job so you can identify it in the queue   | --job-name=jobname         |


### Partitions (Summit)

On Summit, nodes with the same hardware configuration are grouped into partitions. You will need to specify a partition using `--partition` in your job script in order for your job to run on the appropriate type of node.

These are the partitions available on Summit.

| Partition       | Description       | # of nodes | cores/node | RAM/core (GB) | Billing weight | Default/Max Walltime |
| --------------- | ----------------- | ---------- | ---------- | ------------- | -------------- | ------------------------ |
| shas            | Haswell (default) | 380        | 24         | 4.84          | 1              | 4H, 24H                  |
| sgpu            | GPU-enabled       | 10         | 24         | 4.84          | 2.5            | 4H, 24H                  |
| smem <sup>1</sup> | High-memory     | 5          | 48         | 42.7          | 6              | 4H, 7D                   |
| sknl            | Phi (KNL)         | 20         | 68         | 5.25          | 0.1            | 4H, 24H                  |
| ssky <sup>2</sup> | Skylake         | 5          | 24         | 7.68          | 1              | 4H, 24H                 |
| ssky-preemptable <sup>2</sup> | Skylake | 15     | 24         | 7.68          | 1              | 4H, 24H                  |

> <sup>1</sup> The `smem` partition is limited to 96 cores (2 entire nodes) across *all running smem jobs.* For example, you can run one 96-core job or up to two 48-core jobs, four 24-core jobs, ninty-six 1-core jobs, etc.  If you need more memory or cores, please contact <rc-help@colorado.edu>.
> 
> <sup>2</sup> Skylake nodes are seperated into 2 partitions and consists of 5 public nodes in the `ssky` partition and 15 private nodes that can be used by anyone with the `ssky-preemptable`. Jobs running on the `ssky-preemptable` partition will be pushed off the node if the condo owner of the node runs a job to their private partition. More information on Skylake nodes [can be found here.](ssky.html)

In addition to these partitions, Research Computing also provides specialized partitions for interactive and test jobs. These partitions allow quick access to a reserved set of cores provided for testing and interactive use. 

| Partition        | Description  | Max Nodes | Max cores | RAM/core (GB) | Billing weight | Default/Max Walltime |
| ---------------- | ------------ | --------- | --------- | ------------- | -------------- | ------------------------ |
| shas-testing <sup>3</sup> | Haswell| Up to 2| 24      | 4.84         | 1              | 0.5H, 0.5H               |
| shas-interactive | Haswell      | 1         | 1         | 4.84          | 1              | 1H, 4H                   |
| sgpu-testing     | GPU-enabled  | 1         | 24        | 4.84          | 2.5            | 0.5H, 0.5H               |
| sknl-testing     | Phi (KNL)    | 1         | 24        | 5.25          | 1              | 0.5H, 0.5H               |

> <sup>3</sup> The `shas-testing` partition is limited to 24 cores total. These cores can come from up to 2 nodes but a user is limited to maximum of 24 cores per job.

To run a job longer than 24 hours on the `shas`, or `sknl` partitions, use the `long` QOS.

More details about each type of node can be found [here](https://www.colorado.edu/rc/resources/summit/specifications).

### Quality of Service (Summit)

On Summit, Quality of Service or QoS is used to constrain or modify the characteristics that a job can have. This could come in the form of specifying a QoS to request for a longer run time or a high priority queue for condo owned nodes. For example, by selecting the `long` QoS, a user can place the job in a lower priority queue with a max wall time increased from 24 hours to 7 days. 

**Normally, this slurm directive does not need to be set for most jobs. Only set a QoS when requesting a long or condo job.**

The available QoS's for Summit are:

| QOS name    | Description                | Max walltime    | Max jobs/user | Node limits        | Partition limits | Priority Adjustment  |
| ----------- | -------------------------- | --------------- | ------------- | ------------------ | ---------------- | ---------------------|
| normal      | Default                    | 1D              | 1000          | 256/user           | n/a              | 0 |
| long        | Longer wall times          | 7D              | 200           | 22/user; 40 total; | shas, sknl, ssky | 0 |
| condo       | Condo purchased nodes only | 7D              | 500           | 256/user           | shas, ssky       | Equiv. of 1 day queue wait time |

Couldn't find what you need? [Provide feedback on these docs!](https://forms.gle/bSQEeFrdvyeQWPtW9)
