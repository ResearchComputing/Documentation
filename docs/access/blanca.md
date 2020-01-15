## Blanca

CU Research Computing operates a shared “condo” compute cluster, named Blanca, which consists of nodes owned by individual research groups or departments.  Condo partners get significantly prioritized access on nodes that they own and can run jobs on any nodes that are not currently in use by other partners.

An allocation of CPU time is not needed in order to run on Blanca.

If you would like to purchase a Blanca node, please visit the Research Computing [website](https://www.colorado.edu/rc/resources/blanca) for more details.

### Blanca Quick-Start

1. If your group is a Blanca partner, ask your PI or PoC to send an email to rc-help@colorado.edu requesting access for you to their high-priority queue.
2. From a login node, run "module load slurm/blanca" to access the Slurm job scheduler instance for Blanca.
3. Consult the Table and the Examples section below to learn how to direct your jobs to the appropriate compute nodes.
4. If needed, compile your application on the appropriate compute node type.
5. Read the rest of this page thoroughly.


### Job Scheduling

All jobs are run through a batch/queue system.  Interactive jobs on compute nodes are allowed but these must be initiated through the scheduler.  Each partner group has its own high-priority QoS (analogous to a queue) for jobs that will run on nodes that it has purchased.  High-priority jobs move to the top of the queue and are thus guaranteed to start running within a few minutes, unless other high-priority jobs are already queued or running ahead of them.  High-priority jobs can run for a maximum wall time of 7 days.  All partners also have access to a low-priority preemptable QoS that can run on any Blanca nodes that are not already in use by their owners.  Low-priority jobs have a maximum wall time of 24 hours.

Blanca uses a separate instance of the Slurm scheduling system from the other RC compute resources.  You can use Blanca’s Slurm instance by loading a special module on a login node: “module load slurm/blanca”.

More details about how to use Slurm can be found [here](../running-jobs/running-apps-with-jobs.html).

### QoS

Slurm on Blanca uses “Quality of Service”, or QoS, to classify jobs for scheduling.  A QoS in this case is analogous to a "queue" in other scheduling systems.  Each partner group has its own high-priority QoS called `blanca-<group identifier>` and can also use the condo-wide low-priority QoS, which is called `preemptable`.

If you are a new Blanca user, ask your PI or Point of Contact person to request access for you to your group’s high-priority QoS; requests should be made via email to rc-help@colorado.edu.  You are only allowed to use a high-priority QoS if you have specifically been added as a member of it, and you can only use the low-priority preemptable QoS if you are also a member of a high-priority QoS.  Your PI may also be able to point you to group-specific documentation regarding Blanca.

### Node-QoS-Features

Since not all Blanca nodes are identical, you can include node features in your job requests to help the scheduler determine which nodes are appropriate for your jobs to run on when you are using the preemptable QoS.

To determine which nodes exist on the system, type `scontrol show nodes` to get a list.

### Node Features Table

Node name     | High-priority QoS | General hardware attributes | Features
--------------|---------------|-----------------------------|---------
bnode010[1-5] | blanca-ics    | 32 cores, 2.6 GHz,<br> 256 GB RAM,<br> 1 TB local disk | sandybridge,<br> avx,<br> rhel7
bnode010[6-7] | blanca-igg | 24 cores, 2.5 GHz,<br> 128 GB RAM,<br> 1 TB local disk | haswell,<br> avx2,<br> rhel7
bnode01[08-11] | blanca-ibgc1 | 48 cores, 2.5 GHz,<br> 256 GB RAM,<br> 1 TB local disk | haswell,<br> avx2,<br> rhel7
bnode01[12-14] | blanca-mrg | 24 cores, 2.5 GHz,<br> 128 GB RAM,<br> 1 TB local disk | haswell,<br> avx2,<br> rhel7
bnode01[15-16] | blanca-el | 28 cores w/ 2x hyperthreading/core, 2.4 GHz,<br> 128 GB RAM,<br> 1 TB local disk | broadwell,<br> avx2,<br> rhel7
bnode02[01-36] | blanca-ccn | 16 cores, 3.3 GHz,<br> 64 GB RAM,<br> 1 TB local disk |ivybridge,<br> Quadro,<br> k2000,<br> avx,<br> fdr,<br> rhel7
bnode0301 | blanca-ics | 32 cores, 2.4 GHz,<br> 256 GB RAM,<br> 1 TB local disk | broadwell,<br> avx2,<br> rhel7
bnode030[2-9] | blanca-sha | 28 cores, 2.4 GHz,<br> 128 GB RAM,<br> 1 TB local disk | broadwell,<br> avx2,<br> rhel7
bnode0310 | blanca-ics | 32 cores, 2.4 GHz,<br> 256 GB RAM,<br> 1 TB local disk | broadwell,<br> avx2,<br> rhel7
bnode0311 | blanca-ceae | 28 cores, 2.4 GHz,<br> 128 GB RAM,<br> 1 TB local disk | broadwell,<br> avx2,<br> rhel7
bgpu-dhl1 | blanca-dhl | 56 cores, 2.4 GHz,<br> 128 GB RAM,<br> 1 TB local disk | broadwell,<br> avx2,<br> rhel7,<br> Tesla,<br> P100
bnode03[12-15] | blanca-pccs | 28 cores, 2.4 GHz,<br> 128 GB RAM,<br> 1 TB local disk | broadwell,<br> avx2,<br> rhel7
bnode0316,<br> bnode0401 | blanca-csdms | 28 cores w/ 2x hyperthreading/core, 2.4 GHz,<br> 128 GB RAM,<br> 1 TB local disk | broadwell,<br> avx2,<br> rhel7, <br> 2x hyperthreading/core
bnode04[02-03] | blanca-sol | 28 cores w/ 2x hyperthreading/core, 2.4 GHz,<br> 128 GB RAM,<br> 1 TB local disk | broadwell,<br> avx2,<br> rhel7, <br> 2x hyperthreading/core
bnode05[01-02] | blanca-appm | 32 cores, 2.10 GHz,<br> 191.904 GB RAM,<br> 1 TB local disk | skylake, <br> avx2,<br> rhel7,<br> 2x hyperthreading/core
himem04 | blanca-ibg | 80 cores, 2.1 GHz,<br> 1024 GB RAM,<br> 10 TB local disk | westmere-ex,<br> localraid,<br> rhel7
bnode0404 | blanca-rittger | 32 cores, 2.10 GHz,<br> 191.904 GB RAM,<br> 1 TB local disk | skylake,<br> avx2,<br> rhel7,<br> 2x hyperthreading/core
bnode04[05-08] | blanca-ics | 28 cores, 2.4 GHz,<br> 250.000 GB RAM,<br>1 TB local disk | broadwell,<br> avx2,<br> rhel7
bnode04[12-14] | blanca-ibg | 32 cores, 2.10 GHz,<br> 1000.00 GB RAM,<br> 10 TB local disk | skylake,<br> avx2,<br> rhel7,<br> 2x hyperthreading/core
bnode05[03-04] | blanca-csdms | 32 cores, 2.10 GHz,<br> 191.904 GB RAM,<br> 1 TB local disk | skylake,<br> avx2,<br> rhel7,<br> 2x hyperthreading/core
bnode05[05-06] | blanca-geol | 32 cores, 2.10 GHz,<br> 191.904 GB RAM,<br> 1 TB local disk | skylake,<br> avx2,<br> rhel7,<br> 2x hyperthreading/core
bnode05[07] | blanca-rittger | 32 cores, 2.10 GHz,<br> 191.840 GB RAM,<br> 1 TB local disk | skylake,<br> avx2,<br> rhel7,<br> 2x hyperthreading/core
bnode05[08-09] | blanca-appm | 40 cores, 2.10 Ghz,<br> 191.668 GB RAM,<br> 1 TB local disk | cascade,<br> avx2,<br> rhel7,<br> 2x hyperthreading/core
bgpu-mktg1 | blanca-mktg | 32 cores, 2.10 GHz,<br> 772.476 GB RAM,<br> 1.8 TB local disk,<br> 1 NVIDIA P100 GPU | skylake,<br> avx2,<br> rhel7,<br> Tesla,<br> P100

### Description of features

- **westmere-ex**: Intel processor generation  
- **sandybridge**: Intel processor generation  
- **ivybridge**: Intel processor generation  
- **haswell**: Intel processor generation  
- **broadwell**: Intel processor generation  
- **avx**: AVX processor instruction set  
- **avx2**: AVX2 processor instruction set  
- **fdr**: InfiniBand network generation  
- **Quadro**: NVIDIA GPU generation  
- **Tesla**: NVIDIA GPU generation  
- **k2000**: NVIDIA K2000 GPU  
- **P100**: NVIDIA P100 GPU  
- **localraid**: large, fast RAID disk storage in node  
- **rhel7**: RedHat Enterprise Linux version 7 operating system  


### Examples

Here are examples of Slurm directives that can be used in your batch scripts in order to meet certain job requirements.  Note that the "constraint" directive constrains a job to run only on nodes with the corresponding feature.

1. To run a 32-core job for 36 hours on a single blanca-ics node:
```bash
#SBATCH --qos=blanca-ics
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=32
#SBATCH --time=36:00:00
```

2. To run a 56-core job across two blanca-sha nodes for seven days:
```bash
#SBATCH --qos=blanca-sha
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=28
#SBATCH --time=7-00:00:00
#SBATCH --export=NONE
```

3. To run an 8-core job in the low-priority QoS on any node that has broadwell processors and uses the RHEL 7 operating system:
```bash
#SBATCH --qos=preemptable
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=8
#SBATCH --time=4:00:00
#SBATCH --export=NONE
#SBATCH --constraint="broadwell&rhel7"
```

4. To run an 8-core job in the low-priority QoS on any node that has either the AVX or AVX2 instruction set:
```bash
#SBATCH --qos=preemptable
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=8
#SBATCH --time=4:00:00
#SBATCH --export=NONE
#SBATCH --constraint="avx|avx2"
```

5. To start a 2-hr interactive job on one core on a blanca-ceae node, run this at the command line:
```bash
sinteractive --qos=blanca-ceae --export=NONE --time=02:00:00
```
Note that the interactive job won't start until the resources that it needs are available, so you may not get a command prompt on your assigned compute node immediately.


### Important notes

1. To see what modules are available, start an interactive job on a compute node and use `module avail` or `module spider` on it.
2. /home, /projects, and /work (PetaLibrary Active) are available on all Blanca nodes.  Scratch I/O can be written to /rc_scratch, which should offer much better performance than /projects.  All Blanca nodes also have at least 850 GB of scratch space on a local disk, /local/scratch.  For more info on the different RC storage spaces, [please see our page on storage.](https://www.colorado.edu/rc/resources/filesystemstorage)
3. There are no dedicated Blanca compile nodes.  To build software that will run on Blanca, start an interactive job on a node like the one on which you expect your jobs to run, and compile your software there.  Do not compile on the login nodes!
4. Multi-node MPI jobs that do a lot of inter-process communication do not run well on most Blanca nodes because there is no high-performance low-latency inter-node network except on blanca-ccn.

### Blanca Preemptable QOS

*(effective 2018-03-01)* Each partner group has its own high-priority QoS (“blanca-<group identifier>”) for jobs that will run on nodes that it has contributed. High-priority jobs can run for up to 7 days. All partners also have access to a low-priority QoS (“preemptable”) that can run on any Blanca nodes that are not already in use by the partners who contributed them. Low-priority jobs will have a maximum time limit of 24 hours, and can be preempted at any time by high-priority jobs that request the same compute resources being used by the low-priority job. The preemption process will terminate the low-priority job with a grace period of up to 120-seconds. Preempted low-priority jobs will then be requeued by default.  Additional details follow.

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

Submit a 6-hour preemptable python job on 32 cores without specifying a partition (job will run on any available compute partitions on Blanca, regardless of features, so long as they have at least 16 cores each).

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

Same as Example 1, but specify a specific partition (‘blanca-ccn’) (job will only run on blanca-ccn nodes)

```bash
#!/bin/bash
#SBATCH --time=06:00:00
#SBATCH --qos=preemptable
#SBATCH --partition=blanca-ccn
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

The ‘blanca’ QoS: Note that as of 1 March, 2018, the “preemptable” qos replaces the previous low-priority QoS, “blanca”, which is no longer active.
