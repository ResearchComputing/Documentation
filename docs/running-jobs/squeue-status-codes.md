# `squeue` status and reason codes

The `squeue` command details a variety of information on an active
job’s status with state and reason codes. *__Job state
codes__* describe a job’s current state in queue (e.g. pending,
completed). *__Job reason codes__* describe the reason why the job is
in its current state. 

The following tables outline a variety of job state and reason codes you
may encounter when using squeue to check on your jobs.

## Job State Codes

| Status        | Code  | Explaination                                                           |
| ------------- | :---: | ---------------------------------------------------------------------- |
| COMPLETED	| `CD`	| The job has completed successfully.                                    |
| COMPLETING	| `CG`	| The job is finishing but some processes are still active.              |
| FAILED	| `F`	| The job terminated with a non-zero exit code and failed to execute.    |
| PENDING	| `PD`	| The job is waiting for resource allocation. It will eventually run.    |
| PREEMPTED	| `PR`	| The job was terminated because of preemption by another job.           |
| RUNNING	| `R`	| The job currently is allocated to a node and is running.               |
| SUSPENDED	| `S`	| A running job has been stopped with its cores released to other jobs.  |
| STOPPED	| `ST`	| A running job has been stopped with its cores retained.                |

A full list of these Job State codes can be found in [Slurm’s
documentation.](https://slurm.schedmd.com/squeue.html#lbAG)


## Job Reason Codes

| Reason Code              | Explaination                                                                                |
| ------------------------ | ------------------------------------------------------------------------------------------- |
| `Priority`	           | One or more higher priority jobs is in queue for running. Your job will eventually run.     |
| `Dependency`	           | This job is waiting for a dependent job to complete and will run afterwards.                |
| `Resources`	           | The job is waiting for resources to become available and will eventually run.               |
| `InvalidAccount`	   | The job’s account is invalid. Cancel the job and rerun with correct account.             |
| `InvaldQoS`              | The job’s QoS is invalid. Cancel the job and rerun with correct account.                 |
| `QOSGrpCpuLimit` 	   | All CPUs assigned to your job’s specified QoS are in use; job will run eventually.          |
| `QOSGrpMaxJobsLimit`	   | Maximum number of jobs for your job’s QoS have been met; job will run eventually.           |
| `QOSGrpNodeLimit`	   | All nodes assigned to your job’s specified QoS are in use; job will run eventually.         |
| `PartitionCpuLimit`	   | All CPUs assigned to your job’s specified partition are in use; job will run eventually.    |
| `PartitionMaxJobsLimit`  | Maximum number of jobs for your job’s partition have been met; job will run eventually.     |
| `PartitionNodeLimit`	   | All nodes assigned to your job’s specified partition are in use; job will run eventually.   |
| `AssociationCpuLimit`	   | All CPUs assigned to your job’s specified association are in use; job will run eventually.  |
| `AssociationMaxJobsLimit`| Maximum number of jobs for your job’s association have been met; job will run eventually.   |
| `AssociationNodeLimit`   | All nodes assigned to your job’s specified association are in use; job will run eventually. |

A full list of these Job Reason Codes can be found [in Slurm’s
documentation.](https://slurm.schedmd.com/squeue.html#lbAF)

