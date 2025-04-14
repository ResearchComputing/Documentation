# Alpine Quick Start

Alpine is the University of Colorado Boulder Research Computing's third-generation high performance computing (HPC) 
cluster. Alpine is a heterogeneous compute cluster currently composed of hardware provided from University of Colorado 
Boulder, Colorado State University, and Anschutz Medical Campus. Alpine currently offers {{ alpine_total_compute_nodes }} compute nodes and a total 
of {{ alpine_total_cores }} cores. Alpine can be securely accessed anywhere, anytime using Open OnDemand or ssh connectivity to the CURC system.

## Alpine Quick-Start

1. From a *login node*, load the `slurm/alpine` module to access the SLURM job scheduler instance for Alpine:
   ```bash
   $ module load slurm/alpine
   ```

2. Once the Alpine Slurm job scheduler has been loaded you can submit and start jobs on the Alpine cluster. Consult the [requesting resources](./alpine-hardware.md#requesting-hardware-resources) section and the [examples](slurm_directive_ex.md) section to learn how to direct your jobs to the appropriate Alpine compute nodes.

3. Software can be loaded into the Alpine compute environment via the LMOD [module system](../../compute/modules.md), which allows users choose software from our pre-installed software stack.

4. If you would like to use software that is not within our preinstalled stack, your application 
must be compiled using `acompile`. More information about the `acompile` command can be found under our 
[partitions](./alpine-hardware.md#partitions)
section.

Consult our [compiling and linking documentation](../../compute/compiling.md) for more information on compiling software. 
You can also submit a [software 
request](./software.md#alpine-software) using our [Software Request Form](https://www.colorado.edu/rc/userservices/software-request).

## Cluster Summary
### Nodes
The Alpine cluster is made up of different types of nodes. A general overview of these nodes is as follows: 
- **CPU nodes**: {{ alpine_total_256GB_cpu_nodes }} AMD Milan compute nodes with 256 GB RAM
- **GPU nodes**: a mixture of {{ alpine_total_gpu_nodes }} NVIDIA and AMD GPUs
- **High-memory nodes**: {{ alpine_total_hi_mem_cpu_nodes }} high-memory nodes with 1 TB of memory or more

Alpine is made possible due to its contributors. Below we provide each contributor, along with the number of nodes they have provided:
- **University of Colorado Boulder**: {{ ucb_alpine_total_nodes }} nodes
- **Colorado State University**: {{ csu_alpine_total_nodes }} nodes
- **CU Anschutz Medical Campus**: {{ amc_alpine_total_nodes }} nodes

```{note}
- For specific details on node types and a breakdown of contributions made to Alpine, please see the [Hardware Summary](./alpine-hardware.md#hardware-summary) section of our Alpine Hardware page. 
- All nodes are available to all users. For full details about node access, please read the [Alpine node access and FairShare policy](condo-fairshare-and-resource-access.md).
```

### Interconnect
The Alpine cluster has different types of interconnects/fabrics which connect different types of hardware, outlined below:
- **CPU nodes**: HDR-100 InfiniBand (200Gb inter-node fabric); available on most CPU nodes as of July 2023 and on most remaining CPU nodes pending hardware arrivals
- **GPU nodes**: 2x25 Gb Ethernet +RoCE
- **High-memory nodes**: 2x25 Gb Ethernet +RoCE
- **Scratch storage**: 25Gb Ethernet +RoCE

## Node Features
The Alpine cluster features some heterogeneity. A variety of feature tags are applied to nodes deployed in Alpine to allow jobs to target specific CPU, GPU, network, and storage requirements.

Use the `sinfo` command to determine the features that are available on any node in the cluster.

```bash
sinfo --format="%N | %f"
```

```{note}
**Feature descriptions and finalized partition names are still being added to Alpine nodes. Refer to the description of features list below for current node features.**
```

### Description of features
- **Milan**: 64-core and dual-socket 32-core AMD EPYC Milan CPU
- **A100**: NVIDIA A100 GPU
- **MI100**: AMD MI100 GPU
- **l40**: NVIDIA L40 GPU
- **storage**: large, fast RAID disk storage in node
- **rh8**: RedHat Enterprise Linux version 8 operating system

## Job Scheduling

All jobs on Alpine are run through a queue system using the SLURM job scheduler. Though many HPC workflows are run through batch-type jobs, interactive jobs on compute nodes are allowed; however, these jobs must also be initiated through the scheduler. High-priority jobs move to the top of the queue and are thus guaranteed to start running within a few minutes, unless other high-priority jobs are already queued or running ahead of them. High-priority jobs can run for a maximum wall time of 24 hours. Low-priority jobs have a maximum wall time of 7 days.

More details about how to use SLURM to run jobs can be found in our [running applications with jobs](../../running-jobs/running-apps-with-jobs.md) documentation.


## Allocations

When you receive a Research Computing account you are automatically assigned a **Trailhead Auto-Allocation**, which grants you a fixed share of `ucb-general`. The Trailhead is a great allocation for smaller jobs or testing and benchmarking your code. To accommodate a variety of allocation sizes on Alpine, CURC offers two application-based tiers. The **Ascent Allocation** tier provides users with {{ boulder_ascent_SUs }} SUs over a 12 month period. The **Peak Allocation** tier is aimed at projects that will consume between {{ boulder_ascent_SUs }} and {{ boulder_peak_SUs }} SUs in a 12 month period. Please see our [Allocations page](allocations.md) for a comparison of tiers and instructions to apply.

Alpine is jointly funded by the University of Colorado Boulder, the University of Colorado Anschutz, Colorado State University, and the National Science Foundation (award 2201538).


