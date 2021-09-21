## CUmulus _(CURC On-Premise Cloud Service)_
CUmulus is an NSF-funded on-premise cloud system hosted and operated by CU Research Computing.

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


