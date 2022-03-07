## Alpine

### _EARLY RELEASE:_ CURC Alpine is currently in early testing available only for the Early Adopters group.

### _EARLY RELEASE:_ The Alpine cluster is currently in early release. If you see or experience any errors, please report them to [rc-help@colorado.edu](rc-help@colorado.edu).


Alpine is the third-generation HPC cluster at University of Colorado Research Computing, following Janus and RMACC Summit. Alpine is a heterogeneous cluster with pooled resources from the following institutions: CU Boulder, Colorado State University, and Anschutz Medical Campus. 

### Alpine Quick-Start:

1. From a login node, run the command:
   ```bash
   $ module load slurm/alpine
   ```
to access the Slurm job scheduler instance for Alpine.

2. Once the Alpine Slurm job scheduler has been loaded you can submit and start jobs on the Alpine cluster. Consult the [table](anchor) and the [examples](anchor) section below to learn how to direct your jobs to the appropriate Alpine compute nodes.

3. Software can be loaded into the Alpine compute environment via the [module system](link), which allows users choose from our pre-installed software stack.

4. If you would like to use software that is not within our preinstalled stack you can compile your application on a compute node via an interactive job (as Alpine does not yet have dedicated compile nodes). Consult our [compiling and linking](../compute/compiling.md) for more information on compiling software. You can also request a software installation by submitting a [software request form](lnk).

### Cluster Specifications:
#### Nodes
- **CPU nodes**: 64 AMD Milan Compute nodes (64 cores/node)
- **GPU nodes**: 
	- 8 GPU-enabled (3x AMD MI100) atop AMD Milan CPU
	- 8 GPU-enabled (3x NVIDIA A100) atop AMD Milan CPU

> For a full list of nodes on Alpine use the command:  `scontrol show nodes.` Get single node details with the `scontrol show nodes <node name>` command.
#### Interconnect
- **CPU nodes**: HDR-100 InfiniBand (200Gb inter-node fabric)
- **GPU nodes**: 2x25 Gb Ethernet +RoCE
- **Scratch Storage**: 25Gb Ethernet +RoCE


### Node Features
The Alpine cluster features some heterogeneity. A variety of feature tags are applied to nodes deployed in Alpine to allow jobs to target specific CPU, GPU, network, and storage requirements.

Use the `sinfo` command to determine the features that are available on any node in the cluster.

> _**Note:**_ **Feature descriptions and finalized partitions names are still being added to Alpine nodes. Refer to the [description of features](#description-of-features) list below for current node features.**

```bash
sinfo --format="%N | %f"
```

#### Description of features
- **Milan**: dual-socket 32-core AMD Milan CPU
- **A100**: NVIDIA A100 GPU
- **MI100**: AMD MI100 GPU- **localraid**: large, fast RAID disk storage in node
- **rhel8**: RedHat Enterprise Linux version 8 operating system


### Job Scheduling

All jobs on Alpine are run through a batch/queue system using the SLURM job scheduler. Though many HPC workflows are run through batch-type jobs, interactive jobs on compute nodes are allowed but these must be initiated through the scheduler. High-priority jobs move to the top of the queue and are thus guaranteed to start running within a few minutes, unless other high-priority jobs are already queued or running ahead of them. High-priority jobs can run for a maximum wall time of 24 hours. Low-priority jobs have a maximum wall time of 7 days.

More details about how to use SLURM to run jobs can be found in our [running applications with jobs](../running-jobs/running-apps-with-jobs.html) documentation.


### Requesting Resources
Resources are requested within jobs by passing in SLURM directives, or resource flags, to either a job script (most common) or the command line when submitting a job. Below are some common resource directives for Alpine: 
* **Partition:** specify node type
* **Gres (General Resources):** specify GPU amount (required if using a GPU node)
* **QOS (Quality of Service):** constrain or modify job characteristics

#### Partitions

**Nodes with the same hardware configuration are grouped into partitions**. You will need to specify a partition using `--partition` SLURM directive in your job script (or at the command line when submitting a job) in order for your job to run on the appropriate type of node. On Alpine nodes are also grouped by institution. You need to include your institutions suffix in order to request the required nodes. 

> **Note:** GPU nodes require the additional `--gres` directive (see next section).

Partitions available on Alpine:


| Partition       | Description       | # of nodes | cores/node | RAM/core (GB) | Billing weight | Default/Max Walltime |
| --------------- | ----------------- | ---------- | ---------- | ------------- | -------------- | ------------------------ |
| amilan-[institute] | AMD Milan (default) | 64 | 64 | 4.01 | 1              | 4H, 24H                  |
| ami100-[institute] | GPU-enabled (3x AMD MI100) | 8 | 64 | 4.01 | tbd | 4H, 24H                  |
| aa100-[institute]* | GPU-enabled (3x NVIDIA A100) | 8 | 64 | 4.01 | tbd | 4H, 24H                  |

> * Note: Nvidia A100 GPUs only support CUDA versions >11.x

** [institute] should be substituted for your institute** (examples):
* `ucb` (CU Boulder)
```bash
--partition=amilan-ucb
--partition=aa100-ucb
--partition=ami100-ucb
```
* `csu` (Colorado State University)
```bash
--partition=amilan-csu
--partition=aa100-csu
--partition=ami100-csu
```
* `amc` (Anschutz Medical Campus).
```bash
--partition=amilan-amc
--partition=aa100-amc
--partition=ami100-amc
```

#### General Resources (gres)

General resources allows for fine-grain hardware specifications. On Alpine the gres directive is **required** to use GPU accelerators on GPU nodes. At a minimum, one would specify `--gres=gpu` in their job script (or on the command line when submitting a job) to specify that they would like to use a single gpu on their specified partition. One can also request multiple GPU accelerators on nodes that have more than one. The available Alpine GPU resources and configurations can be viewed as follows on a login node with the `slurm/alpine` module loaded:

```bash
$ sinfo --Format NodeList:30,Partition,Gres |grep gpu |grep -v "mi100\|a100"
```

> _**Note:**_ AMD MI100 have yet to be provisioned with `gres` if needed, you can request a _whole_ AMD MI100 node by simply specifying `--partition=ami100-<institute>` without the `gres` functionality.

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

#### Quality of Service (qos)

Quality of Service or QoS is used to constrain or modify the characteristics that a job can have. This could come in the form of specifying a QoS to request for a longer run time. For example, by selecting the `long` QoS, a user can place the job in a **lower priority queue** with a max wall time increased from 24 hours to 7 days.

**Normally, this slurm directive does not need to be set for most jobs. Only set a QoS when requesting a long job.**

The available QoS's for Summit are:

| QOS name    | Description                | Max walltime    | Max jobs/user | Node limits        | Partition limits | Priority Adjustment  |
| ----------- | -------------------------- | --------------- | ------------- | ------------------ | ---------------- | ---------------------|
| normal      | Default                    | 1D              | tbd | tbd | n/a              | 0 |
| long        | Longer wall times          | 7D              | tbd | tbd | tbd | 0 |


#### Requesting GPUs in jobs



__Notes__:
  * Examples of full job scripts for GPUs are shown in the next section.

### Examples

Here are examples of Slurm directives that can be used in your batch scripts in order to meet certain job requirements.

1. To run a 32-core job for 36 hours on a single (default) Alpine CPU node (as a UCB user):
```bash
#SBATCH --partition=amilan-ucb
#SBATCH --nodes=1
#SBATCH --ntasks=32
#SBATCH --time=36:00:00
```

2. To run a 56-core job (28 cores/node) across two Alpine CPU nodes (as a CSU user) in the low-priority qos for seven days:
```bash
#SBATCH --partition=amilan-ucb
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=28
#SBATCH --time=7-00:00:00
#SBATCH --qos=long
```

3. To run a 16-core job for 24 hours on a single Alpine AMD GPU node (as a AMC user), using all three GPUs:
```bash
#SBATCH --partition=ami100-amc
#SBATCH --nodes=1
#SBATCH --ntasks=16
#SBATCH --time=24:00:00
#SBATCH --gres=gpu:3
```

4. To run a 50-core job for 2 hours on a single Alpine NVIDIA GPU node (as a UCB user), using 2 GPUs:
```bash
#SBATCH --partition=aa100-amc
#SBATCH --nodes=1
#SBATCH --ntasks=50
#SBATCH --time=02:00:00
#SBATCH --gres=gpu:2
```

5. To run an 8-core job for 4 hours on any node that has at least 1 GPU:
```bash
#SBATCH --nodes=1
#SBATCH --ntasks=8
#SBATCH --time=4:00:00
#SBATCH --gres=gpu
```

#### Full Example Job Script

Run a 1-hour job on 4 cores on an Alpine CPU node with the normal qos (as a UCB user).

```
#!/bin/bash
#SBATCH --partition=amilan-ucb
#SBATCH --job-name=example-job
#SBATCH --output=example-job.%j.out
#SBATCH --time=01:00:00
#SBATCH --qos=normal
#SBATCH --nodes=1
#SBATCH --ntasks=4

module purge
module load anaconda
conda activate custom-env

python myscript.py
```

### Allocations

All new Alpine users are granted an initial allocation (account) called `ucb-general`. Users who require more core hours than `ucb-general` can provide are advised to apply for an allocation. The allocation process requires that users have run example jobs in ucb-general that can be assessed by RC for efficiency/optimation on Alpine. We then work with users to make workflows more efficient if needed, and then grant the allocation.

You can read more about the allocation process and why you would want to apply for one on our [Allocation's page](../access/allocations.md).

> _**Note:**_ For Alpine early adopters, you may finish off your Summit project year on Alpine (i.e. port pro-rated Summit SUs ath the same level). For example, if you have 3 months left on an 1.2M SU grant, we can port 300k SU to Alpine.

### Moving from Summit to Alpine

* All software available on Summit should also be available on Alpine ([contact us](rc-help@colorado.edu) if you run into a software issue).

### Important notes

Not yet fully reviewed, subject to update:

1. To see what modules are available, start an interactive job on a compute node and use `module avail` or `module spider` on it.
2. Filesystems: `/home`, `/projects`, and `/pl/active` (PetaLibrary Active) are available on all Alpine nodes.
> Note that for job I/O, `/scratch/summit/$USER` is replaced by `/scratch/alpine/$USER`. The Alpine scratch directory will offer much better performance than doing I/O from `/projects`.
3. Node-local scratch: Most Alpine nodes also have at least 400 GB of scratch space on a local SSD disk, which will offer the fastest I/O possible.  We presently are working to make this space available to users, but presently _it is not_.  Once we make it available, this job specific directory will be available within jobs as `$SLURM_SCRATCH`. Note that this storage is only available during jobs and is deleted after jobs, so be sure to copy new data you want to keep off of it at the end of your job script. For more info on the different RC storage spaces, please see our page on [storage](../compute/filesystems.html).
4. Head-nodes: There are presently no dedicated Alpine "head nodes" that would be analogous to the Summit "scompile" nodes.  We are working to address this need. In the meantime, to build software that will run on Alpine, start an interactive job on an Alpine node on the partition on which you expect your jobs to run, and compile your software there. Do not compile on the login nodes!
