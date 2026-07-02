# Running workflow managers on Persistence1

`Persistence1` is a dedicated service for running long-lived workflow managers that coordinate jobs on Alpine.

Many workflow management tools, including Nextflow, Snakemake, and KinBot, require a process that remains active for days or weeks while monitoring workflow progress and submitting jobs to the cluster. Because these applications must remain running for extended periods, they are not suitable for execution as standard Slurm jobs and should not be run on login nodes.

`Persistence1` provides a dedicated environment where users can run workflow managers and other workflow orchestration tools that require continuous execution while maintaining access to Alpine resources. 

```{important}
`Persistence1` is not intended for running computationally intensive workloads directly, interactive analysis, high-memory applications or replacing Slurm job submissions.
```


## Getting Started

Access to `persistence1` is managed through a dedicated user group and must be requested before use. 

* To request access, submit a request through the [support request form](https://colorado.service-now.com/req_portal?id=ucb_sc_rc_form).
* In the form, select "Other" as the "Nature of Request".
* Include the following information in your request:
    - your CURC username
    - a brief description of the workflow manager or application you intend to run


## Connecting to Persistence1

After access has been granted, you can connect to `persistence1` from a CURC login node:

```
[rcops@login-ci3 ~]$ ssh persistence1
```

## Working on Persistence1

`Persistence1` provides access to the same filesystems on CURC compute nodes, as well as a subset of relevant software.

Users can:

* access their `/home`, `/projects` `/scratch/alpine`, and (if available) PetaLibrary directories.
* run container-based workflow managers through Apptainer
* use the Miniforge module to create and manage conda environments that contain workflow managers
* directly load and use modules for popular workflow managers such as Nextflow

## Getting Help

If you have questions about access, software availability, or workflow configuration on `Persistence1`, submit a request through [support request form](https://colorado.service-now.com/req_portal?id=ucb_sc_rc_form).
