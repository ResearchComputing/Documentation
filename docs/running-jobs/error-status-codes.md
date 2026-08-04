# Job Submission and Status Error, Warning, and Reason Codes

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

## Alpine Job Submission Error Codes

| **#** | **Error Message** | **Cause / Explanation** | **Resolution / Action** |
| --- | --- | --- | --- |
| 1 | The `<partition>` partition accepts the following QoS values: `<list>` | You have provided a QoS value that is not supported by the requested partition. | Use a supported QoS from the list given in the error output. You can also find more information about Alpine QoS in our [Alpine QoS Documentation](../clusters/alpine/alpine-hardware.md#quality-of-service-qos). |
| 2 | Users must specify `--nodes` for all GPU partitions. | You have not specified a number of nodes in your job request, which is required on all GPU partitions. | Specify a number of nodes using the `--nodes=N` directive, where `N` is the number of nodes to request. Please note that currently, all GPU jobs are limited to 1 node. |
| 3 | All GPU jobs are limited to 1 node. Please reschedule your job using `--nodes=1`. | You have requested more than one node (the maximum allowed) on a GPU partition. | Reschedule your job using `--nodes=1`. |
| 4 | A list of `gres` options is currently not permitted. | You have provided a comma-separated list of `GRES` options, which is not permitted. | Specify only one `GRES` option. |
| 5 | An invalid `--gres` input was provided. | You have provided an invalid `--gres` option. | Please check the spelling of your `--gres` input and try again. You can find a list of valid Alpine `GRES` in our [Alpine GRES Documentation](../clusters/alpine/alpine-hardware.md#general-resources-gres). |
| 6 | For GPU partitions, users must use the `gres` name `gpu`. | You have specified a `gres` option other than `gpu` on a GPU partition. | Please specify `gpu` as the `gres` name. |
| 7 | An invalid `GRES` type was specified for the selected partition `<partition>` and QoS `<qos>`. Valid `GRES` types for this partition and QoS selection are: `<list>`. | You have specified a `GRES` type that is not compatible with the provided partition and QoS. | Select a valid `GRES` type from the list provided in the error message. You can also find more information about Alpine `GRES` in our [Alpine GRES Documentation](../clusters/alpine/alpine-hardware.md#general-resources-gres). |
| 8 | For the QoS `<qos>`, users can only request `<N>` GPU(s) of type `<type>` per job. | You have requested a greater number of GPUs than are allowed for this partition and QoS. | Request fewer GPUs for your job, up to the number specified in the error message. |
| 9 | Users must specify `--ntasks` or `--mem` for all GPU partitions. | You have requested resources from a GPU partition, but did not specify the `--ntasks` or `--mem` directives. | Specify values for `--ntasks` or `--mem` in your job request. |
| 10 | You are requesting `<N>` tasks, which exceeds the maximum allowed of `<N>` tasks for `<N>` GPU(s) of type `<type>`. | You have requested a greater number of tasks (`--ntasks`) than is allowed for the specified number of GPUs. | Decrease the number of tasks requested, or increase the number of GPUs requested. You can find more information about task/GPU limits in the "Max cores/GPU" column of our [Alpine GRES Documentation](../clusters/alpine/alpine-hardware.md#general-resources-gres). |
| 11 | You are requesting `<N>` CPUs, which exceeds the maximum allowed of `<N>` CPUs for `<N>` GPU(s) of type `<type>`. | You have requested a greater number of CPUs (`--ntasks` * `--cpus-per-task`) than is allowed for the specified number of GPUs. | Decrease the number of CPUs requested, or increase the number of GPUs requested. You can find more information about CPU core/GPU limits in the "Max cores/GPU" column of our [Alpine GRES Documentation](../clusters/alpine/alpine-hardware.md#general-resources-gres). |
| 12 | You are requesting `<N>` MiB of RAM, which exceeds the maximum allowed of `<N>` MiB of RAM for `<N>` GPU(s) of type `<type>`. | You have requested more than the maximum allowed amount of RAM (memory) for the number of GPUs and type of GPU provided. | Request less RAM in your job submission, no more than the amount specified in the error message, or increase the number of GPUs requested. |
| 13 | A partition has not been provided, specifying a partition is now required. | You have not specified a partition in your job submission; specifying a partition is required. | Specify a partition name in your job submission. You can find a list of valid partitions in our [Alpine Partitions Documentation](../clusters/alpine/alpine-hardware.md#partitions). |
| 14 | If a list of partitions is provided, there cannot be a mix of GPU and CPU only partitions. | Your job request contains a list of both GPU- and CPU-only partitions, which cannot be mixed. | Do not mix CPU- and GPU-only partitions in your job requests. If specifying a list of partitions, do not mix partition types in the list. |
| 15 | A Quality of Service (QoS) has not been provided. Specifying a QoS is now required. | You have not specified a QoS in your job submission; specifying a QoS is required. | Specify a QoS name in your job submission. You can find a list of valid QoS values in our [Alpine QoS Documentation](../clusters/alpine/alpine-hardware.md#quality-of-service-qos). |
| 16 | A list of QoS is currently not supported. | You have provided a comma-separated list of QoS values, which is not permitted. | Specify only one QoS value in your job submission. |
| 17 | Time has not been specified (i.e. the Slurm directive `--time`). Specifying job run time is now required. | You have not specified a value for `--time` in your job submission. | Specify a value for time using the `--time` directive. For assistance with setting run time, please submit a [Support Request Form](https://colorado.service-now.com/req_portal?id=ucb_sc_rc_form). |
| 18 | The requested runtime of the `<qos>` QoS cannot exceed `<N>` hour(s). | You have requested more than the maximum amount of time allowed for this QoS. | Reduce the time requested for the job, or switch to a different QoS that supports longer jobs. You can find a list of valid QoS values in our [Alpine QoS Documentation](../clusters/alpine/alpine-hardware.md#quality-of-service-qos). |
| 19 | The requested runtime of the `<qos>` QoS must be greater than `<N>` hour(s). | You have not requested enough time to meet the minimum required for this QoS. | Increase the time requested for the job, or switch to a different QoS that supports shorter jobs. You can find a list of valid QoS values and their associated runtime constraints in our [Alpine QoS Documentation](../clusters/alpine/alpine-hardware.md#quality-of-service-qos). |
| 20 | When requesting resources from GPU partitions, users must specify `--gres`. | You have not specified a `GRES` using the `--gres` directive, which is required on this partition. | Specify a `GRES` using the `--gres` directive. You can find a list of Alpine `GRES`, as well as examples, in our [Alpine GRES Documentation](../clusters/alpine/alpine-hardware.md#general-resources-gres). |
| 21 | If a list of GPU partitions is provided, then `GRES` must be set to `--gres=gpu:N`, where `N` is the number of GPUs. | You have provided an invalid `GRES` format while using a list of GPU partitions. | Use the `GRES` format `--gres=gpu:N`, where `N` is the number of GPUs. |

## Alpine Job Submission Warning Codes

| **#** | **Warning Message** | **Cause / Explanation** | **Resolution / Action** |
| --- | --- | --- | --- |
| 1 | Please modify your provided `GRES` so that the `GRES` type is specified. For the `<partition>` partition and `<qos>` QoS, valid `GRES` are as follows (where `N` is the number of GPUs): `<list>` | You have not specified a `GRES` type in your provided `--gres` option. | Select a valid `GRES` type from the list provided in the error message. You can also find more information about Alpine `GRES` in our [Alpine GRES Documentation](../clusters/alpine/alpine-hardware.md#general-resources-gres). |
| 2 | Since a `GRES` type was not specified, `GRES` has been set to `--gres=<gres>.` | You did not specify a `GRES` type, so the `GRES` with the lowest VRAM was automatically selected. | Please specify a `gres` type (for example, `--gres=gpu:a100-40gb`) in the future. You can find a list of valid Alpine `GRES` types in our [Alpine GRES Documentation](../clusters/alpine/alpine-hardware.md#general-resources-gres). |
