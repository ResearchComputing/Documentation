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


| Count & Type          | Partition | Processor        | Sockets | Cores (total) | Threads per Core | RAM per Core (GB) | GPU type    | GPU count | Local Disk Capacity & Type | Fabric                                       |
| --------------------- | ------------------- | ---------------- | :-------: | :-------------: | :------------: | :-------------: | ----------- | :---------: | -------------------------- | -------------------------------------------- |
| {{ alpine_ucb_total_64_core_256GB_cpu_nodes }} Milan General CPU | amilan              | x86_64 AMD Milan | 1 or 2  | 64            | 1            |  {{ alpine_standard_ram_per_core }}         | N/A         | 0         | 416G SSD                   | HDR-100 InfiniBand (200Gb inter-node fabric) |
| {{ alpine_ucb_total_128_core_256GB_cpu_nodes }} Milan CPU | amilan             | x86_64 AMD Milan | 2  | 128            | 1            |  {{ alpine_standard_ram_per_core }}         | N/A         | 0         | 416G SSD | HDR-100 InfiniBand (200Gb inter-node fabric) |
| {{ alpine_ucb_total_48_core_1TB_cpu_nodes }} Milan High-Memory  | amem                | x86_64 AMD Milan | 2       | 48            | 1            | 21.5          | N/A         | 0         | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       |
| {{ alpine_ucb_total_64_core_1TB_cpu_nodes }} Milan High-Memory   | amem                | x86_64 AMD Milan | 1       | 64            | 1            |  16           | N/A         | 0         | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       |
| {{ alpine_ucb_total_mi100_gpu_nodes }} Milan AMD GPU | ami100              | x86_64 AMD Milan | 2       | 64            | 1            |  {{ alpine_standard_ram_per_core }}           | AMD MI100   | 3         | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       |
| {{ alpine_ucb_total_a100_gpu_nodes }} Milan NVIDIA GPU    | aa100               | x86_64 AMD Milan | 2       | 64            | 1            |  {{ alpine_standard_ram_per_core }}           | NVIDIA A100 | 3         | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       |
| {{ alpine_ucb_total_gh200_gpu_nodes }} Grace CPU NVIDIA Hopper GPU    | gh200<br><br>Note: these nodes are only available upon request, please submit a [support request form](https://colorado.service-now.com/req_portal?id=ucb_sc_rc_form). | ARM Neoverse V2 | 1       | 72            | 1            |  6.6          | NVIDIA Hopper GPU | 1         | 1.8 T SSD                   | 2x25 Gb Ethernet +RoCE                       |
| {{ alpine_ucb_total_acompile_nodes }} Milan CPU compile nodes | acompile | x86_64 AMD Milan | 1 or 2  | 64            | 1            |  {{ alpine_standard_ram_per_core }}           | N/A         | 0         | 416G SSD                   | HDR-100 InfiniBand (200Gb inter-node fabric) |
| {{ alpine_ucb_total_64_core_256GB_cpu_nodes_atesting }} Milan CPU test nodes; pulls from CU amilan pool | atesting | x86_64 AMD Milan | 1 or 2  | 64            | 1            |  {{ alpine_standard_ram_per_core }}           | N/A         | 0         | 416G SSD                   | HDR-100 InfiniBand (200Gb inter-node fabric) |
| {{ alpine_ucb_total_a100_test_gpu_nodes }} Milan NVIDIA GPU testing node | aa100 (requested using the gpu-testing QoS) | x86_64 AMD Milan | 2       | 64            | 1            |  {{ alpine_standard_ram_per_core }}           | NVIDIA A100 | 3 (each split by MIG)        | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       |
| {{ alpine_ucb_total_mi100_test_gpu_nodes }} Milan AMD GPU testing nodes; pulls from ami100 pool | ami100 (requested using the gpu-testing QoS) | x86_64 AMD Milan | 2       | 64            | 1            |  {{ alpine_standard_ram_per_core }}           | AMD MI100   | 3         | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       |

:::

### CU Anschutz Medical Campus contribution

:::{table}
:width: 95%
:widths: auto
:align: left

| Count & Type          | Partition | Processor        | Sockets | Cores (total) | Threads per Core | RAM per Core (GB) | GPU type    | GPU count | Local Disk Capacity & Type | Fabric                                       |
| --------------------- | ------------------- | ---------------- | :-------: | :-------------: | :------------: | :-------------: | ----------- | :---------: | -------------------------- | -------------------------------------------- |
| {{ alpine_amc_total_64_core_256GB_cpu_nodes }} Milan General CPU  | amilan         | x86_64 AMD Milan | 1       | 64            | 1            |  {{ alpine_standard_ram_per_core }}           | N/A         | 0         | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       |
| {{ alpine_amc_total_64_core_1TB_cpu_nodes }} Milan High-Memory   | amem           | x86_64 AMD Milan | 1       | 64            | 1            |  16          | N/A         | 0         | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       | 
| {{ alpine_amc_total_128_core_2TB_cpu_nodes }} Milan High-Memory   | amem           | x86_64 AMD Milan | 2       | 128           | 1            |  16           | N/A         | 0         |  70G SSD                   | HDR-100 InfiniBand (200Gb inter-node fabric) | 
| {{ alpine_amc_total_a100_gpu_nodes }} Milan NVIDIA GPU    | aa100          | x86_64 AMD Milan | 1       | 64            | 1            |  {{ alpine_standard_ram_per_core }}           | NVIDIA A100 | 3         | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       |
| {{ alpine_amc_total_l40_gpu_nodes }} Milan NVIDIA GPU    | al40           | x86_64 AMD Milan | 2       | 64            | 1            |  {{ alpine_standard_ram_per_core }}           | NVIDIA L40  | 3         | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       | 

:::

### Colorado State University contribution

:::{table}
:width: 95%
:widths: auto
:align: left

| Count & Type          | Partition | Processor        | Sockets | Cores (total) | Threads per Core | RAM per Core (GB) | GPU type    | GPU count | Local Disk Capacity & Type | Fabric                                       |
| --------------------- | ------------------- | ---------------- | :-------: | :-------------: | :------------: | :-------------: | ----------- | :---------: | -------------------------- | -------------------------------------------- |
| {{ alpine_csu_total_48_core_256GB_cpu_nodes }} Milan General CPU  | amilan         | x86_64 AMD Milan | 2       | 48            | 1            |  {{ alpine_standard_ram_per_core }}           | N/A         | 0         | 416G SSD                   | HDR-100 InfiniBand (200Gb inter-node fabric) |
| {{ alpine_csu_total_32_core_256GB_cpu_nodes }} Milan General CPU  | amilan         | x86_64 AMD Milan | 2       | 32            | 1            |  {{ alpine_standard_ram_per_core }}           | N/A         | 0         | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       | 
:::


## Requesting Hardware Resources
Resources are requested within jobs by passing in SLURM directives, or resource flags, to either a job script (most common) or to the command line when submitting a job. Below are some common resource directives for Alpine (summarized then detailed):
* [Partition](#partitions): Specifies node type
* [Quality of Service (qos)](#quality-of-service-qos): Constrains or modifies job characteristics
* [General Resources (gres)](#general-resources-gres): Specifies the number and type of GPU you would like to request (*required if using a GPU node*)

### Partitions

**Nodes with the same hardware configuration are grouped into partitions**. You specify a partition using the `--partition` SLURM directive in your job script (or at the command line when submitting an interactive job) in order for your job to run on the appropriate type of node. 

```{note}
- GPU nodes require the additional `--gres` directive (see [General Resources (gres)](#general-resources-gres))
- For resource limitations of hardware (e.g. maximum walltime and job submissions) see the sections [Quality of Service (qos)](#quality-of-service-qos) and [General Resources (gres)](#general-resources-gres)
- For more information on special-purpose resources that provide quicker access to testing resources, see [Special-Purpose Resources](#special-purpose-resources)
```

#### Partitions available on Alpine:


| Partition | Description                  | # of nodes | cores/node | RAM/core (GB) | Billing_weight/core | 
| --------- | ---------------------------- | ---------- | ---------- | ------------- | ------------------- |
| amilan    | AMD Milan (default)          | {{ alpine_total_amilan_nodes }}        | 32 or 48 or 64 or 128 |   {{ alpine_standard_ram_per_core }}         | 1                   | 
| ami100    | GPU-enabled (3x AMD MI100)   | {{ alpine_total_ami100_nodes }}          | 64         |   {{ alpine_standard_ram_per_core }}         | 6.1<sup>3</sup>     |
| aa100     | GPU-enabled (3x NVIDIA A100)<sup>4</sup>. For select nodes, MIG has been enabled providing 6x 20 GB NVIDIA A100 MIG instances. | {{ alpine_total_aa100_nodes }}          | 64         |   {{ alpine_standard_ram_per_core }}        | 6.1<sup>3</sup>     | 
| al40      | GPU-enabled (3x NVIDIA L40)<sup>4</sup> | {{ alpine_total_al40_nodes }}          | 64         |   {{ alpine_standard_ram_per_core }}        | 6.1<sup>3</sup>     |
| amem<sup>1</sup> | High-memory           | {{ alpine_total_amem_nodes }}          | 48 or 64 or 128     |  16<sup>2</sup> | 4.0           |
| acompile | AMD Milan compile nodes | {{ alpine_total_acompile_nodes }} | 64 |   {{ alpine_standard_ram_per_core }}         | N/A                   | 
| atesting | AMD Milan test nodes | {{ alpine_total_atesting_cpu_nodes }}; Pulls from CU amilan pool | 64 |   {{ alpine_standard_ram_per_core }}         | 0.025                   |  
| gh200 | NVIDIA Grace-Hopper (GH200) nodes<br><br>Note: this partition is only available upon request, please submit a [support request form](https://colorado.service-now.com/req_portal?id=ucb_sc_rc_form). | {{ alpine_ucb_total_gh200_gpu_nodes }} | 72        |   6.65       | Billed at roughly twice the rate of our A100s   | 

```{important}
**Partition table footnotes:** 


<sup>1</sup>The `amem` partition requires the use of either the `mem-normal` or `mem-long` QOS. These QOS require that each job request 256GB of RAM or more.

<sup>2</sup>The `amem` partition has a mixture of nodes with 48, 64, and 128 cores.  Nodes with 48 and 64 cores have 1 TB of RAM; nodes with 128 cores have 2 TB of RAM.  The default RAM-per-requested core on the `amem` partition is 15,927 MB, which is configured such that if you request all 64 (128) cores on a 64-core (128-core) `amem` node, you will receive roughly 1,000,000 MB of RAM (i.e., the full ~1 TB available). If you request all 48 cores on a 48-core node, by default you will receive 764,496 MB of RAM, which is less than the 1 TB available. If you require more RAM than the default of 15,927 MB per-requested-core, employ the `--mem` flag in your job script and specify the amount of RAM you need, in MB. For example, to request all of the RAM on a node, use "--mem=1000000M".   

<sup>3</sup>On the GPU partitions, `ami100`, `aa100`, and `al40`, the _billing_weight_ value of 6.1/core is an aggregate estimate and will be smaller for MIG instances. In practice, users are billed 1.0 for each core they request and an amount for each GPU they request (which is defined by GPU type). For the amount charged per GPU type, see the `Billing_weight/GPU` column in the table provided in the section [Available GRES on Alpine](#available-gres-on-alpine). For example, if a user requests all 64 cores and three `a100-40gb` GPUs for one hour, they will be billed (1.0 * 64) + (108.6 * 3)=389.8 SUs. 

<sup>4</sup>NVIDIA A100 and L40 GPUs only support CUDA versions >11.x
```

All users, regardless of institution, should specify partitions as follows:
```bash
--partition=amilan
--partition=aa100
--partition=ami100
--partition=al40
--partition=amem
```

### Quality of Service (qos)

**Quality of Service or QoS is used to constrain or modify the characteristics that a job can have.** For example, by selecting the `long` QoS, a user can place the job in a **lower priority queue** with a max wall time increased from 24 hours to 7 days.

#### Available QoS for Alpine:

| QOS name    | Description                | Max walltime    | Max jobs/user | Max hardware/user        | Valid Partitions | 
| ----------- | -------------------------- | --------------- | ------------- | ------------------ | ---------------- |
| normal | Standard QoS for non-testing partitions                    | 1 day              | 1000          | 128 nodes                | amilan  |
| long | Longer wall times          | 7 days              | 200           | 20 nodes               | amilan            | 
| mem-normal | Standard QoS for High-memory jobs           | 24 hours              | 1000          | 256 CPU cores                | amem        | 
| mem-long | QoS for longer running High-memory jobs           | 7 days              | 200          | 185 CPU cores                | amem       | 
| gpu-normal | Standard QoS for GPU jobs        |  24 hours             |    1000      | see [Available GRES on Alpine](#available-gres-on-alpine) |  aa100,ami100,al40     | 
| gpu-long |  QoS for longer running GPU jobs          |   7 days            |    200      | see [Available GRES on Alpine](#available-gres-on-alpine)  | aa100,ami100,al40 | 
| gpu-testing | Testing QoS for GPU jobs        | 1 hour | 5 | see [Available GRES on Alpine](#available-gres-on-alpine) |  aa100,ami100     | 
| testing | Used for all testing partitions   | 1 hour              | 5          |  2 nodes      | atesting     | 
| compile | Used for acompile jobs  | 12 hours              |    4     |   1 node      | acompile   | 
| gh200 | Used for GH200 jobs<br><br>Note: this QoS is only available upon request, please submit a [support request form](https://colorado.service-now.com/req_portal?id=ucb_sc_rc_form). | 7 days             |   1       |   1 node      | gh200  | 

#### QoS examples

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


### General Resources (gres)

**General resources allows for fine-grain hardware specifications**. On Alpine, the `gres` directive is _**required**_ to use GPU accelerators on GPU nodes. The general form for specifying `gres` is as follows: `--gres=gpu:<GRES type>:N`. In this general form, `<GRES type>` specifies the type of GPU you want to run on within a given partition, and `N` is the number of GPUs you want to request. In the table below, we specify the available GRES types for each partition and common constraints associated with them.
````{note}
Alpine GPU resources and configurations can be viewed as follows on a login node (with the `slurm/alpine` module loaded):

```bash
$ sinfo --Format Partition,Gres |grep gpu
```
````

#### Available GRES on Alpine:

| GRES type   | Description                | Partition | `gpu-normal` GPU Resources | `gpu-long` GPU Resources | `gpu-testing` GPU Resources | Max cores/GPU | Billing_weight/GPU |
| ----------- | -------------------------- | --------------- | --------------- | ------------- | ------------------ | ------------------ | ------------------ | 
| `a100_3g.20gb` | NVIDIA A100 GPU with 20 GB of VRAM made possible by NVIDIA's [Multi-Instance GPU (MIG)](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html) feature |  `aa100` | N/A |  N/A | <ul><li>Total: 6</li><li>Max/user: 1</li></ul>   | 10 | 54.3 |
| `a100-40gb` | NVIDIA A100 GPU with 40 GB of VRAM |  `aa100` |  <ul><li>Total: 18</li><li>Max/user: 6</li></ul>   | <ul><li>Total: 6</li><li>Max/user: 3</li></ul> |  N/A | 21 | 108.6 |
| `a100_80gb` | NVIDIA A100 GPU with 80 GB of VRAM |  `aa100` |  <ul><li>Total: 10</li><li>Max/user: 3</li></ul>   | <ul><li>Total: 3</li><li>Max/user: 1</li></ul> |  N/A | 21 |  108.6 |
| `l40` | NVIDIA L40 GPU with 48 GB of VRAM |  `al40` |  <ul><li>Total: 7</li><li>Max/user: 3</li></ul>   | <ul><li>Total: 3</li><li>Max/user: 3</li></ul> |  N/A  | 21 |  108.6 |
| `mi100` | AMD MI100 GPU with 34 GB of VRAM |  `ami100` |  <ul><li>Total: 18</li><li>Max/user: 5</li></ul>   | <ul><li>Total: 6</li><li>Max/user: 3</li></ul> | <ul><li>Total: 3</li><li>Max/user: 1</li></ul>   | 21 |  108.6 |
| `gh200` | NVIDIA GH200 GPU with 102 GB of VRAM |  `gh200` | N/A  | N/A | N/A   | 72 |  260.64 |

```{important}
- The `Max/user` value is the concurrent GPU limit per user for a given GRES type. Jobs exceeding this limit are held in the queue and will only be eligible to run once the user's active GPU consumption falls below the threshold. 
- Resources belonging to `gpu-testing` are for verifying GPU workflows and building GPU-accelerated applications. Established workflows should be submitted to `gpu-normal` or `gpu-long`. 
- Resources requested via `gpu-testing` are currently only charged 10% of the provided CPU and GPU billing weights. 
- GH200 resources are part of the `gh200` QoS, which is only available to users upon request. To request access, please submit a [support request form](https://colorado.service-now.com/req_portal?id=ucb_sc_rc_form).
```

#### Examples of GRES Usage

(tabset-ref-ex-gpu-conf-req)=
`````{tab-set}
:sync-group: tabset-ex-gpu-conf-req

````{tab-item} One 40 GB A100 GPU
:sync: ex-gpu-conf-req-1-40-a100

**Request a single A100 GPU with 40 GB of VRAM.**

```bash
--gres=gpu:a100-40gb:1
```

````

```` {tab-item} Three MI100 GPUs
:sync: ex-gpu-conf-req-3-mi100

**Request multiple (in this case 3) MI100 GPUs.**

```bash
--gres=gpu:mi100:3
```

````

`````

# Special-Purpose Resources

To help users test out their workflows, CURC provides several special-purpose resources on Alpine. These resources enable users to quickly test or compile code on CPU and GPU compute nodes. To ensure equal access to these resources, the amount of resources (such as CPUs, GPUs, and runtime) are limited. 

```{important}
Compiling and testing resources are, as their name implies, only meant for compiling code and testing workflows. They are not to be used outside of compiling or testing. Please utilize the appropriate resources when running code. 
```

## Special-Purpose CPU-only Resources

CURC currently provides two types of special-purpose CPU-only resources on Alpine that are made available through the partitions `atesting` and `acompile`. 

### `acompile` usage

`acompile` provides near-immediate access to limited resources for the purpose of viewing the module stack, verifying non-MPI jobs, and compiling software. Users can request up to 4 CPU cores (but no GPUs) for a maximum runtime of 12 hours. The partition can be quickly accessed with the `acompile` command, which launches an interactive compute session. 

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

### `atesting` usage

The `atesting` partition provides access to limited resources for the purpose of verifying workflows and MPI jobs. Users are able to request up to 2 CPU nodes (8 cores per node) for a maximum runtime of 1 hour and 16 CPUs. 

(tabset-ref-atesting-use)=
`````{tab-set}
:sync-group: tabset-atesting-use

````{tab-item} Example 1
:sync: atesting-use-ex1

**Request one core per node for 10 minutes.**

```bash
sinteractive --partition=atesting --ntasks=2 --ntasks-per-node=1 --nodes=2 --qos=testing --time=00:10:00
```

````

```` {tab-item} Example 2
:sync: atesting-use-ex2

**Request 4 cores for 30 minutes.**

```bash
sinteractive --partition=atesting --ntasks=4 --nodes=1 --qos=testing --time=00:30:00 
```

````

```` {tab-item} Example 3
:sync: atesting-use-ex3

**Request 2 nodes with 2 cores per node for 10 minutes - a good option for testing MPI jobs.**

```bash
sinteractive --partition=atesting --ntasks=4 --ntasks-per-node=2 --nodes=2 --qos=testing --time=00:10:00
```

````
`````

## Special-Purpose GPU Resources

The `gpu-testing` QoS provides access to limited GPU resources for the purpose of verifying GPU workflows and building GPU-accelerated applications. Please note that the `gpu-testing` QoS must be used in conjunction with a chosen GPU partition and GPU type. For a list of resources that are available via `gpu-testing` as well as limitations of the QoS, see the sections [Quality of Service (qos)](#quality-of-service-qos) and [General Resources (gres)](#general-resources-gres). 

```{important}
- The `a100_3g.20gb` GPU type made available on the `gpu-testing` QoS is a NVIDIA [Multi-Instance GPU (MIG)](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html). MIG is a feature that can "slice" GPUs into multiple GPU instances. These GPU instances can be treated as a single GPU. The increase in available GPUs, and in effect increase in GPU access, provided by MIG does come with certain limitations. One important limitation is that MIG does not allow for multiple GPU instances to communicate with each other. This is the reason we limit users to just 1 GPU under the `gpu-testing` QoS for each GPU type. For more information on the limitations of MIG, please see NVIDIA's MIG [Application Considerations](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/latest/deployment-considerations.html#application-considerations) documentation. 
- Currently there are no testing resources for the L40 GPUs, however most workflows that successfully run on the `aa100` resources will work on the `al40` partition.
```

(tabset-ref-gpu-testing-use)=
`````{tab-set}
:sync-group: tabset-gpu-testing-use

````{tab-item} NVIDIA A100 GPU
:sync: gpu-testing-use-a100

**Request one 20 GB A100 MIG slice with 10 CPU cores for 30 minutes.**

```bash
sinteractive --partition=aa100 --gres=gpu:a100_3g.20gb:1 --ntasks=10 --nodes=1 --qos=gpu-testing --time=00:30:00 
```

````

```` {tab-item} AMD MI100 GPU
:sync: gpu-testing-use-mi100

**Request one MI100 GPU with 21 CPU cores for one hour.**

```bash
sinteractive --partition=ami100 --gres=gpu:mi100:1 --ntasks=21 --nodes=1 --qos=gpu-testing --time=00:60:00
```

````

`````

Alpine is jointly funded by the University of Colorado Boulder, the University of Colorado Anschutz, Colorado State University, and the National Science Foundation (award 2201538).

