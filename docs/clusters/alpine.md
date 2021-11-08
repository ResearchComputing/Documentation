## Alpine

Alpine is the third-generation HPC cluster at CURC, following Janus and RMACC Summit.

> _**Note:**_ The Alpine cluster is in early/beta release and being actively developed. If you see any errors, please report them to [rc-help@colorado.edu](rc-help@colorado.edu).

### Alpine Quick-Start

1. From a login node, run "module load slurm/alpine" to access the Slurm job scheduler instance for Alpine.
2. Consult the Table and the Examples section below to learn how to direct your jobs to the appropriate compute nodes.
3. If needed, compile your application on a compile node.

### Job Scheduling

All jobs are run through a batch/queue system. Interactive jobs on compute nodes are allowed but these must be initiated through the scheduler. High-priority jobs move to the top of the queue and are thus guaranteed to start running within a few minutes, unless other high-priority jobs are already queued or running ahead of them. High-priority jobs can run for a maximum wall time of 24 hours. Low-priority jobs have a maximum wall time of 7 days.

More details about how to use Slurm can be found [here](../running-jobs/running-apps-with-jobs.html).

### Nodes

To determine which nodes exist on the Alpine system, type `scontrol show nodes` to get a full list.

### Node Features

The Alpine cluster features some heterogeneity. A variety of feature tags are applied to nodes deployed in Alpine to allow jobs to target specific CPU, GPU, network, and storage requirements.

Use the `sinfo` command to determine the features that are available on any node in the cluster.

> Note: Alpine is currently in a beta release, not all feature descriptions have been added to nodes.

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

#### Requesting GPUs in jobs

Using GPUs in jobs requires one to use the General Resource ("Gres") functionality of Slurm to request the gpu(s).  At a minimum, one would specify `#SBATCH --gres=gpu` in their job script to specify that they would like to use a single gpu of any type.  One can also request multiple GPUs on nodes that have more than one, and a specific type of GPU (e.g. A100, MI100) if desired.  The available Alpine GPU resources and configurations can be viewed as follows on a login node with the `slurm/alpine` module loaded:

```bash
$ sinfo --Format NodeList:30,Partition,Gres |grep gpu |grep -v "mi100\|a100"
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
2. /home, /projects, and /pl/active (PetaLibrary Active) are available on all Alpine nodes.  I/O can be written to /rc_scratch, which should offer much better performance than /projects.  Most Alpine nodes also have at least 400 GB of scratch space on a local disk, available to jobs as $SLURM_SCRATCH.  For more info on the different RC storage spaces, [please see our page on storage.](https://www.colorado.edu/rc/resources/filesystemstorage)
3. There are no dedicated Alpine compile nodes.  To build software that will run on Alpine, start an interactive job on a node like the one on which you expect your jobs to run, and compile your software there.  Do not compile on the login nodes!


#### Best practices

**Checkpointing**: Given that preemptable jobs can request wall times up to 24 hours in duration, there is the possibility that users may lose results if they do not checkpoint. Checkpointing is the practice of incrementally saving computed results such that -- if a job is preempted, killed, canceled or crashes -- a given software package or model can continue from the most recent checkpoint in a subsequent job, rather than starting over from the beginning. For example, if a user implements hourly checkpointing and their 24 hour simulation job is preempted after 22.5 hours, they will be able to continue their simulation from the most recent checkpoint data that was written out at 22 hours, rather than starting over. Checkpointing is an application-dependent process, not something that can be automated on the system end; many popular software packages have checkpointing built in (e.g., ‘restart’ files). In summary, users of the preemptable QoS should implement checkpointing if at all possible to ensure they can pick up where they left off in the event their job is preempted.

**Requeuing**: Users running jobs that do not require requeuing if preempted should specify the `--no-requeue` flag noted above to avoid unnecessary use of compute resources.

#### Example Job Scripts

Run a 1-hour job on 4 cores on the alpine-cpu-a2 compute nodes

```
#!/bin/bash
#SBATCH --job-name=example-job
#SBATCH --output=example-job.%j.out
#SBATCH --time=01:00:00
#SBATCH --partition=alpine-cpu-a2
#SBATCH --nodes=1
#SBATCH --ntasks=4

module purge
module load python

python myscript.py
```
