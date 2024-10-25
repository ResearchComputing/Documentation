# Research Computing User Guide

Documentation covering the use of Research Computing resources.

Here are some quick links to documentation to get you started.

- [Logging In](access/logging-in.md)
- [Research Computing Filesystems](compute/filesystems.md)
- [Compiling Software](compute/compiling.md)
- [Batch Jobs](running-jobs/batch-jobs.md)
- [The Module System](compute/modules.md)
- [Frequently Asked Questions (FAQ)](access/faq.md)

Can't find what you need? We appreciate feedback on our documentation via Issues on our [GitHub page](https://github.com/ResearchComputing/Documentation/issues). If you would like to provide feedback on CURC services, please see our [We want to hear from you!](./additional-resources/feedback) page.

More information is available at https://www.colorado.edu/rc.

If you have any questions, please contact <rc-help@colorado.edu>.

## Courses using RC Resources

Instructors who wish to lead a class using CURC resources must complete the [course intake form](https://forms.office.com/r/3Bx0Dp0635) at least 3 weeks prior to the beginning of the semester in which the course will be taught. Completing the intake form will ensure that CU Research Computing can determine whether adequate resources and support are available to meet your needs, and that resources are allocated appropriately.  Upon completion, a case will be automatically generated in CURC's case management system. A CURC team member will subsequently follow up with you in the case via email, to discuss details and begin provisioning resources as needed. 

Note that CU Research Computing conducts planned maintenance the first Wednesday of each month, which may impact resource availability between 7a-5p. Instructors should expect that resources will not be available during the first Wednesday of each month. The CU Research Computing help desk is staffed from 8:00a-5:00p M-F; support outside of these times should not be expected. 

The following resources are available for course support:

* Alpine
   * Batch or Interactive Compute on Alpine
   * JupterHub in Open OnDemand (Alpine)
   * RStudio in Open OnDemand (Alpine)
   * MatLab in Open OnDemand (Alpine)
   * Remote Desktop in Open OnDemand
   * Shared storage space for students (up to 1 TB)
   * Standing reservation for Alpine resources during class meeting times
   * Compute allocations if student needs exceed their `ucb-general` account
   * Assistance building software or conda environments to support the course

* Cloud
   * Custom JupyterHub hosted in the cloud (costs may be incurred)
   * Custom RStudio hosted in the cloud (costs may be incurred)

* Lectures/training
  * CURC staff can lecture on specified topics during the class meeting time (once per course per semester). 

Students are welcome to use RC resources on their own for class projects and can request access as a regular UCB affiliate via the link off the RC homepage at: https://www.colorado.edu/rc. Students are not required to complete the course intake form noted above. To request help, contact rc-help@colorado.edu and please indicate that the work is for a class project and any deadlines.  

## Meet the RC User Support Team!

![The RC User Support team](./landing_page_images/MeetTheUserSupportTeam.png)

----

```{toctree}
:maxdepth: 1
:caption: Getting Started

access/navigating_docs
access/logging-in
access/faq
access/current-sem-trainings
access/acknowledge_curc_resources
access/duo-2-factor-authentication
```

```{toctree}
:maxdepth: 1
:caption: The Compute Environment

compute/node-types
compute/filesystems
compute/modules
compute/data-transfer
compute/compiling
compute/monitoring-resources

```

```{toctree}
:maxdepth: 1
:caption: Clusters

clusters/alpine/index
clusters/blanca/blanca
clusters/summit/summit

```

```{toctree}
:maxdepth: 2
:caption: Portals & Gateways

open_ondemand/index

```

```{toctree}
:maxdepth: 1
:caption: Running Jobs

running-jobs/running-apps-with-jobs
running-jobs/batch-jobs
running-jobs/interactive-jobs
running-jobs/slurm-commands
running-jobs/job-resources
running-jobs/squeue-status-codes
running-jobs/roce-enabled

```

```{toctree}
:maxdepth: 1
:caption: Storage

storage/petalibrary/index

```
   
```{toctree}
:maxdepth: 2
:caption: Cloud

cloud/aws/index
cloud/azure/index
cloud/gcp/index
cloud/cumulus/index

```

```{toctree}
:maxdepth: 2
:caption: Software

software/loadbalancer
software/gaussian
software/matlab
software/python
software/GNUParallel
software/vasp
software/Containerization
software/alphafold
software/spack
software/sratoolkit

```

```{toctree}
:maxdepth: 2
:caption: Programming and Parallelization
   
programming/coding-best-practices
programming/parallel-programming-fundamentals
programming/MPIBestpractices
programming/MPI-C
programming/MPI-Fortran
programming/OpenMP-C
programming/OpenMP-Fortran

```
   
```{toctree}
:maxdepth: 1
:caption: Additional resources

additional-resources/policies
additional-resources/feedback
additional-resources/CURC-cheatsheet
additional-resources/amc_ssh_auth
additional-resources/registrycilogon-instructions
additional-resources/utah-videos
additional-resources/blanca-MOU
additional-resources/facilities_equip_other
additional-resources/biokem-facility
additional-resources/csu-xsede-usernames

```