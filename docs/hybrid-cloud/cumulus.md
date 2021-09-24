## CUmulus _(CURC On-Premise Cloud Service)_

### About CUmulus

CU Research Computing hosts an on-premise cloud service, called CUmulus, which supports cases not well suited for HPC such as webservers, databases, and long-running services. 

The CUmulus service includes access to a Virtual Private Cloud (VPC) which provides users with a logically isolated section of the cloud with a small number of outside routable floating IP addresses.  Within this VPC customers will be given an allocation of:
 - CPU cores
 - Memory
 - Storage

which can be used to host virtual machines and volumes to host workloads.

#### Features
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

#### Eligibility

CUmulus is a free-to-use cloud system where:
- 80% of cycles: CU Boulder faculty, staff, students, and affiliates
- 20% of cycles: RMACC affiliates (CSU, Wyoming, UC system campuses, [and many more](https://rmacc.org/partners)) 

> To ensure optimal usage, unused cycles are preemptively available to the Open Science Grid ([OSG](https://opensciencegrid.org/))

#### Expectations

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

#### Using CUmulus

##### Appropriate use cases:
- Workflow management software that monitors/schedules jobs on Summit, Alpine, or Blanca
- Running a research database/website application that queries data stored on CURC PetaLibrary 
- Web-based research “Hubs” (JupyterHub, Shiny Apps)

##### Inappropriate use cases: 
- Running workflows that you could run on Summit, Alpine or Blanca
- Websites that do not require connectivity to CURC resources
- Websites that do not require connectivity to CURC resources
- Serverless applications

> **_NOTE:_** _If neither CUmulus nor other CURC resources (Summit, Alpine, Blanca) are appropriate for your use case, we have a small seed grant from Amazon Web Services and may be able to provide you with AWS resources that suit your needs._
> Possible AWS Cases:
> - Workflow that cannot be run on Summit/Alpine/Blanca and resource needs are too big for CUmulus
> - Workflow that require access to very large datasets that are only hosted on AWS (e.g., some NASA satellite datasets)

###  Requesting Access to CUmulus

The application process for CUmulus requires to submit a [Google form]() to propose your use case. In this application you will:
- Describe your proposed CUmulus workflow
- Describe why this workflow is appropriate for CUmulus and cannot be accommodated by other CURC resources (Summit, Alpine or Blanca)
- Estimate the resources you require (operating system, CPU cores, disk space, memory)

Once we receive your request the allocation committee will review it. If the case is deemed appropriate by the allocations committee the following will occur.

- 30 day trial period to allow you to set up your instance and test it:

	We will review trial usage with you at 30 days. 

- Production period: 

	If trial period was successful, adjust resources based on trial period and grant 1-year allocation.  

### Project Management

Once your application has been accepted you will be notified that a project has be created and cloud access is ready. Projects are managed through CUmulus's graphical management interface: [cumulus.rc.colorado.edu/](cumulus.rc.colorado.edu/). Project owners can access the CUmulus management interface with InCommon Federation (select this option from the authentication pull-down).

![](cumulus/login.png)

The first attempt to login will fail because you have not been assigned to any groups or roles. Once you have attempted to login respond to the email that your project was set up and your username will be processed.

Once your username is processed you will be able to login, you will land on the "Overview page" which provides information about your project (computing, volume, and network usage). You can select a period of time to query usage below the main overview graphics as well as view all current vm instances.

![](cumulus/overview.png)

#### Create New Instance

![](cumulus/instances.png)

To create a new vm instance navigate to Project -> Compute -> Instances on the side-bar. On this page you will see all currently running instances(there should be no instances running your first time). Click on "Launch Instance," which will bring up the instance creation window. 

![](cumulus/instance_creation.png)

1) Details: naming and giving your instance a brief description (availability zone and count can be left as defaults).

2) Source: "Image" should be pre-selected from the "Select Boot Source" pull-down. Select your Operating System from the list of images available.

3) Flavor: Select general purpose compute flavors for research workload; the general resources needed for this instance (keep in mind OS prerequisites).

4) Networks: defaults

5) Network Ports: defaults

6) Security Groups: Select the secrity groups to launch the instance in (e.g. ssh-restricted in order to ssh into your vm, icmp to ping and troubleshoot your instance).

7) Key Pair: Create an ssh-key from your local machine ([ssh documentation](https://www.ssh.com/academy/ssh/public-key-authentication))and upload the public-key.

8) Configuration: defaults

9) Server Group: defaults

10) Scheduler Hints: defaults

11) Metadata: defaults

#### Connect Floating IP to instance

To add a publicly accessible IP to your instance, navigate to Project -> Network -> Floating IPs, which will show you a list of currently available public IP addresses. Select "Associate IP" from the list under the "Actions" column to associate with an instance. 
> _Note:_ If no floating IPs exist, email [rc-help@colorado.edu](rc-help@colorado.edu).

![](cumulus/floating_ips.png)

#### Adding Users to your Project

Project group members can be added/removed using CU Boulder's [Grouper application](https://oit.colorado.edu/tutorial/grouper-manage-members-email-enabled-groups).





