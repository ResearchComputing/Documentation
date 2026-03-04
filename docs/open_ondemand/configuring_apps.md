# Configuring Open OnDemand interactive applications

Within Open OnDemand, interactive applications contain different configuration options. These options vary by application and for a select number of applications one can select **"Configuration type"**. This field allows one to specify either **"Preset configuration"** or **"Custom configuration"**. The **"Preset configuration"** option provides the **"Preset configuration"** field, which provides a select number of options for resources and automatically sets important Slurm directives for you. Although **"Preset configurations"** work for most users, some users may want to have finer control of the resources they would like to run on. This can be accomplished by selecting **"Custom configuration"** in the **"Configuration type"** field. For more information on these custom configurations, consult the section [Custom configuration options](#custom-configuration-options) below. 

```{eval-rst}
.. figure:: ./OnDemand/preset_custom_configs.png
   :align: center
```

```{important}

All applications that have a **"Configuration type"** option and start a job using the **"Preset configuration"** field are automatically submitted to the `ahub` partition. This partition provides quick access to resources with limitations (see [partitions on Alpine](../clusters/alpine/alpine-hardware.md#partitions)). One major stipulation of these resources is that only **1 job** can run on `ahub` at a time. 

```

## Custom configuration options

Custom configuration options can be extremely useful, if you would like to request resources that are not available through the **"Preset configuration"** option. Using this option one can gain access to unconventional resources such as the following. 

* GPU nodes
* High-memory nodes
* A large numbers of cores
* Longer job durations

Unfortunately, specifying these options can be overwhelming! To help users make sense of these options, we have constructed the table below, which describes each field. 

| Input | Description |
| --- | ----------- |
| Cluster | The HPC cluster you would like to run on. Possible options are [Alpine](../clusters/alpine/index.md) and [Blanca](../clusters/blanca/blanca.md).  |
| Account | The account you would like to use. If you do not have a project allocation, then CU Boulder users specify `ucb-general`; CSU users specify `csu-general`; RMACC users specify `rmacc-general`; and AMC users provide `amc-general`. If you have a project allocation you can use this allocation e.g. `ucbXXX_asc1`. Blanca users should use their `blanca-<groupname>` partition name. |
| Partition | Specifies a particular node type to use. For example, you can provide `ahub` for quicker access or utilize another [partition on Alpine](../clusters/alpine/alpine-hardware.md#partitions).  Blanca users should use their `blanca-<groupname>` partition.  |
| QoS Name | Quality of Service (QoS) constrains or modifies certain job characteristics. On most Alpine partitions you can specify `normal` for jobs of up to 24 hours and `long` for jobs of up to 7 days in duration. For more information see [Alpine QoS](../clusters/alpine/alpine-hardware.md#quality-of-service-qos). Blanca users should specify their `blanca-<groupname>` partition name for QoS. |
| Time| The duration of the job, in hours. This is dependent on both the partition and the QoS on Alpine (see above).  On Blanca, users may specify jobs of up to 7 days (168 hours) in duration. |
| Number of cores | The number of physical CPU cores for the job. Interactive job applications may use up to 16 cores, if using the `ahub` partition.  All jobs are limited to a single compute node. |
| Reservation | A reservation reserves resources for jobs being executed by select users and/or accounts. Reservations are rare on our system, but can sometimes be granted for courses utilizing HPC resources or the testing of specialty hardware. | 
| gres | General resources (gres) allows for fine-grain hardware specifications. This option is often used to request GPUs. For more information on gres, see [General Resources (gres)](../clusters/alpine/alpine-hardware.md#general-resources-gres).| 
| nodelist | Allows individuals to request resources from a specific list of nodes. For example, one could provide `c3cpu-a2-u1-1` if they only wanted their job to request resources from that node. For more information on setting this field, please see [Slurm's documentation on `--nodelist`](https://slurm.schedmd.com/sbatch.html#OPT_nodelist).  | 
| constraint | Provides users with the ability to request resources that have specific features. For example, if we only wanted nodes with EPYC 9534 processors, we could provide `epyc-9534`. For more information on setting this field, please see [Slurm's documentation on `--constraint`](https://slurm.schedmd.com/sbatch.html#OPT_constraint). | 

```{warning}
Jobs scheduled on partitions other than `ahub` may take up to several hours to start depending on the hardware and duration selected.
```

