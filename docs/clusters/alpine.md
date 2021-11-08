## Alpine

> **:warning: Early Release.**
> The Alpine cluster is in early/beta release and being actively developed. If you see or experience any errors, please report them to [rc-help@colorado.edu](rc-help@colorado.edu).

Alpine is the third-generation HPC cluster at University of Colorado Research Computing, following Janus and RMACC Summit.

### Alpine Quick-Start

1. From a login node, run "module load slurm/alpine" to access the Slurm job scheduler instance for Alpine.
2. Consult the Table and the Examples section below to learn how to direct your jobs to the appropriate compute nodes.
3. If needed, compile your application on a compute node via an interactive job as Alpine does not have dedicated compile nodes. Consult our [compiling and linking](../compute/compiling.md) for more information on compiling software.

### Job Scheduling

All jobs are run through a batch/queue system. Interactive jobs on compute nodes are allowed but these must be initiated through the scheduler. High-priority jobs move to the top of the queue and are thus guaranteed to start running within a few minutes, unless other high-priority jobs are already queued or running ahead of them. High-priority jobs can run for a maximum wall time of 24 hours. Low-priority jobs have a maximum wall time of 7 days.

More details about how to use Slurm can be found [here](../running-jobs/running-apps-with-jobs.html).

### Nodes

To determine which nodes exist on the Alpine system, type `scontrol show nodes` to get a full list.

### Node Features

The Alpine cluster features some heterogeneity. A variety of feature tags are applied to nodes deployed in Alpine to allow jobs to target specific CPU, GPU, network, and storage requirements.

Use the `sinfo` command to determine the features that are available on any node in the cluster.

> :warning: Feature descriptions and finalized partitions names are still being added to Alpine nodes. Refer to the [description of features](#description-of-features) list below for current node features.

```bash
sinfo --format="%N | %f"
```

The `sinfo` query may be further specified to look at the features available within a specific partition.

```bash
sinfo --format="%N | %f" --partition="alpine-curc"
```

#### Description of features

- **Milan**: dual-socket 32-core AMD Milan CPU
- **A100**: NVIDIA A100 GPU  
- **MI100**: AMD MI100 GPU  
- **localraid**: large, fast RAID disk storage in node  
- **rhel8**: RedHat Enterprise Linux version 8 operating system  

### Requesting Resources 

#### Partitions

On Alpine, nodes with the same hardware configuration are grouped into partitions. You will need to specify a partition using `--partition` in your job script in order for your job to run on the appropriate type of node.

These are the partitions available on Alpine.


| Partition       | Description       | # of nodes | cores/node | RAM/core (GB) | Billing weight | Default/Max Walltime |
| --------------- | ----------------- | ---------- | ---------- | ------------- | -------------- | ------------------------ |
| amilan-[gX] | Milan (default) | 64 | 64 | 4.01 | 1              | 4H, 24H                  |
| ami100-[gX] | GPU-enabled (3xMI100) | 8 | 64 | 4.01 | tbd | 4H, 24H                  |
| aa100-[gX] | GPU-enabled (3xA100) | 8 | 64 | 4.01 | tbd | 4H, 24H                  |

#### Quality of Service

On Alpine, Quality of Service or QoS is used to constrain or modify the characteristics that a job can have. This could come in the form of specifying a QoS to request for a longer run time. For example, by selecting the `long` QoS, a user can place the job in a lower priority queue with a max wall time increased from 24 hours to 7 days. 

**Normally, this slurm directive does not need to be set for most jobs. Only set a QoS when requesting a long job.**

The available QoS's for Summit are:

| QOS name    | Description                | Max walltime    | Max jobs/user | Node limits        | Partition limits | Priority Adjustment  |
| ----------- | -------------------------- | --------------- | ------------- | ------------------ | ---------------- | ---------------------|
| normal      | Default                    | 1D              | tbd | tbd | n/a              | 0 |
| long        | Longer wall times          | 7D              | tbd | tbd | tbd | 0 |

#### Requesting GPUs in jobs

Using GPUs in jobs requires one to use the General Resource ("gres") functionality of Slurm to request the gpu(s).  At a minimum, one would specify `#SBATCH --gres=gpu` in their job script to specify that they would like to use a single gpu of any type.  One can also request multiple GPUs on nodes that have more than one, and a specific type of GPU (e.g. A100, MI100) if desired.  The available Alpine GPU resources and configurations can be viewed as follows on a login node with the `slurm/alpine` module loaded:

```bash
$ sinfo --Format NodeList:30,Partition,Gres |grep gpu |grep -v "mi100\|a100"
```
> :warning: GPU resouces to be added

__Examples of configurations one could request__:

_request a single gpu of any type_
```
#SBATCH --gres=gpu
```

_request multiple gpus of any type_
```
#SBATCH --gres=gpu:3
```

_request two gpus of type NVIDIA A100_
```
#SBATCH --gres=gpu:a100:2
```

__Notes__:
  * Examples of full job scripts for GPUs are shown in the next section.

### Examples

Here are examples of Slurm directives that can be used in your batch scripts in order to meet certain job requirements.

1. To run a 32-core job for 36 hours on a single (default) Alpine CPU node:
```bash
#SBATCH --partition=amilan
#SBATCH --nodes=1
#SBATCH --ntasks=32
#SBATCH --time=36:00:00
```

2. To run a 56-core job across two alpine nodes in the low-priority qos for seven days:
```bash
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=28
#SBATCH --time=7-00:00:00
#SBATCH --qos=long
```

3. To run a 16-core job for 36 hours on a single Alpine gpu node, using all three gpus:
```bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --time=36:00:00
#SBATCH --gres=gpu:3
```
4. To run an 8-core job for 4 hours on any node that has at least 1 GPU:
```bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=8
#SBATCH --time=4:00:00
#SBATCH --gres=gpu
```

### Important notes

Not yet fully reviewed, subject to update:

1. To see what modules are available, start an interactive job on a compute node and use `module avail` or `module spider` on it.
2. /home, /projects, and /pl/active (PetaLibrary Active) are available on all Alpine nodes.  I/O can be written to /rc_scratch, which should offer much better performance than /projects.  Most Alpine nodes also have at least 400 GB of scratch space on a local disk, available to jobs as $SLURM_SCRATCH.  For more info on the different RC storage spaces, [please see our page on storage.](https://www.colorado.edu/rc/resources/filesystemstorage)
3. There are no dedicated Alpine compile nodes.  To build software that will run on Alpine, start an interactive job on a node like the one on which you expect your jobs to run, and compile your software there.  Do not compile on the login nodes!

#### Example Job Scripts

Run a 1-hour job on 4 cores on an amilan cpu node with the normal qos.

```
#!/bin/bash
#SBATCH --job-name=example-job
#SBATCH --output=example-job.%j.out
#SBATCH --time=01:00:00
#SBATCH --partition=amilan
#SBATCH --qos=normal
#SBATCH --nodes=1
#SBATCH --ntasks=4

module purge
module load python

python myscript.py
```
