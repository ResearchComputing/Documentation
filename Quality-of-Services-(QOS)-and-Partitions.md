### Table of Contents
[Overview](#overview)
[Partitions](#partitions)
[Quality of Services](#quality-of-service)

# Overview

There are several ways to define in Slurm where your job will run.  Two of these ways are partitions and Quality of Services, or QOSes.  Partitions and QOSes can be specified when using the Slurm [sbatch command](https://slurm.schedmd.com/sbatch.html).  This document will describe the different partitions and QOSes for Research Computing resources.  

# Partitions

On Summit, nodes with the same hardware configuration are grouped into partitions. You will need to specify a partition using  --partition in sbatch in order for your job to run on the appropriate type of node.

|Partition name|    Description        |# of nodes|cores/nodes|RAM/core (GB)|Max Walltime|Billing weight|
|--------------|-----------------------|----------|-----------|-------------|------------|--------------|
|     shas     |Haswell CPUs (default) |   380    |    24     |    5.25     |    24H     |       1      |
|     sgpu     |      GPU-enabled      |    10    |    24     |    5.25     |    24H     |      2.5     |
|     smem     |      High-memory      |     5    |    48     |     42      |     7D     |       6      |
|     sknl     | Phi (Knights Landing) |    20    |    64     |    TBD      |    24H     |      0.1     |

More details about each type of node can be found [here](https://www.colorado.edu/rc/resources/summit/specifications).

# Quality of service

On Blanca, a QoS is specified to submit a job to either a group's high-priority queue or to the shared low-priority queue.

On Summit, QoSes are used to constrain or modify the characteristics that a job can have. For example, by selecting the "debug" QoS, a user can obtain higher queue priority for a job with the tradeoff that the maximum allowed wall time is reduced from what would otherwise be allowed on that partition. We recommend specifying a QoS (using the  --qos  flag or directive in Slurm) as well as a partition for every job

The available Summit QoSes are

|QOS name|       Description          |     Max walltime     |Max jobs/user|   Node limits   |Priority boost|
|--------|----------------------------|----------------------|-------------|-----------------|--------------|
| normal |         default            |Derived from partition|     n/a     |  256/user       |       0      |
| debug  |     For quick testing      |          1H          |      1      |   32/job        |Equiv. of 3-day queue wait time|
|  long  |     Longer wall times      |          7D          |     n/a     |22/user;40 total |0       |
|  condo | Condo purchased nodes only |          7D          |     n/a     |n/a              |Equiv. of 1 day queue wait time|