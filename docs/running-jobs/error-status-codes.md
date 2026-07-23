# Job Submission and Status Error and Reason Codes

## Alpine Job Submission Error Codes

| **#** | **Error Message** | **Cause / Explanation** | **Resolution / Action** |
| --- | --- | --- | --- |
| 1 | The `<partition>` partition accepts the following QoS values: `<list>` | You have provided a QoS value that is not supported by the requested partition. | Use a supported QoS from the list given in the error output. |
| 2 | Please modify your provided `GRES` so that the `GRES` type is specified. For the `<partition>` partition and `<qos>` QoS, valid GRES are as follows (where `N` is the number of GPUs): `<list>` | You have not specified a `GRES` type in your provided `--gres` option. | Select a valid `GRES` type from the list provided in the error message. |
| 3 | Users must specify `--nodes` for all GPU partitions. | You have not specified a number of nodes in your job request, which is required on all GPU partitions. | Specify a number of nodes using the `--nodes=N` directive, where N is the number of nodes to request. |
| 4 | All GPU jobs are limited to 1 node. Please reschedule your job using `--nodes=1`. | You have requested more than one node (the maximum allowed) on a GPU partition. | Reschedule your job using `--nodes=1`. |
| 5 | When requesting resources on the `<partition>` partition, users must specify `--gres`. | You have not specified a `GRES` using the `--gres` directive, which is required on this partition. | Specify a `GRES` using the `--gres` directive. |
| 6 | A list of `gres` options is currently not permitted. | You have provided a comma-separated list of `GRES` options, which is not permitted. | Specify only one `GRES` option. |
| 7 | An invalid `--gres` input was provided. | You have provided an invalid `--gres` option. | Please check the spelling of your `--gres` input and try again. |
| 8 | For GPU partitions, users must use the `gres` name `gpu`. | You have specified a `gres` option other than `gpu` on a GPU partition. | Please specify `gpu` as the `gres` name. |
| 9 | Since a `GRES` type was not specified, `GRES` has been set to `--gres=<gres>`. | You did not specify a `GRES` type, so one was automatically selected. | Please specify a `gres` type (for example, `--gres=gpu:a100-40gb`) in the future. |
| 10 | An invalid `GRES` type was specified for the selected partition `<partition>` and QoS `<qos>`. Valid `GRES` types for this partition and QoS selection are: `<list>`. | You have specified `GRES` type that is not compatible with this partition. | Select a valid `GRES` type from the list provided in the error message. |
| 11 | For the partition `<partition>` and QoS `<qos>`, users can only request `<N>` GPU(s) per job. | You have requested a greater number of GPUs than are allowed for this partition and QoS. | Request fewer GPUs for your job, up to the number specified in the error message. |
| 12 | Users must specify `--ntasks` or `--mem` for all GPU partitions. | You have requested resources from a GPU partition, but did not specify the `--ntasks` or `--mem` directives. | Specify values for `--ntasks` or `--mem` in your job request. |
| 13 | You are requesting <N> tasks/CPUs, which exceeds the maximum allowed of <N> tasks/CPUs for <N> GPU(s). | You have requested a greater number of CPU cores (`--ntasks` or `--ntasks` * `--cpus-per-task`) than is allowed for the specified number of GPUs. | Decrease the number of tasks/CPUs requested, or increase the number of GPUs reqeusted. |
| 14 | You are requesting `<N>` MiB of RAM, which exceeds the maximum allowed of `<N>` MiB of RAM for `<N>` GPU(s). | You have requested more than the maximum allowed amount of RAM (memory) for this partition. | Request less RAM in your job submission, no more than the amount specified in the error message. |
| 15 | A partition has not been provided; specifying a partition is now required. For more information on valid partition values, please see https://curc.readthedocs.io/en/latest/clusters/alpine/alpine-hardware.html#partitions. | You have not specified a partition in your job submission; specifying a partition is required. | Specify a partition name in your job submission. Please see the following page for a list of valid partitions: https://curc.readthedocs.io/en/latest/clusters/alpine/alpine-hardware.html#partitions |
| 16 | If a list of partitions is provided, there cannot be a mix of GPU and CPU only partitions. | Your job request contains a list of both GPU- and CPU-only partitions, which cannot be mixed. | Do not mix CPU- and GPU-only partitions in your job requests. If specifying a list of partitions, do not mix partition types in the list. |
| 17 | A Quality of Service (QoS) has not been provided. Specifying a QoS is now required. For more information on valid QoS values, please see https://curc.readthedocs.io/en/latest/clusters/alpine/alpine-hardware.html#quality-of-service-qos. | You have not specified a QoS in your job submission; specifying a QoS is required. | Specify a QoS name in your job submission. Please see the following page for a list of valid QoS values: https://curc.readthedocs.io/en/latest/clusters/alpine/alpine-hardware.html#quality-of-service-qos |
| 18 | A list of QoS is currently not supported. | You have provided a comma-separated list of QoS values, which is not permitted. | Specify only one QoS value in your job submission. |
| 19 | Time has not been specified (i.e. the Slurm directive `--time`). Specifying job run time is now required. For assistance with setting run time, please email rc-help@colorado.edu. | Your have not specified a value for `--time` in your job submission. | Specify a value for time using the `--time` directive. |
| 20 | The requested runtime of the `<qos>` QoS cannot exceed `<N>` hour(s). | You have requested more than the maximum amount of time allowed for this QoS. | Reduce the time requested for the job, or switch to a different QoS that supports longer jobs. |
| 21 | The requested runtime of the `<qos>` QoS must be greater than `<N>` hour(s). | You have not requested enough time to meet the minimum required for this QoS. | Increase the time requested for the job, or switch to a different QoS that supports shorter jobs. |
| 22 | When requesting resources from GPU partitions, users must specify `--gres`. | You have not specified a `GRES` using the `--gres` directive, which is required on this partition. | Specify a `GRES` using the `--gres` directive. |
| 23 | If a list of GPU partitions is provided, then `GRES` must be set to `--gres=gpu:N`, where `N` is the number of GPUs. | You have provided an invalid `GRES` format while using a list of GPU partitions. | Use the `GRES` format `--gres=gpu:N`, where `N` is the number of GPUs. |


## Alpine and Blanca `squeue` Status and Reason Codes

The `squeue` command details a variety of information on an active
job’s status with state and reason codes. *__Job state
codes__* describe a job’s current state in queue (e.g. pending,
completed). *__Job reason codes__* describe the reason why the job is
in its current state. 

The following tables outline a variety of job state and reason codes you
may encounter when using squeue to check on your jobs.

### Job State Codes

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

```{seealso}
A full list of these Job State codes can be found in [Slurm’s
documentation.](https://slurm.schedmd.com/squeue.html#lbAG)
```

### Job Reason Codes

| Reason Code              | Explanation                                                                                |
| ------------------------ | ------------------------------------------------------------------------------------------- |
| `Priority`	           | One or more higher priority jobs is in queue for running. Your job will eventually run.     |
| `Dependency`	           | This job is waiting for a dependent job to complete and will run afterward.                |
| `Resources`	           | The job is waiting for resources to become available and will eventually run.               |
| `InvalidAccount`	   | The job’s account is invalid. Cancel the job and rerun with the correct account.             |
| `InvaldQoS`              | The job’s QoS is invalid. Cancel the job and rerun with the correct account.                 |
| `QOSGrpCpuLimit` 	   | All CPUs assigned to your job’s specified QoS are in use; the job will run eventually.          |
| `QOSGrpMaxJobsLimit`	   | Maximum number of jobs for your job’s QoS have been met; the job will run eventually.           |
| `QOSGrpNodeLimit`	   | All nodes assigned to your job’s specified QoS are in use; the job will run eventually.         |
| `PartitionCpuLimit`	   | All CPUs assigned to your job’s specified partition are in use; the job will run eventually.    |
| `PartitionMaxJobsLimit`  | Maximum number of jobs for your job’s partition have been met; the job will run eventually.     |
| `PartitionNodeLimit`	   | All nodes assigned to your job’s specified partition are in use; the job will run eventually.   |
| `AssociationCpuLimit`	   | All CPUs assigned to your job’s specified association are in use; the job will run eventually.  |
| `AssociationMaxJobsLimit`| Maximum number of jobs for your job’s association have been met; the job will run eventually.   |
| `AssociationNodeLimit`   | All nodes assigned to your job’s specified association are in use; the job will run eventually. |

```{seealso}
A full list of these Job Reason Codes can be found [in Slurm’s
documentation.](https://slurm.schedmd.com/squeue.html#lbAF)
```
