## Alpine

tbd

### Alpine Quick-Start

tbd

1. 
2. 
3. 
4. 

### Job Scheduling

All jobs are run through a batch/queue system.  Interactive jobs on compute nodes are allowed but these must be initiated through the scheduler.  Each partner group has its own high-priority QoS (analogous to a queue) for jobs that will run on nodes that it has purchased.  High-priority jobs move to the top of the queue and are thus guaranteed to start running within a few minutes, unless other high-priority jobs are already queued or running ahead of them.  High-priority jobs can run for a maximum wall time of 7 days.  All partners also have access to a low-priority preemptable QoS that can run on any Alpine nodes that are not already in use by their owners.  Low-priority jobs have a maximum wall time of 24 hours.

### QoS

Slurm on Alpine uses “Quality of Service”, or QoS, to classify jobs for scheduling.  A QoS in this case is analogous to a "queue" in other scheduling systems.  Each partner group has its own high-priority QoS called `alpine-<group identifier>` and can also use the condo-wide low-priority QoS, which is called `preemptable`.

If you are a new Alpine user, ask your PI or Point of Contact person to request access for you to your group’s high-priority QoS; requests should be made via email to <rc-help@colorado.edu>.  You are only allowed to use a high-priority QoS if you have been added as a member of it, and you can only use the low-priority preemptable QoS if you are also a member of a high-priority QoS.  Your PI may also be able to point you to group-specific documentation regarding Alpine.

### Node-QoS-Features

Since not all Alpine nodes are identical, you can include node features in your job requests to help the scheduler determine which nodes are appropriate for your jobs to run on when you are using the preemptable QoS.

To determine which nodes exist on the system, type `scontrol show nodes` to get a list.

### Node Features

Use the `sinfo` command to determine the features that are available on any node in the cluster.

```bash
sinfo --format="%N | %f"
```

The `sinfo` query may be further specified to look at the features available within a specific partition.

#### Description of features

tbd

- **example**: Example (network, CPU, GPU, RAID, mem, OS, etc.)

#### Requesting GPUs in jobs

### Examples

Here are examples of Slurm directives that can be used in your batch scripts in order to meet certain job requirements.  Note that the "constraint" directive constrains a job to run only on nodes with the corresponding feature.

1. To run a 32-core job for 36 hours on a single alpine-ics node:
```bash
#SBATCH --qos=alpine-ics
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=32
#SBATCH --time=36:00:00
```

2. To run a 56-core job across two alpine-sha nodes for seven days:
```bash
#SBATCH --qos=alpine-sha
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=28
#SBATCH --time=7-00:00:00
#SBATCH --export=NONE
```

3. To run a 16-core job for 36 hours on a single alpine-curc-gpu node, using all three gpus:
```bash
#SBATCH --qos=alpine-curc-gpu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --time=36:00:00
#SBATCH --gres=gpu:3
```

4. To run an 8-core job in the low-priority QoS on any node that has broadwell processors and uses the RHEL 7 operating system:
```bash
#SBATCH --qos=preemptable
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=8
#SBATCH --time=4:00:00
#SBATCH --export=NONE
#SBATCH --constraint="broadwell&rhel7"
```

5. To run an 8-core job in the low-priority QoS on any node that has either the AVX or AVX2 instruction set:
```bash
#SBATCH --qos=preemptable
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=8
#SBATCH --time=4:00:00
#SBATCH --export=NONE
#SBATCH --constraint="avx|avx2"
```

6. To run an 8-core job in the low-priority QoS on any node that has at least 1 GPU:
```bash
#SBATCH --qos=preemptable
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=8
#SBATCH --time=4:00:00
#SBATCH --export=NONE
#SBATCH --gres=gpu
```

7. To start a 2-hr interactive job on one core on a alpine-ceae node, run this at the command line:
```bash
sinteractive --qos=alpine-ceae --export=NONE --time=02:00:00
```
Note that the interactive job won't start until the resources that it needs are available, so you may not get a command prompt on your assigned compute node immediately.


### Important notes

1. To see what modules are available, start an interactive job on a compute node and use `module avail` or `module spider` on it.
2. /home, /projects, and /pl/active (PetaLibrary Active) are available on all Alpine nodes.  Scratch I/O can be written to /rc_scratch, which should offer much better performance than /projects.  Most Alpine nodes also have at least 400 GB of scratch space on a local disk, available to jobs as $SLURM_SCRATCH.  For more info on the different RC storage spaces, [please see our page on storage.](https://www.colorado.edu/rc/resources/filesystemstorage)
3. There are no dedicated Alpine compile nodes.  To build software that will run on Alpine, start an interactive job on a node like the one on which you expect your jobs to run, and compile your software there.  Do not compile on the login nodes!
4. Multi-node MPI jobs that do a lot of inter-process communication do not run well on most standard Alpine nodes. Nodes equipped with specialty fabrics like Alpine CCN or any node on Alpine HPC can run MPI application much more efficiently.

### Alpine Preemptable QOS

*(effective 2018-03-01)* Each partner group has its own high-priority QoS (“alpine-<group identifier>”) for jobs that will run on nodes that it has contributed. High-priority jobs can run for up to 7 days. All partners also have access to a low-priority QoS (“preemptable”) that can run on any Alpine nodes that are not already in use by the partners who contributed them. Low-priority jobs will have a maximum time limit of 24 hours, and can be preempted at any time by high-priority jobs that request the same compute resources being used by the low-priority job. The preemption process will terminate the low-priority job with a grace period of up to 120-seconds. Preempted low-priority jobs will then be requeued by default.  Additional details follow.

#### Usage
To specify the preemptable QoS in a job script:

```bash
#SBATCH --QoS=preemptable
```

To specify the preemptable QoS for an interactive job:

```bash
$ sinteractive --qos=preemptable <other_arguments>
```

Batch jobs that are preempted will automatically requeue if the exit code is non-zero. (It will be non-zero in most cases.) If you would prefer that jobs not requeue, specify:

```bash
#SBATCH --no-requeue
```

Interactive jobs will not requeue if preempted.

#### Best practices

Checkpointing: Given that preemptable jobs can request wall times up to 24 hours in duration, there is the possibility that users may lose results if they do not checkpoint. Checkpointing is the practice of incrementally saving computed results such that -- if a job is preempted, killed, canceled or crashes -- a given software package or model can continue from the most recent checkpoint in a subsequent job, rather than starting over from the beginning. For example, if a user implements hourly checkpointing and their 24 hour simulation job is preempted after 22.5 hours, they will be able to continue their simulation from the most recent checkpoint data that was written out at 22 hours, rather than starting over. Checkpointing is an application-dependent process, not something that can be automated on the system end; many popular software packages have checkpointing built in (e.g., ‘restart’ files). In summary, users of the preemptable QoS should implement checkpointing if at all possible to ensure they can pick up where they left off in the event their job is preempted.

Requeuing: Users running jobs that do not require requeuing if preempted should specify the `--no-requeue` flag noted above to avoid unnecessary use of compute resources.

#### Example Job Scripts

Run a 6-hour preemptable python job on 32 cores without specifying a partition (job will run on any available compute partitions on Alpine, regardless of features, so long as they have at least 16 cores each).

```bash
#!/bin/bash
#SBATCH --time=06:00:00
#SBATCH --qos=preemptable
#SBATCH --job-name=test
#SBATCH --nodes=2
#SBATCH --ntasks=32
#SBATCH --output=test.%j.out

module purge
module load python

python myscript.py
```

Same as Example 1, but specify a specific partition (‘alpine-ccn’) (job will only run on alpine-ccn nodes)

```bash
#!/bin/bash
#SBATCH --time=06:00:00
#SBATCH --qos=preemptable
#SBATCH --partition=alpine-ccn
#SBATCH --job-name=test
#SBATCH --nodes=2
#SBATCH --ntasks=32
#SBATCH --output=test.%j.out

module purge
module load python

python myscript.py
```

Same as Example 1, but specify desired node features, in this case the avx2 instruction set and Redhat V7 OS (job will run on any node meeting these feature requirements, and which has at least 16 cores per node).

```bash
#!/bin/bash
#SBATCH --time=06:00:00
#SBATCH --qos=preemptable
#SBATCH --constraint="avx2&rhel7"
#SBATCH --job-name=test
#SBATCH --nodes=2
#SBATCH --ntasks=32
#SBATCH --output=test.%j.out

module purge
module load python

python myscript.py
```

#### Other considerations

Grace period upon preemption: When jobs are preempted, a 120 second grace period is available to enable users to save and exit their jobs should they have the ability to do so. The preempted job is immediately sent SIGCONT and SIGTERM signals by Slurm in order to provide notification of its imminent termination. This is followed by the SIGCONT, SIGTERM and SIGKILL signal sequence upon reaching the end of the 120 second grace period. Users wishing to do so can monitor the job for the SIGTERM signal and, when detected, take advantage of this 120 second grace period to save and exit their jobs.

The ‘alpine’ QoS: Note that as of 1 March, 2018, the “preemptable” qos replaces the previous low-priority QoS, “alpine”, which is no longer active.
