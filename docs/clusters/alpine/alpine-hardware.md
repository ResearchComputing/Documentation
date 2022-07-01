## Alpine Hardware

### Hardware Summary

| Count & Type | Scheduler Partition | Processor | Sockets | Cores (total) | Threads/Core | Clock (GHz) | RAM (GB) | L3 Cache (MB) | GPU type | GPU count | Local Disk Capacity & Type | Fabric | OS |
| ------------ | ------------------- | --------- | ------- | ----- | ------------ | ----------- | -------- | -------- | - | --------- | -------------------------- | ------ | -- |
| 64 Milan General CPU | amilan-[institution] | x86_64  AMD Milan | 2 | 64 | 1 | 3.2 | 239 | 32 | | | 416G SSD | HDR-100 InfiniBand (200Gb inter-node fabric) | RHEL 8.4|
| 8 Milan AMD GPU | ami100-[institution] | x86_64  AMD Milan | 2 | 64 | 1 | 3.2 | 239 | 32 | AMD MI100 | 3 | 416G SSD | 2x25 Gb Ethernet +RoCE | RHEL 8.4 |
| 8 Milan NVIDIA GPU | aa100-[institution] | x86_64  AMD Milan | 2 | 64 | 1 | 3.2 | 239 | 32 | NVIDIA A100 | 3 | 416G SSD | 2x25 Gb Ethernet +RoCE | RHEL 8.4 |


### Requesting Hardware Resources
Resources are requested within jobs by passing in SLURM directives, or resource flags, to either a job script (most common) or to the command line when submitting a job. Below are some common resource directives for Alpine (summarized then detailed):
* **Partition:** Specify node type
* **Gres (General Resources):** Specify GPU amount (*required if using a GPU node*)
* **QOS (Quality of Service):** Constrain or modify job characteristics


#### Partitions

**Nodes with the same hardware configuration are grouped into partitions**. You specify a partition using `--partition` SLURM directive in your job script (or at the command line when submitting an interactive job) in order for your job to run on the appropriate type of node. On Alpine nodes are also grouped by institution. You need to include your institutions suffix in order to request the required nodes.

> **Note:** GPU nodes require the additional `--gres` directive (see next section).

Partitions available on Alpine:


| Partition       | Description       | # of nodes | cores/node | RAM/core (GB) | Billing weight | Default/Max Walltime |
| --------------- | ----------------- | ---------- | ---------- | ------------- | -------------- | ------------------------ |
| amilan-[institute] | AMD Milan (default) | 64 | 64 | 3.74 | 1              | 4H, 24H                  |
| ami100-[institute] | GPU-enabled (3x AMD MI100) | 8 | 64 | 3.74 | tbd | 4H, 24H                  |
| aa100-[institute]* | GPU-enabled (3x NVIDIA A100) | 8 | 64 | 3.74 | tbd | 4H, 24H                  |

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

**General resources allows for fine-grain hardware specifications**. On Alpine the `gres` directive is _**required**_ to use GPU accelerators on GPU nodes. At a minimum, one would specify `--gres=gpu` in their job script (or on the command line when submitting a job) to specify that they would like to use a single gpu on their specified partition. One can also request multiple GPU accelerators on nodes that have multiple accelerators. Alpine GPU resources and configurations can be viewed as follows on a login node with the `slurm/alpine` module loaded:

```bash
$ sinfo --Format NodeList:30,Partition,Gres |grep gpu |grep -v "mi100\|a100"
```

__Examples of GPU configurations/requests__:

_request a single GPU accelerator:_
```
--gres=gpu
```
_request multiple (in this case 3) GPU accelerators:_
```
--gres=gpu:3
```

#### Quality of Service (qos)

**Quality of Service or QoS is used to constrain or modify the characteristics that a job can have.** This could come in the form of specifying a QoS to request for a longer run time. For example, by selecting the `long` QoS, a user can place the job in a **lower priority queue** with a max wall time increased from 24 hours to 7 days.

> Normally, this slurm directive does not need to be set for most jobs. Only set a QoS when requesting a long job.

The available QoS's for Summit are:

| QOS name    | Description                | Max walltime    | Max jobs/user | Node limits        | Partition limits | Priority Adjustment  |
| ----------- | -------------------------- | --------------- | ------------- | ------------------ | ---------------- | ---------------------|
| normal      | Default                    | 1D              | tbd | tbd | n/a              | 0 |
| long        | Longer wall times          | 7D              | tbd | tbd | tbd | 0 |

Alpine is jointly funded by the University of Colorado Boulder, the University of Colorado Anschutz, Colorado State University, and the National Science Foundation (award 2201538).

Couldn't find what you need? [Provide feedback on these docs!](https://forms.gle/bSQEeFrdvyeQWPtW9)
