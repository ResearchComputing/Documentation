## CUmulus _(CURC On-Premise Cloud Service)_

CUmulus is an NSF-funded on-premise cloud system hosted by CU Research Computing. The CUmulus service includes access to a private cloud "vpc" with a small number of outside routable "floating IPs".  Within this "vpc" customers will be given an allocation of:
 - CPU cores
 - Memory
 - Storage

which can be used to host virtual machines and volumes to host workloads.

These virtual machines and volumes will be considered unmanaged meaning that customers of the CUmulus platform are fully responsible for the software contents running in the virtual machine and security within (including keeping that security up to date).

Research Computing staff will manage the security of the OpenStack platform and associated technologies and keep these up to date.

In addition, OIT Public Cloud Broker staff will provide [consultation services](https://oit.colorado.edu/services/consulting-professional-services/public-cloud-broker/consulting-services) with cloud architecture planning and optimization to assist with usage of this platform.

### Features
- Virtual machine creation
- Disk volume creation/snapshot
- Basic Infrastructure monitoring
- Assignment of routable "floating IPs"
- High availability in the event of underlying hardware failure
- Load balancing of virtual resources across multiple physical machines
- Console access to hosted VMs

> CUmulus Resources
> - 244 total CPU cores
> - 4GB RAM per CPU core
> - 101.3TB of object-oriented storage

### Eligibility

CUmulus is a free-to-use cloud system where:
- 80% of cycles: CU Boulder faculty, staff, students, and affiliates
- 20% of cycles: RMACC affiliates (CSU, Wyoming, UC system campuses, [and many more](https://rmacc.org/partners)) 

> To ensure optimal usage, unused cycles are preemptively available to the Open Science Grid ([OSG](https://opensciencegrid.org/))

### Expectations

CU Research Computing manages the resources and address systems-level issues as they arise. Users will be expected to deploy and manage their cloud instances, including selecting security policies and networking protocols, installing and maintaining software, and running computational workflows. Users are essentially “system administrators” of their cloud instance. 

> **_NOTE:_** _CU Research Computing does not support administration within CUmulus cloud instances._

RC will:
- Maintain a recent version of OpenStack with availability of both command line and web console access with Identikey
- Maintain a high availability environment within the constraints of business hours staffing (no on-call support)
- Maintain the platform according to baseline security standards (see [https://www.cu.edu/security/system-wide-baseline-security-standards](https://www.cu.edu/security/system-wide-baseline-security-standards))
- Respond within 24 hours to any support requests
- Assist with planning and architecture for usage of the platform
- Take action to address any abuse or misuse of the platform
- Provide supported base images for customers to use on the platform (these are provided without warranty, but represent known working operating systems on the CUmulus platform). Over time we may add additional features to these images to make them more usable in this environment


Customers of CUmulus will:
- Utilize the platform only for the storage/processing of Public data (see [https://www.cu.edu/security/data-classification](https://www.cu.edu/security/data-classification))
- Plan for and maintain an operating system patching process that ensures patches are installed at least quarterly
- Configure applications software with security in mind (e.g. use of least privilege when configuring security groups)
- Address any vulnerabilities identified by OIT or OIS in running operating systems or software in a timely manner
- Comply with baseline security standards (see [https://www.cu.edu/security/system-wide-baseline-security-standards](https://www.cu.edu/security/system-wide-baseline-security-standards))
- Comply with acceptable use policies [https://www.colorado.edu/policies/acceptable-use-cu-boulders-it-resources](https://www.colorado.edu/policies/acceptable-use-cu-boulders-it-resources) 

### Using CUmulus

#### Appropriate use cases:
- Workflow management software that monitors/schedules jobs on Summit, Alpine, or Blanca
- Running a research database/website application that queries data stored on CURC PetaLibrary 
- Web-based research “Hubs” (JupyterHub, Shiny Apps)

#### Inappropriate use cases: 
- Running workflows that you could run on Summit, Alpine or Blanca
- Websites that do not require connectivity to CURC resources
- Websites that do not require connectivity to CURC resources
- Serverless applications

> **_NOTE:_** _If neither CUmulus nor other CURC resources (Summit, Alpine, Blanca) are appropriate for your use case, we have a small seed grant from Amazon Web Services and may be able to provide you with AWS resources that suit your needs._
> Possible AWS Cases:
> - Workflow that cannot be run on Summit/Alpine/Blanca and resource needs are too big for CUmulus
> - Workflow that require access to very large datasets that are only hosted on AWS (e.g., some NASA satellite datasets)
