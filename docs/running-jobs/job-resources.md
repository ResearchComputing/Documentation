## Job Resource Information

Slurm allows the use of flags to specify resources needed for a job. Below is a table describing some of the most common Slurm resource flags, followed by tables describing available Summit partitions and Quality of Service (QoS) options.

### Slurm Resource Flags

Job scripts, the `sbatch` command, and the `sinteractive` command support many different resource requests in the form of flags. To review all options for sbatch, please visit the Slurm [sbatch page](http://slurm.schedmd.com/sbatch.html). Below, we have listed some flags to consider when submitting your job script.

| Type               | Description                                         | Flag                       |
| :----------------- | :-------------------------------------------------- | :------------------------- |
| [Allocations](../access/allocations)    | Specify an allocation account  | --account=allocation       |
| Partitions         | Specify a partition ([see table below](#partitions)) | --partition=partition |
| Sending email      | Receive email at beginning or end of job completion | --mail-type=type           |
| Email address      | Email address to receive the email                  | --mail-user=user           |
| Number of nodes    | The number of nodes needed to run the job           | --nodes=nodes              |
| Number of tasks    | The ***total*** number of processes needed to run the job | --ntasks=processes   |
| Tasks per node     | The number of processes you wish to assign to each node | --ntasks-per-node=processes |
| Total Memory       | The total memory required to complete the Job. <br> Requesting more memory will reserve additional <br> cores proportional to how much memory was requested. <br> Units can be specified with the suffixes: K,M,G,T | --mem=memory |
| Quality of service | Specify a QOS ([see table below](#quality-of-service)) | --qos=qos               |
| Wall time          | The max. amount of time your job will run for       | --time=wall time           |
| Job Name           | Name your job so you can identify it in the queue   | --job-name=jobname         |


### Partitions

On Summit, nodes with the same hardware configuration are grouped into partitions. You will need to specify a partition using `--partition` in your job script in order for your job to run on the appropriate type of node.

These are the partitions available on Summit.

| Partition | Description       | # of nodes | cores/node | RAM/core (GB) | Billing weight | Default and Max Walltime |
| --------- | ----------------- | ---------- | ---------- | ------------- | -------------- | ------------------------ |
| shas      | Haswell (default) | 380        | 24         | 4.84          | 1              | 4H, 24H                  |
| sgpu      | GPU-enabled       | 10         | 24         | 4.84          | 2.5            | 4H, 24H                  |
| smem*    | High-memory       | 5          | 48         | 42.7          | 6              | 4H, 7D                   |
| sknl      | Phi (KNL)         | 20         | 68         | 5.25          | 0.1            | 4H, 24H                  |

*The *smem* partition is limited to 96 cores (2 entire nodes) across _all_ running *smem* jobs. For example, you can run one 96-core job or up to two 48-core jobs, four 24-core jobs, ninty-six 1-core jobs, etc.  If you need more memory or cores, please contact [rc-help@colorado.edu](rc-help@colorado.edu).

In addition to these partitions, Research Computing also provides specialized partitions for interactive and test jobs. Each of these partitions must be paired with their corresponding Quality of Service ([see QoS options below](#quality-of-service)).

| Partition        | Description       | Max Nodes | Max cores | RAM/core (GB) | Billing weight | Default and Max Walltime |
| ---------------- | ----------------- | --------- | --------- | ------------- | -------------- | ------------------------ |
| shas-testing*   | Haswell (default) | 24        | 24        | 4.84          | 1              | 0.5H, 0.5H               |
| shas-interactive | Haswell (default) | 1         | 1         | 4.84          | 1              | 1H, 4H                   |
| sgpu-testing     | GPU-enabled       | 1         | 24        | 4.84          | 2.5            | 0.5H, 0.5H               |
| sknl-testing     | Phi (KNL)         | 1         | 24        | 5.25          | 1              | 0.5H, 0.5H               |

*The *shas testing* partition is limited to 24 cores total. These cores can be spread upon multiple nodes but only 24 will be available for the partition.

To run a job longer than 24 hours on the *shas*, *sgpu*, or *sknl* partitions, use the *long* QOS.

More details about each type of node can be found [here](https://www.colorado.edu/rc/resources/summit/specifications).

### Quality of Service

On Summit, Quality of Service or QoS is used to constrain or modify the characteristics that a job can have. For example, by selecting the *testing* QoS, a user can obtain higher queue priority for a job with the trade-off that the maximum allowed wall time is reduced from what would otherwise be allowed on that partition. We recommend specifying a QoS as well as a partition for every job.

The available QoS's for Summit are:

| QOS name    | Description                           | Max walltime    | Max jobs/user | Node limits                      | Priority boost                  |
| ----------- | ------------------------------------- | --------------- | ------------- | -------------------------------- | ------------------------------- |
| normal*     | default                               | see table above | n/a           | 256/user                         | 0                               |
| testing     | For quick turnaround when testing     | 30M             | 1             | 24 cores *across* up to 24 nodes | QoS has dedicated cores         |
| interactive | For interactive jobs (command or GUI) | 4H              | 1             | 1 core                           | QoS has dedicated cores         |
| long        | Longer wall times                     | 7D              | n/a           | 22/user; 40 total                | 0                               |
| condo       | Condo purchased nodes only            | 7D              | n/a           | n/a                              | Equiv. of 1 day queue wait time |

*The _normal_ QOS is the default QOS if no other is specified.

**The testing and interactive QOS must be paired with a testing or interactive partition. Jobs that utilize testing and interactive QOS will fail if paired with a any other partition**
