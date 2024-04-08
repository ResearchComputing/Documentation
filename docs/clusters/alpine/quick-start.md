## Alpine Quick Start

Alpine is the University of Colorado Boulder Research Computing's third-generation high performance computing (HPC) 
cluster. Alpine is a heterogeneous compute cluster currently composed of hardware provided from University of Colorado 
Boulder, Colorado State University, and Anschutz Medical Campus. Alpine currently offers 382 compute nodes and a total 
of 22,180 cores. Alpine can be securely accessed anywhere, anytime using Open OnDemand or ssh connectivity to the CURC system.

### Alpine Quick-Start

1. From a *login node* load the `slurm/alpine` module to access the SLURM job scheduler instance for Alpine:
   ```bash
   $ module load slurm/alpine
   ```

2. Once the Alpine Slurm job scheduler has been loaded you can submit and start jobs on the Alpine cluster. Consult the [requesting resources](#requesting-resources) section and the [examples](#examples) section below to learn how to direct your jobs to the appropriate Alpine compute nodes.

3. Software can be loaded into the Alpine compute environment via the LMOD [module system](../../compute/modules), which allows users choose software from our pre-installed software stack.

4. If you would like to use software that is not within our preinstalled stack your application 
must be compiled using `acompile`. More information about the `acompile` function can be found under our 
[partitions](./alpine-hardware.html#partitions) 
section.

Consult our [compiling and linking documentation](../../compute/compiling) for more information on compiling software. 
You can also submit a [software 
request](./software.html#alpine-software-policy) using our [Software Request Form](https://www.colorado.edu/rc/userservices/software-request).

### Cluster Summary
#### Nodes
The Alpine cluster is made up of different types of nodes outlined below:
- **CPU nodes**: 347 AMD Milan compute nodes (270 nodes with 64 cores/node, 28 nodes with 48 cores/node, 49 nodes with 32 cores/node) with 256 GB RAM
- **GPU nodes**:
	- 8 GPU-enabled (3x AMD MI100) atop AMD Milan CPU
	- 12 GPU-enabled (3x NVIDIA A100) atop AMD Milan CPU
- **High-memory nodes**: 12 AMD Milan nodes with 1TB of memory

Alpine also includes nodes contributed by partner institutions. Contributors with nodes in either deployment or production are:
- **Colorado State University**: 77 AMD Milan compute nodes (28 nodes with 48 cores/node, 49 nodes with 32 cores/node)
- **CU Anschutz Medical Campus**: 14 AMD Milan compute nodes (64 cores/node), 2 AMD Milan nodes with 1TB of RAM, and 4 GPU-enabled (3x NVIDIA A100 atop AMD Milan)

All nodes are available to all users. For full details about node access, please read the [Alpine node access and FairShare policy](./condo-fairshare-and-resource-access).

> For a full list of nodes on Alpine use the command:  `scontrol show nodes`. Get single node details with the `scontrol show nodes <node name>` command.

#### Interconnect
The Alpine cluster has different types of interconnects/fabrics which connect different types of hardware, outlined below:
- **CPU nodes**: HDR-100 InfiniBand (200Gb inter-node fabric); available on most CPU nodes as of July 2023 and on most remaining CPU nodes pending hardware arrivals
- **GPU nodes**: 2x25 Gb Ethernet +RoCE
- **High-memory nodes**: 2x25 Gb Ethernet +RoCE
- **Scratch storage**: 25Gb Ethernet +RoCE

### Node Features
The Alpine cluster features some heterogeneity. A variety of feature tags are applied to nodes deployed in Alpine to allow jobs to target specific CPU, GPU, network, and storage requirements.

Use the `sinfo` command to determine the features that are available on any node in the cluster.

> _**Note:**_ **Feature descriptions and finalized partitions names are still being added to Alpine nodes. Refer to the description of features list below for current node features.**

```bash
sinfo --format="%N | %f"
```

#### Description of features
- **Milan**: 64-core and dual-socket 32-core AMD Milan EPYC CPU
- **A100**: NVIDIA A100 GPU
- **MI100**: AMD MI100 GPU
- **storage**: large, fast RAID disk storage in node
- **rhel8**: RedHat Enterprise Linux version 8 operating system

### Job Scheduling

All jobs on Alpine are run through a queue system using the SLURM job scheduler. Though many HPC workflows are run through batch-type jobs, interactive jobs on compute nodes are allowed but these must also be initiated through the scheduler. High-priority jobs move to the top of the queue and are thus guaranteed to start running within a few minutes, unless other high-priority jobs are already queued or running ahead of them. High-priority jobs can run for a maximum wall time of 24 hours. Low-priority jobs have a maximum wall time of 7 days.

More details about how to use SLURM to run jobs can be found in our [running applications with jobs](../../running-jobs/running-apps-with-jobs) documentation.


### Allocations

When you receive a Research Computing account you are automatically assigned a **Trailhead Auto-Allocation**, which grants you a fixed share of `ucb-general`. The Trailhead is a great allocation for smaller jobs or testing and benchmarking your code. To accommodate a variety of allocation sizes on Alpine, CURC offers two application-based tiers. The **Ascent Allocation** tier provides users with 250,000 SUs over a 12 month period. The **Peak Allocation** tier is aimed at projects that will consume between 250,000 and 5,000,000 SUs in a 12 month period. Please see our [Allocations page](./allocations) for a comparison of tiers and instructions to apply.

Alpine is jointly funded by the University of Colorado Boulder, the University of Colorado Anschutz, Colorado State University, and the National Science Foundation (award 2201538).


