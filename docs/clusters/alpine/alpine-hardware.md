# Alpine Hardware

## Hardware Summary

```{important}
All Alpine nodes are available to all users. For full details about node access, please read the [Alpine node access and FairShare policy](condo-fairshare-and-resource-access.md).
```

### University of Colorado Boulder contribution

:::{table}
:width: 95%
:widths: auto
:align: left

| Count & Type          | Partition | Processor        | Sockets | Cores (total) | Threads per Core | RAM per Core (GB) | L3 Cache (MB) | GPU type    | GPU count | Local Disk Capacity & Type | Fabric                                       | OS       |
| --------------------- | ------------------- | ---------------- | :-------: | :-------------: | :------------: | :-------------: | :-------------: | ----------- | :---------: | -------------------------- | -------------------------------------------- | -------- |
| {{ alpine_ucb_total_64_core_256GB_cpu_nodes }} Milan General CPU | amilan              | x86_64 AMD Milan | 1 or 2  | 64            | 1            |  3.8          | 32            | N/A         | 0         | 416G SSD                   | HDR-100 InfiniBand (200Gb inter-node fabric) | RHEL 8.4 |
| {{ alpine_ucb_total_128_core_256GB_cpu_nodes }} Milan CPU | amilan128c             | x86_64 AMD Milan | 2  | 128            | 1            |  2.01         | 32            | N/A         | 0         | 416G SSD | HDR-100 InfiniBand (200Gb inter-node fabric) | RHEL 8.8 |
| {{ alpine_ucb_total_48_core_1TB_cpu_nodes }} Milan High-Memory  | amem                | x86_64 AMD Milan | 2       | 48            | 1            | 21.5          | 32            | N/A         | 0         | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       | RHEL 8.4 |
| {{ alpine_ucb_total_64_core_1TB_cpu_nodes }} Milan High-Memory   | amem                | x86_64 AMD Milan | 1       | 64            | 1            |  16           | 32            | N/A         | 0         | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       | RHEL 8.4 |
| {{ alpine_ucb_total_mi100_gpu_nodes }} Milan AMD GPU | ami100              | x86_64 AMD Milan | 2       | 64            | 1            |  3.8          | 32            | AMD MI100   | 3         | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       | RHEL 8.4 |
| {{ alpine_ucb_total_a100_gpu_nodes }} Milan NVIDIA GPU    | aa100               | x86_64 AMD Milan | 2       | 64            | 1            |  3.8          | 32            | NVIDIA A100 | 3         | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       | RHEL 8.4 |
| {{ alpine_ucb_total_gh200_gpu_nodes }} Grace CPU NVIDIA Hopper GPU    | currently in beta testing              | ARM Neoverse V2 | 1       | 72            | 1            |  6.6          | 119.5            | NVIDIA Hopper GPU | 1         | 1.8 T SSD                   | 2x25 Gb Ethernet +RoCE                       | RHEL 9.5 |

:::

### CU Anschutz Medical Campus contribution

:::{table}
:width: 95%
:widths: auto
:align: left

| Count & Type          | Partition | Processor        | Sockets | Cores (total) | Threads per Core | RAM per Core (GB) | L3 Cache (MB) | GPU type    | GPU count | Local Disk Capacity & Type | Fabric                                       | OS       |
| --------------------- | ------------------- | ---------------- | :-------: | :-------------: | :------------: | :-------------: | :-------------: | ----------- | :---------: | -------------------------- | -------------------------------------------- | -------- |
| {{ alpine_amc_total_64_core_256GB_cpu_nodes }} Milan General CPU  | amc, amilan         | x86_64 AMD Milan | 1       | 64            | 1            |  3.8          | 32            | N/A         | 0         | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       | RHEL 8.4 |
| {{ alpine_amc_total_64_core_1TB_cpu_nodes }} Milan High-Memory   | amc, amem           | x86_64 AMD Milan | 1       | 64            | 1            |  16           | 32            | N/A         | 0         | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       | RHEL 8.4 |
| {{ alpine_amc_total_128_core_2TB_cpu_nodes }} Milan High-Memory   | amc, amem           | x86_64 AMD Milan | 2       | 128           | 1            |  16           | 32            | N/A         | 0         |  70G SSD                   | HDR-100 InfiniBand (200Gb inter-node fabric) | RHEL 8.4 |
| {{ alpine_amc_total_a100_gpu_nodes }} Milan NVIDIA GPU    | amc, aa100          | x86_64 AMD Milan | 1       | 64            | 1            |  3.8          | 32            | NVIDIA A100 | 3         | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       | RHEL 8.4 |
| {{ alpine_amc_total_l40_gpu_nodes }} Milan NVIDIA GPU    | amc, al40           | x86_64 AMD Milan | 2       | 64            | 1            |  3.8          | 32            | NVIDIA L40  | 3         | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       | RHEL 8.4 |

:::

### Colorado State University contribution

:::{table}
:width: 95%
:widths: auto
:align: left

| Count & Type          | Partition | Processor        | Sockets | Cores (total) | Threads per Core | RAM per Core (GB) | L3 Cache (MB) | GPU type    | GPU count | Local Disk Capacity & Type | Fabric                                       | OS       |
| --------------------- | ------------------- | ---------------- | :-------: | :-------------: | :------------: | :-------------: | :-------------: | ----------- | :---------: | -------------------------- | -------------------------------------------- | -------- |
| {{ alpine_csu_total_48_core_256GB_cpu_nodes }} Milan General CPU  | csu, amilan         | x86_64 AMD Milan | 2       | 48            | 1            |  3.8          | 32            | N/A         | 0         | 416G SSD                   | HDR-100 InfiniBand (200Gb inter-node fabric) | RHEL 8.4 |
| {{ alpine_csu_total_32_core_256GB_cpu_nodes }} Milan General CPU  | csu, amilan         | x86_64 AMD Milan | 2       | 32            | 1            |  3.8          | 32            | N/A         | 0         | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       | RHEL 8.4 |
:::


## Requesting Hardware Resources
Resources are requested within jobs by passing in SLURM directives, or resource flags, to either a job script (most common) or to the command line when submitting a job. Below are some common resource directives for Alpine (summarized then detailed):
* **Gres (General Resources):** Specifies the number of GPUs (*required if using a GPU node*)
* **QOS (Quality of Service):** Constrains or modifies job characteristics
* **Partition:** Specifies node type

### General Resources (gres)

**General resources allows for fine-grain hardware specifications**. On Alpine the `gres` directive is _**required**_ to use GPU accelerators on GPU nodes. At a minimum, one would specify `--gres=gpu` in their job script (or on the command line when submitting a job) to specify that they would like to use a single GPU on their specified partition. One can also request multiple GPU accelerators on nodes that have multiple accelerators. Alpine GPU resources and configurations can be viewed as follows on a login node with the `slurm/alpine` module loaded:

```bash
$ sinfo --Format Partition,Gres |grep gpu |grep -v -i amc
```

__Examples of GPU configurations/requests__:

(tabset-ref-ex-gpu-conf-req)=
`````{tab-set}
:sync-group: tabset-ex-gpu-conf-req

````{tab-item} Single GPU
:sync: ex-gpu-conf-req-single-gpu

**Request a single GPU accelerator.**

```bash
--gres=gpu
```

````

```` {tab-item} Multiple GPUs
:sync: ex-gpu-conf-req-multiple-gpu

**Request multiple (in this case 3) GPU accelerators.**

```bash
--gres=gpu:3
```

````

`````

### Quality of Service (qos)

**Quality of Service or QoS is used to constrain or modify the characteristics that a job can have.** For example, by selecting the `long` QoS, a user can place the job in a **lower priority queue** with a max wall time increased from 24 hours to 7 days.

The available QoS for Alpine:

| QOS name    | Description                | Max walltime    | Max jobs/user | Node limits        | Valid Partitions | 
| ----------- | -------------------------- | --------------- | ------------- | ------------------ | ---------------- |
| normal      | Standard QoS for non-testing partitions                    | 1 day              | 1000          | 128                | amilan,amilan128c,aa100,ami100  |
| long        | Longer wall times          | 7 days              | 200           | 20                | amilan,amilan128c,aa100,ami100              | 
| mem         | High-memory jobs           | 7 days              | 1000          | 12                 | amem only        | 
| testing         | Used for all testing partitions   | 1 hour              | 5          |  2       | atesting,atesting_a100,atesting_mi100     | 
| compile       | Used for acompile jobs  | 12 hours              |    -      |   1      | acompile   | 
| amc       | QoS for nodes contributed by AMC    | 24 hours              | -         |  -       | amc  | 
| csu       | QoS for nodes contributed by CSU    | 24 hours              |  -        |  -       | csu  | 
| rmacc       | QoS for nodes contributed by RMACC    | 24 hours              |    -      |   -      | rmacc  | 
| gh200       | Used for GH200 jobs (available only through request)   | 7 days             |   1       |   1      | gh200  | 

__QoS examples__:

(tabset-ref-ex-qos-req)=
`````{tab-set}
:sync-group: tabset-ex-qos-req

````{tab-item} Requesting the normal partition 
:sync: ex-qos-req-normal-partition

```bash
--qos=normal
```

````

```` {tab-item} Requesting the long partition
:sync: ex-qos-req-long-partition

```bash
--qos=long
```

````

`````


### Partitions

**Nodes with the same hardware configuration are grouped into partitions**. You specify a partition using the `--partition` SLURM directive in your job script (or at the command line when submitting an interactive job) in order for your job to run on the appropriate type of node. 

```{note}
GPU nodes require the additional `--gres` directive (see above section).
```

Partitions available on Alpine:


| Partition | Description                  | # of nodes | cores/node | RAM/core (GB) | Billing_weight/core | Default/Max Walltime     | Resource Limits |
| --------- | ---------------------------- | ---------- | ---------- | ------------- | ------------------- | ------------------------ | ----------------------|
| amilan    | AMD Milan (default)          | {{ alpine_total_amilan_nodes }}        | 32 or 48 or 64 |   3.75        | 1                   | 24H, 7D                 | see qos table |
| amilan128c    | AMD Milan        | {{ alpine_total_amilan128c_nodes }}        | 128 |   2.01        | 1                   | 24H, 7D      | see qos table |
| ami100    | GPU-enabled (3x AMD MI100)   | {{ alpine_total_ami100_nodes }}          | 64         |   3.75        | 6.1<sup>3</sup>     | 24H, 7D                 | 15 GPUs across all jobs |
| aa100     | GPU-enabled (3x NVIDIA A100)<sup>4</sup> | {{ alpine_total_aa100_nodes }}          | 64         |   3.75       | 6.1<sup>3</sup>     | 24H, 7D     | 21 GPUs across all jobs |
| al40      | GPU-enabled (3x NVIDIA L40)<sup>4</sup> | {{ alpine_total_al40_nodes }}          | 64         |   3.75       | 6.1<sup>3</sup>     | 24H, 7D     | 6 GPUs across all jobs |
| amem<sup>1</sup> | High-memory           | {{ alpine_total_amem_nodes }}          | 48 or 64 or 128     |  16<sup>2</sup> | 4.0           |  4H,  7D                 | 128 cores across all jobs |
| csu       | Nodes contributed by CSU     | {{ alpine_total_csu_nodes }}         | 32 or 48   |   3.75        | 1                   | 24H, 7D                 | see qos table |
| amc       | Nodes contributed by AMC     | {{ alpine_total_amc_nodes }}        | 32 or 48   |   3.75        | 1                   | 24H, 7D                 | see qos table |

```{important}
**Partition table footnotes:** 


<sup>1</sup>The `amem` partition requires the mem QOS. The mem QOS is only available to jobs asking for 256GB of RAM or more, 12 nodes or fewer, and 128 cores or fewer. For example, you can run one 128-core job or up to two 64-core jobs, etc. If you need more memory or cores, please contact <rc-help@colorado.edu>.

<sup>2</sup>The `amem` partition has a mixture of nodes with 48, 64, and 128 cores.  Nodes with 48 and 64 cores have 1 TB of RAM; nodes with 128 cores have 2 TB of RAM.  The default RAM-per-requested core on the `amem` partition is 15,927 MB, which is configured such that if you request all 64 (128) cores on a 64-core (128-core) `amem` node, you will receive roughly 1,000,000 MB of RAM (i.e., the full ~1 TB available). If you request all 48 cores on a 48-core node, by default you will receive 764,496 MB of RAM, which is less than the 1 TB available. If you require more RAM than the default of 15,927 MB per-requested-core, employ the `--mem` flag in your job script and specify the amount of RAM you need, in MB. For example, to request all of the RAM on a node, use "--mem=1000000M".   

<sup>3</sup>On the GPU partitions, `ami100`, `aa100`, and `al40`, the _billing_weight_ value of 6.1/core is an aggregate estimate. In practice, users are billed 1.0 for each core they request, and 108.2 for each GPU they request. For example, if a user requests all 64 cores and all three GPUs for one hour, they will be billed (1.0 * 64) + (108.2 * 3)=389 SUs.

<sup>4</sup>NVIDIA A100 and L40 GPUs only support CUDA versions >11.x
```

All users, regardless of institution, should specify partitions as follows:
```bash
--partition=amilan
--partition=amilan128c
--partition=aa100
--partition=ami100
--partition=al40
--partition=amem
--partition=csu
--partition=amc
```

#### Special-Purpose Partitions

To help users test out their workflows, CURC provides several special-purpose partitions on Alpine. These partitions enable users to quickly test or compile code on CPU and GPU compute nodes. To ensure equal access to these special-purpose partitions, the amount of resources (such as CPUs, GPUs, and runtime) are limited. 

```{important}
Compiling and testing partitions are, as their name implies, only meant for compiling code and testing workflows. They are not to be used outside of compiling or testing. Please utilize the appropriate partitions when running code. 
```

##### `atesting` usage examples:

`atesting` provides access to limited resources for the purpose of verifying workflows and MPI jobs. Users are able to request up to 2 CPU nodes (8 cores per node) for a maximum runtime of 1 hour (default  1 hour) and 16 CPUs. Users who need GPU nodes to test workflows should use the appropriate GPU testing partitions (`atesting_a100` or `atesting_mi100`) instead of `atesting`.

(tabset-ref-atesting-use)=
`````{tab-set}
:sync-group: tabset-atesting-use

````{tab-item} Example 1
:sync: atesting-use-ex1

**Request one core per node for 10 minutes.**

```bash
sinteractive --partition=atesting --ntasks-per-node=1 --nodes=2 --time=00:10:00
```

````

```` {tab-item} Example 2
:sync: atesting-use-ex2

**Request 4 cores for the default time of 30 minutes.**

```bash
sinteractive --partition=atesting --ntasks=4
```

````

```` {tab-item} Example 3
:sync: atesting-use-ex3

**Request 2 cores each from 2 nodes for testing MPI.**

```bash
sinteractive --ntasks-per-node=2 --nodes=2 --partition=atesting
```

````
`````

##### GPU `atesting` usage examples:

`atesting_a100` and `atesting_mi100` provide access to limited GPU resources for the purpose of verifying GPU workflows and building GPU-accelerated applications. For the `atesting_mi100` partition, users can request up to 3 GPUs and all associated CPU cores (64 max) from a single node for up to one hour. Due to limitations with MIG (see below), we limit users to 1 GPU (with 20 GB of VRAM) and at most 10 CPU cores on the `atesting_a100` partition.  Currently there is no testing partition for the L40 GPUs, however most workflows that successfully test on the `atesting_a100` partition will work on the `al40` partition.

```{important}

The `atesting_a100` partition utilizes NVIDIA's [Multi-Instance GPU (MIG)](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html) feature, which can "slice" GPUs into multiple GPU instances. These GPU instances can be treated as a single GPU. The increase in available GPUs, and in effect increase in GPU access, provided by MIG does come with certain limitations. One important limitation is that MIG does not allow for multiple GPU instances to communicate with each other. This is the reason we limit users to just 1 GPU on the `atesting_a100` partition. For more information on limitations of MIG, please see NVIDIA's MIG [Application Considerations](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#application-considerations) documentation. 
```

(tabset-ref-gpu-atesting-use)=
`````{tab-set}
:sync-group: tabset-gpu-atesting-use

````{tab-item} Example 1
:sync: gpu-atesting-use-ex1

**Request 1 A100 MIG slice with 10 CPU cores for 30 minutes.**

```bash
sinteractive --partition=atesting_a100 --gres=gpu --ntasks=10 --time=30:00
```

````

```` {tab-item} Example 2
:sync: gpu-atesting-use-ex2

**Request 1 MI100 GPU with 1 CPU core for one hour.**

```bash
sinteractive --partition=atesting_mi100 --gres=gpu:1 --ntasks=1 --time=60:00
```

````

`````

##### `acompile` usage examples:

`acompile` provides near-immediate access to limited resources for the purpose of viewing the module stack, verifying non-MPI jobs, and compiling software. Users can request up to 4 CPU cores (but no GPUs) for a maximum runtime of 12 hours. The partition is accessed with the `acompile` command. Users who need GPU nodes to compile software should use Slurm's `sinteractive` command with the appropriate GPU partition (`ami100` or `aa100`) instead of `acompile`.

(tabset-ref-acompile-use)=
`````{tab-set}
:sync-group: tabset-acompile-use

````{tab-item} Example 1
:sync: acompile-use-ex1

**Get usage information for `acompile`.**

```bash
acompile --help
```

````

```` {tab-item} Example 2
:sync: acompile-use-ex2

**Request 2 CPU cores for 2 hours.**

```bash
acompile --ntasks=2 --time=02:00:00
```

````

`````

Alpine is jointly funded by the University of Colorado Boulder, the University of Colorado Anschutz, Colorado State University, and the National Science Foundation (award 2201538).

