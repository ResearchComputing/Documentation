## CUmulus _(On-Premise Cloud)_

CU Research Computing hosts a free-to-use on-premise cloud service, called _CUmulus_, which supports cases not well-suited for HPC such as webservers, databases, and long-running services. 

The CUmulus service includes access to a Virtual Private Cloud (VPC) which provides users with a logically isolated section of the cloud with a small number of outside routable floating IP addresses.  Within this VPC customers will be given an allocation of:
 - CPU cores
 - Memory
 - Storage

which can be used to host virtual machines and volumes to host workloads.

#### CUmulus Quick Start

1. Request a CUmulus application by contacting the RC helpdesk at <rc-help@colorado.edu>
2. Once your application has been accepted, manage your project at the [CUmulus Web Portal](https://cumulus.rc.colorado.edu/auth/login/?next=/).
	- Documentation on [managing your CUmulus project](./project-management.html)
3. Get started with your Cloud Instances by following our documentation on:
	- [Creating a cloud instance](../tutorials/cumulus1.html)
	- [Integrating CUmulus with CURC HPC resources](../tutorials/cumulus3.html)
4. Visit all of our [CUmulus specific tutorials](../tutorials/index.html) on the Research Computing GitHub for step-by-step examples.

#### Features
- Virtual machine creation
- Storage volume creation/snapshot
- Basic Infrastructure monitoring
- Assignment of routable "floating IPs" (e.g., for web-hosting)
- High availability in the event of underlying hardware failure
- Load balancing of virtual resources across multiple physical machines
- Console access to hosted VMs

> CUmulus Resources
> - 244 total CPU cores
> - 4GB RAM per CPU core
> - 101.3TB of object-oriented storage

#### Why use CUmulus?

<iframe width="560" height="315" src="https://www.youtube.com/embed/bX1J641oqNc" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

#### Eligibility

CUmulus is a free-to-use cloud system where:
- 80% of cycles: CU Boulder faculty, staff, students, and affiliates
- 20% of cycles: RMACC affiliates (CSU, Wyoming, UC system campuses, [and many more](https://rmacc.org/partners)) 

> To ensure optimal usage, unused cycles are preemptively available to the Open Science Grid ([OSG](https://opensciencegrid.org/))

#### Expectations

CU Research Computing manages the resources and address systems-level issues as they arise. Users will be expected to deploy and manage their cloud instances, including selecting security policies and networking protocols, installing and maintaining software, and running computational workflows. Users are essentially “system administrators” of their cloud instance. 

> **_NOTE:_** _CU Research Computing does not support administration within CUmulus cloud instances._

##### Appropriate use cases:
- Workflow management software that monitors/schedules jobs on Summit, Alpine, or Blanca
- Running a research database/website application that queries data stored on CURC PetaLibrary 
- Web-based research “Hubs” (JupyterHub, Shiny Apps)

##### Inappropriate use cases: 
- Running workflows that can more efficiently be run on Summit, Alpine or Blanca
- Personal websites or websites unrelated to research
- Serverless applications

> **_NOTE:_** _If neither CUmulus nor other CURC resources (Summit, Alpine, Blanca) are appropriate for your use case, we have limited access to Amazon Web Services and may be able to provide you with AWS resources that suit your needs._ Some Possible AWS Cases are listed below:
> - Workflow that cannot be run on Summit/Alpine/Blanca and resource needs are too big for CUmulus
> - Workflow that require access to very large datasets that are only hosted on AWS (e.g., some NASA satellite datasets)

###  Requesting Access to CUmulus

The application process for CUmulus requires users to submit an proposal for your use case, which can be requested by emailing [rc-help@colorado.edu](rc-help@colorado.edu). In this proposal you will:
- Describe your CUmulus workflow
- Describe why this workflow is appropriate for CUmulus and cannot be accommodated by other CURC resources (Summit, Alpine or Blanca)
- Estimate the resources you require (operating system, CPU cores, disk space, memory)

Once we receive your request the allocation committee will review it. If the case is deemed appropriate by the allocations committee the following will occur.

- 30 day trial period to allow you to set up your instance and test it:

	We will review trial usage with you at 30 days. 

- Production period: 

	If trial period was successful, adjust resources based on trial period and grant 1-year allocation.  

<br>

The CU Research Computing group would like to acknowledge support of this project from the National Science Foundation (OAC-1925766).

Couldn't find what you need? [Provide feedback on these docs!](https://forms.gle/bSQEeFrdvyeQWPtW9)
