## Alpine Quick Start

Alpine is the University of Colorado Boulder Research Computing's third-generation high performance computing (HPC) cluster. Alpine is a heterogeneous compute cluster currently composed of hardware provided from University of Colorado Boulder. Additional contributions provided from Colorado State University and Anschutz Medical Campus are planned for the near future. Alpine currently offers 80 compute nodes and a total of 5120 cores.

Alpine can be securely accessed anywhere, anytime using OpenOnDemand or ssh connectivity to the CURC system.

### Alpine Quick-Start

1. From a *login node* load the `slurm/alpine` module to access the SLURM job scheduler instance for Alpine:
   ```bash
   $ module load slurm/alpine
   ```

2. Once the Alpine Slurm job scheduler has been loaded you can submit and start jobs on the Alpine cluster. Consult the [requesting resources](#requesting-resources) section and the [examples](#examples) section below to learn how to direct your jobs to the appropriate Alpine compute nodes.

3. Software can be loaded into the Alpine compute environment via the LMOD [module system](../../compute/modules.html), which allows users choose software from our pre-installed software stack.

4. If you would like to use software that is not within our preinstalled stack your application must be compiled using an `acompile` job (similar to ssh'ing to an `scompile` node on Summit). Once you have loaded in the `slurm/alpine` module you can run the following command to open up a compile job with a default of 1 core, 3.75GB RAM, for 60 minutes:
```bash
$ acompile
```
> Note: the lack of `ssh` before `acompile`

> Note that only 1 `acompile` job can be open at a time

Consult our [compiling and linking documentation](../compute/compiling.md) for more information on compiling software. You can also submit a software request to rc-help@colorado.edu.

### Cluster Summary
#### Nodes
The Alpine cluster is made up of different types of nodes outlined below:
- **CPU nodes**: 64 AMD Milan Compute nodes (64 cores/node)
- **GPU nodes**:
	- 8 GPU-enabled (3x AMD MI100) atop AMD Milan CPU
	- 8 GPU-enabled (3x NVIDIA A100) atop AMD Milan CPU

> For a full list of nodes on Alpine use the command:  `scontrol show nodes.` Get single node details with the `scontrol show nodes <node name>` command.

#### Interconnect
The Alpine cluster has different types of interconnects/fabrics which connect different types of hardware, outlined below:
- **CPU nodes**: HDR-100 InfiniBand (200Gb inter-node fabric)
- **GPU nodes**: 2x25 Gb Ethernet +RoCE
- **Scratch Storage**: 25Gb Ethernet +RoCE


### Node Features
The Alpine cluster features some heterogeneity. A variety of feature tags are applied to nodes deployed in Alpine to allow jobs to target specific CPU, GPU, network, and storage requirements.

Use the `sinfo` command to determine the features that are available on any node in the cluster.

> _**Note:**_ **Feature descriptions and finalized partitions names are still being added to Alpine nodes. Refer to the description of features list below for current node features.**

```bash
sinfo --format="%N | %f"
```

#### Description of features
- **Milan**: dual-socket 32-core AMD Milan CPU
- **A100**: NVIDIA A100 GPU
- **MI100**: AMD MI100 GPU- **localraid**: large, fast RAID disk storage in node
- **rhel8**: RedHat Enterprise Linux version 8 operating system

### Compile Jobs

If you have used Summit in the past, compiling on Alpine bahaves slightly differently. Instead of having dedicated hardware (2 full nodes) which are oversubscribed for users to `ssh` directly into, Alpine's `acompile` command starts an interactive job for users which provides the following benefits:
- Users can request specific resources (i.e. more cores to compile with, specific GPU resources)
- Limits dedicated hardware permanently set aside
- Users can't accidentally run full workflows that can slow down the entire system

Once you have loaded in the `slurm/alpine` module you can run the following command to open up a compile job with a default of 1 core, 3.75GB RAM, for 60 minutes:
```bash
$ acompile
```
or for options/help:
```bash
$ acompile --help
acompile: CURC utility to access a single alpine compute node for compiling software
usage:
       -t | --time=<time-limit>        : set the job's minimum runtime (default 60 minutes)
       -n | --ntasks=<number-of-cores> : set the number of cores required for the session (default 1/max 4)
       -G | --gpu=<nvidia|amdgpu>      : request a gpu to compile against
       -X | --x11                      : enable x11 support for the session
       -h | --help                     : print this message
```



### Job Scheduling

All jobs on Alpine are run through a queue system using the SLURM job scheduler. Though many HPC workflows are run through batch-type jobs, interactive jobs on compute nodes are allowed but these must also be initiated through the scheduler. High-priority jobs move to the top of the queue and are thus guaranteed to start running within a few minutes, unless other high-priority jobs are already queued or running ahead of them. High-priority jobs can run for a maximum wall time of 24 hours. Low-priority jobs have a maximum wall time of 7 days.

More details about how to use SLURM to run jobs can be found in our [running applications with jobs](../running-jobs/running-apps-with-jobs.html) documentation.


### Allocations

All new Alpine users are granted an initial allocation (account) called `ucb-general`. Users who require more core hours than `ucb-general` can provide are advised to apply for an allocation. The allocation process requires that users have run example jobs in ucb-general that can be assessed by RC for efficiency/optimation on Alpine. Research Computing will then work with users to make workflows more efficient if needed and then grant the allocation.

You can read more about the allocation process and why you might choose to apply for one on our [Allocation's page](../../access/allocations.md).

> _**Note:**_ For Alpine early adopters, you may finish off your Summit project year on Alpine (i.e. port pro-rated Summit SUs ath the same level). For example, if you have 3 months left on an 1.2M SU grant, we can port 300k SU to Alpine.

Alpine is jointly funded by the University of Colorado Boulder, the University of Colorado Anschutz, Colorado State University, and the National Science Foundation (award 2201538).

Couldn't find what you need? [Provide feedback on these docs!](https://forms.gle/bSQEeFrdvyeQWPtW9)
