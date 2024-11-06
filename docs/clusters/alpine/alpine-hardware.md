# Alpine Hardware

## Hardware Summary

| Count & Type          | Scheduler Partition | Processor        | Sockets | Cores (total) | Threads/Core | RAM/Core (GB) | L3 Cache (MB) | GPU type    | GPU count | Local Disk Capacity & Type | Fabric                                       | OS       |
| --------------------- | ------------------- | ---------------- | ------- | ------------- | ------------ | ------------- | ------------- | ----------- | --------- | -------------------------- | -------------------------------------------- | -------- |
| 285 Milan General CPU | amilan              | x86_64 AMD Milan | 1 or 2  | 64            | 1            |  3.8          | 32            | N/A         | 0         | 416G SSD                   | HDR-100 InfiniBand (200Gb inter-node fabric) | RHEL 8.4 |
| 12 Milan High-Memory  | amem                | x86_64 AMD Milan | 2       | 48            | 1            | 21.5          | tbd           | N/A         | 0         | 416G SSD                   | 2x25 Gb Ethernet +RoCE  | RHEL 8.4 |
| 10 Milan High-Memory   | amem                | x86_64 AMD Milan | 1       | 64            | 1            | 16          | tbd           | N/A         | 0         | 416G SSD                   | 2x25 Gb Ethernet +RoCE | RHEL 8.4 |
| 8 Milan AMD GPU       | ami100              | x86_64 AMD Milan | 2       | 64            | 1            |  3.8          | 32            | AMD MI100   | 3         | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       | RHEL 8.4 |
| 8 Milan NVIDIA GPU    | aa100               | x86_64 AMD Milan | 2       | 64            | 1            |  3.8          | 32            | NVIDIA A100 | 3         | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       | RHEL 8.4 |
| 28 Milan General CPU  | csu                 | x86_64 AMD Milan | 2       | 48            | 1            |  3.8          | 32            | N/A         | 0         | 416G SSD                   | HDR-100 InfiniBand (200Gb inter-node fabric)                       | RHEL 8.4 |
| 49 Milan General CPU  | csu                 | x86_64 AMD Milan | 2       | 32            | 1            |  3.8          | 32            | N/A         | 0         | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       | RHEL 8.4 |
| 14 Milan General CPU  | amc                 | x86_64 AMD Milan | 1       | 64            | 1            |  3.8          | 32            | N/A         | 0         | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       | RHEL 8.4 |
| 2 Milan High-Memory   | amc,amem            | x86_64 AMD Milan | 1       | 64            | 1            | 21.5          | 32            | N/A         | 0         | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       | RHEL 8.4 |
| 4 Milan NVIDIA GPU    | amc                 | x86_64 AMD Milan | 1       | 64            | 1            |  3.8          | 32            | NVIDIA A100 | 3         | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       | RHEL 8.4 |


## Requesting Hardware Resources
Resources are requested within jobs by passing in SLURM directives, or resource flags, to either a job script (most common) or to the command line when submitting a job. Below are some common resource directives for Alpine (summarized then detailed):
* **Gres (General Resources):** Specifies the number of GPUs (*required if using a GPU node*)
* **QOS (Quality of Service):** Constrains or modifies job characteristics
* **Partition:** Specifies node type

### General Resources (gres)

**General resources allows for fine-grain hardware specifications**. On Alpine the `gres` directive is _**required**_ to use GPU accelerators on GPU nodes. At a minimum, one would specify `--gres=gpu` in their job script (or on the command line when submitting a job) to specify that they would like to use a single GPU on their specified partition. One can also request multiple GPU accelerators on nodes that have multiple accelerators. Alpine GPU resources and configurations can be viewed as follows on a login node with the `slurm/alpine` module loaded:

```bash
$ sinfo --Format NodeList:30,Partition,Gres |grep gpu |grep -v "mi100|a100"
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

**Quality of Service or QoS is used to constrain or modify the characteristics that a job can have.** This could come in the form of specifying a QoS to request for a longer run time. For example, by selecting the `long` QoS, a user can place the job in a **lower priority queue** with a max wall time increased from 24 hours to 7 days.

The available QoS's for Alpine are:

| QOS name    | Description                | Max walltime    | Max jobs/user | Node limits        | Partition limits | Priority Adjustment  |
| ----------- | -------------------------- | --------------- | ------------- | ------------------ | ---------------- | ---------------------|
| normal      | Default                    | 1D              | 1000          | 128                | amilan,aa100,ami100              | 0                    |
| long        | Longer wall times          | 7D              | 200           | 20                 | amilan,aa100,ami100              | 0                    |
| mem         | High-memory jobs           | 7D              | 1000          | 12                 | amem only        | 0                    |


### Partitions

**Nodes with the same hardware configuration are grouped into partitions**. You specify a partition using the `--partition` SLURM directive in your job script (or at the command line when submitting an interactive job) in order for your job to run on the appropriate type of node. 

```{note}
GPU nodes require the additional `--gres` directive (see above section).
```

Partitions available on Alpine:


| Partition | Description                  | # of nodes | cores/node | RAM/core (GB) | Billing_weight/core | Default/Max Walltime     | Resource Limits |
| --------- | ---------------------------- | ---------- | ---------- | ------------- | ------------------- | ------------------------ | ----------------------|
| amilan    | AMD Milan (default)          | 376        | 32 or 48 or 64 |   3.75        | 1                   | 24H, 7D                 | see qos table |
| ami100    | GPU-enabled (3x AMD MI100)   | 8          | 64         |   3.75        | 6.1<sup>3</sup>     | 24H, 7D                 | 15 GPUs across all jobs |
| aa100     | GPU-enabled (3x NVIDIA A100)<sup>4</sup> | 12          | 64         |   3.75       | 6.1<sup>3</sup>     | 24H, 7D     | 22 GPUs across all jobs |
| amem<sup>1</sup> | High-memory           | 24          | 48 or 64      |  16<sup>2</sup> | 4.0           |  4H,  7D                 | 96 cores across all jobs |
| csu       | Nodes contributed by CSU     | 77         | 32 or 48   |   3.75        | 1                   | 24H, 7D                 | see qos table |

<sup>1</sup>The `amem` partition requires the mem QOS. The mem QOS is only available to jobs asking for 256GB of RAM or more, 12 nodes or fewer, and 96 cores or fewer. For example, you can run one 96-core job or up to two 48-core jobs, etc. If you need more memory or cores, please contact <rc-help@colorado.edu>.

<sup>2</sup>The `amem` partition has 12 nodes with 48 cores, and 12 nodes with 64 cores.  All nodes have 1 TB of RAM.  The default RAM-per-requested core on the `amem` partition is 15,927 MB, which is configured such that if you request all 64 cores on a 64-core `amem` node, you will receive roughly 1,000,000 MB of RAM (i.e., the full ~1 TB available). If you request all 48 cores on a 48-core node, by default you will receive 764,496 MB of RAM, which is less than the 1 TB available. If you require more RAM than the default of 15,927 MB per-requested-core, employ the `--mem` flag in your job script and specify the amount of RAM you need, in MB. For example, to request all of the RAM on a node, use "--mem=1000000M".   

<sup>3</sup>On the GPU partitions, `aa100` and `ami100`, the _billing_weight_ value of 6.1/core is an aggregate estimate. In practice, users are billed 1.0 for each core they request, and 108.2 for each GPU they request. For example, if a user requests all 64 cores and all three GPUs for one hour, they will be billed (1.0 * 64) + (108.2 * 3)=389 SUs.

<sup>4</sup>NVIDIA A100 GPUs only support CUDA versions >11.x

All users, regardless of institution, should specify partitions as follows:
```bash
--partition=amilan
--partition=aa100
--partition=ami100
--partition=amem
--partition=csu
```

#### Special-Purpose Partitions

`atesting` provides access to limited resources for the purpose of verifying workflows and MPI jobs. Users are able to request up to 2 CPU nodes (8 cores per node) for a maximum runtime of 3 hours (default 30 minutes) and 16 CPUs. Users who need GPU nodes to test workflows should use the appropriate GPU testing partitions (`atesting_a100` or `atesting_mi100`) instead of `atesting`.

##### `atesting` usage examples:

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

`atesting_a100` and `atesting_mi100` provide access to limited GPU resources for the purpose of verifying GPU workflows and building GPU-accelerated applications. Users can request up to 3 GPUs and all associated CPU cores (64 max) from a single node for up to one hour (default one hour).

##### GPU `atesting` usage examples:

(tabset-ref-gpu-atesting-use)=
`````{tab-set}
:sync-group: tabset-gpu-atesting-use

````{tab-item} Example 1
:sync: gpu-atesting-use-ex1

**Request 2 A100 GPUs with 40 CPU cores for 30 minutes.**

```bash
sinteractive --partition=atesting_a100 --gres=gpu:2 --ntasks=40 --time=30:00
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

`acompile` provides near-immediate access to limited resources for the purpose of viewing the module stack and compiling software. Users can request up to 4 CPU cores (but no GPUs) for a maximum runtime of 12 hours. The partition is accessed with the `acompile` command. Users who need GPU nodes to compile software should use Slurm's `sinteractive` command with the appropriate GPU partition (`ami100` or `aa100`) instead of `acompile`.

##### `acompile` usage examples:

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

