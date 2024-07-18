# Research Computing User Guide

Documentation covering the use of Research Computing resources.

Here are some quick links to documentation to get you started.

- [Logging In](access/logging-in.md)
- [Research Computing Filesystems](compute/filesystems.md)
- [Compiling Software](compute/compiling.md)
- [Batch Jobs](running-jobs/batch-jobs.md)
- [The Module System](compute/modules.md)
- [Frequently Asked Questions (FAQ)](faq.md)

[Can't find what you need? Provide feedback on the CURC docs!](https://forms.gle/bSQEeFrdvyeQWPtW9)

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

## Acknowledging RC

Use of University of Colorado Research Computing resources, including (but not limited to) the Janus, Summit, and Alpine supercomputers, the Blanca Condo Cluster, and the PetaLibrary data storage service must be acknowledged in any and all publications.

### Acknowledging Alpine

“This work utilized the Alpine high performance computing resource at the University of Colorado Boulder. Alpine is jointly funded by the University of Colorado Boulder, the University of Colorado Anschutz, Colorado State University, and the National Science Foundation (award 2201538).”

- DOI: https://doi.org/10.25811/k3w6-pk81 
- Citation: University of Colorado Boulder Research Computing. (2023). Alpine. University of Colorado Boulder. https://doi.org/10.25811/k3w6-pk81

### Acknowledging Cumulus 

"This work utilized the CUmulus on-premise cloud service at the University of Colorado Boulder. CUmulus is jointly funded by the National Science Foundation (award OAC-1925766) and the University of Colorado Boulder."

### Acknowledging Summit 

"This work utilized the Summit supercomputer, which is supported by the National Science Foundation (awards ACI-1532235 and ACI-1532236), the University of Colorado Boulder, and Colorado State University. The Summit supercomputer is a joint effort of the University of Colorado Boulder and Colorado State University."

- DOI: https://doi.org/10.25811/8np0-je59
- Citation: University of Colorado Boulder Research Computing. (2021). RMACC Summit Supercomputer. University of Colorado Boulder. https://doi.org/10.25811/8np0-je59

### Acknowledging Blanca

"This work utilized the Blanca condo computing resource at the University of Colorado Boulder. Blanca is jointly funded by computing users and the University of Colorado Boulder."

- DOI: https://doi.org/10.25811/v32c-gy42
- Citation: University of Colorado Boulder Research Computing. (2021). Blanca Condo Cluster. University of Colorado Boulder. https://doi.org/10.25811/v32c-gy42

### Acknowledging PetaLibrary 

"Data storage supported by the University of Colorado Boulder 'PetaLibrary'"

- DOI: https://doi.org/10.25811/81nc-wv41
- Citation: University of Colorado Boulder Research Computing. (2021). PetaLibrary. University of Colorado Boulder. https://doi.org/10.25811/81nc-wv41

----

```{toctree}
:maxdepth: 1

faq

```

```{toctree}
:maxdepth: 1
:caption: Accessing RC Resources

access/logging-in
access/duo-2-factor-authentication
access/rmacc
access/amc-access

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
:caption: Gateways & Portals

gateways/OnDemand
gateways/jupyterhub

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
software/Containerizationon
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
:caption: Tutorials
   
tutorials/index

```
   
```{toctree}
:maxdepth: 1
:caption: Additional resources

additional-resources/policies
additional-resources/CURC-cheatsheet
additional-resources/registrycilogon-instructions
additional-resources/utah-videos
additional-resources/blanca-MOU
additional-resources/other
additional-resources/biokem-facility
additional-resources/csu-xsede-usernames

```