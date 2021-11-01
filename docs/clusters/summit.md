## Summit

tbd

### Summit Quick-Start

1. From a login node, run "module load slurm/summit" to access the Slurm job scheduler instance for Summit.
2. Consult the Table and the Examples section below to learn how to direct your jobs to the appropriate compute nodes.
3. If needed, compile your application on the appropriate compute node type.

### Job Scheduling

All jobs are run through a batch/queue system.  Interactive jobs on compute nodes are allowed but these must be initiated through the scheduler.  High-priority jobs move to the top of the queue and are thus guaranteed to start running within a few minutes, unless other high-priority jobs are already queued or running ahead of them.  High-priority jobs can run for a maximum wall time of 7 days.  Low-priority jobs have a maximum wall time of 24 hours.

More details about how to use Slurm can be found [here](../running-jobs/running-apps-with-jobs.html).

### QoS

Slurm on Summit uses “Quality of Service”, or QoS, to classify jobs for scheduling.  A QoS in this case is analogous to a "queue" in other scheduling systems.  Each partner group has its own high-priority QoS called `summit-<group identifier>` and can also use the condo-wide low-priority QoS, which is called `preemptable`.

### Node-QoS-Features

To determine which nodes exist on the system, type `scontrol show nodes` to get a list.

tbd

### Node Features

The Summit cluster features some heterogeneity. A variety of feature tags are applied to nodes deployed in Summit to allow jobs to target specific CPU, GPU, network, and storage requirements.

Use the `sinfo` command to determine the features that are available on any node in the cluster.

```bash
sinfo --format="%N | %f"
```

The `sinfo` query may be further specified to look at the features available within a specific partition.

```bash
sinfo --format="%N | %f" --partition="summit-curc"
```

#### Description of features

- **A100**: NVIDIA A100 GPU  
- **MI100**: AMD MI100 GPU  
- **localraid**: large, fast RAID disk storage in node  
- **rhel8**: RedHat Enterprise Linux version 8 operating system  

#### Requesting GPUs in jobs

Using GPUs in jobs requires one to use the General Resource ("Gres") functionality of Slurm to request the gpu(s).  At a minimum, one would specify `#SBATCH --gres=gpu` in their job script to specify that they would like to use a single gpu of any type.  One can also request multiple GPUs on nodes that have more than one, and a specific type of GPU (e.g. A100, MI100) if desired.  The available Summit GPU resources and configurations can be viewed as follows on a login node with the `slurm/summit` module loaded:

```bash
$ sinfo --Format NodeList:30,Partition,Gres |grep gpu |grep -v "summit "
```

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

tbd

### Important notes

Not yet fully reviewed, subject to update:

1. To see what modules are available, start an interactive job on a compute node and use `module avail` or `module spider` on it.
2. /home, /projects, and /pl/active (PetaLibrary Active) are available on all Summit nodes.  Scratch I/O can be written to /rc_scratch, which should offer much better performance than /projects.  Most Summit nodes also have at least 400 GB of scratch space on a local disk, available to jobs as $SLURM_SCRATCH.  For more info on the different RC storage spaces, [please see our page on storage.](https://www.colorado.edu/rc/resources/filesystemstorage)
3. There are no dedicated Summit compile nodes.  To build software that will run on Summit, start an interactive job on a node like the one on which you expect your jobs to run, and compile your software there.  Do not compile on the login nodes!

### Summit Preemptable QOS

tbd

#### Usage

tbd

#### Best practices

Checkpointing: Given that preemptable jobs can request wall times up to 24 hours in duration, there is the possibility that users may lose results if they do not checkpoint. Checkpointing is the practice of incrementally saving computed results such that -- if a job is preempted, killed, canceled or crashes -- a given software package or model can continue from the most recent checkpoint in a subsequent job, rather than starting over from the beginning. For example, if a user implements hourly checkpointing and their 24 hour simulation job is preempted after 22.5 hours, they will be able to continue their simulation from the most recent checkpoint data that was written out at 22 hours, rather than starting over. Checkpointing is an application-dependent process, not something that can be automated on the system end; many popular software packages have checkpointing built in (e.g., ‘restart’ files). In summary, users of the preemptable QoS should implement checkpointing if at all possible to ensure they can pick up where they left off in the event their job is preempted.

Requeuing: Users running jobs that do not require requeuing if preempted should specify the `--no-requeue` flag noted above to avoid unnecessary use of compute resources.

#### Example Job Scripts

tbd

#### Other considerations

tbd
