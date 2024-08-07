# Jobs application

The **Jobs** application within Open OnDemand is the perfect tool for individuals who would prefer to use a graphical user interface (GUI) to submit and monitor jobs. Users have the ability to interact with both the [Alpine](../clusters/alpine/index.md) and [Blanca](../clusters/blanca/blanca.md) clusters with a few simple clicks. To access either of these tools, select the **Jobs** tab (pictured below). This provides the user with two options **Active Jobs** and **Job Composer**. Details for both of these options are provided in the subsections that follow. 
```{eval-rst}
.. figure:: ./OnDemand/jobs_tab.png
   :align: center
```

## Active Jobs

The **Active Jobs** tool allows users to view any of their active jobs (or all jobs) for a specific cluster (or all clusters). A user can view jobs running on [Alpine](../clusters/alpine/index.md), [Blanca](../clusters/blanca/blanca.md), or Core (the cluster that [Core Desktop](./core_desktop.md) and the [MATLAB GUI](./matlab.md) run on) clusters. Additionally, users can cancel their jobs using this tool. To view currently running jobs, first select the **Active Jobs** tool, this will bring you to the interface pictured below. On the right-hand side, you will see a drop-down button that allows you to view all jobs on the specified cluster (determined by the furthest right button) or only your jobs. To cancel a running job, navigate to the job you would like to cancel and select the red delete button. 
```{eval-rst}
.. figure:: ./OnDemand/active_jobs_interface.png
   :align: center
```

## Job Composer 

Although interactive jobs can be extremely helpful, it is often the case that a user would rather submit their job to a cluster where it can run whenever the resources are available. This is accomplished through [Batch Jobs and Job Scripting](../running-jobs/batch-jobs.md). To provide a simple interface for creating batch jobs and jobs scripting, we include the **Job Composer** tool. This tool allows users to modify and create job scripts, schedule jobs, and manage these jobs all in one central location. To create a job, navigate to the **Job Composer** tool and select **New Job**. When first getting started, it is easiest to select **From Default Template**, which will construct a template job with a default name and submit script (job script). Once a new job has been selected, a user can modify the job to their liking by navigating the provided interface. Below we provide a graphic that highlights some of the key features users may be interested in. 
```{eval-rst}
.. figure:: ./OnDemand/job_composer_nav.png
   :align: center
```

```{important}
Be sure to select the appropriate cluster when creating a job. Additionally, caution should be taken when selecting the delete button. The delete button will remove the entire directory created for the job. In the example provided above, this means that `/projects/breyes@xsede.org/ondemand/projects/default/1` would be completely deleted. 
```

```{note}
For more resources on utilizing the provided tool, see [OSC's Job Management help page](https://www.osc.edu/resources/online_portals/ondemand/job_management). 
```