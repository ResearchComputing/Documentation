## CURC User Policies
<br>

### CURC Annual Survey

CURC issues an annual survey to all CURC users asking several questions about research grants, scholarly works, and student success that have been supported by CURC systems/services. These metrics are critical for fulfilling CURC's annual reporting requirements quantifying the Return on Investment of CURC resources for the University.  The survey will be open for responses for 10 weeks. To facilitate responses, this policy states that if a user does not respond to the survey by the deadline, CURC will temporarily remove their access to CURC systems until the survey is completed. CURC will not delete any data or remove any accounts. User access will be reinstated upon completion of the survey.

<br>

### Acceptable data storage and use

CURC systems and services (Alpine, Blanca, OnDemand, Petalibrary, core storage, etc.) should not be used to store any data that is US government Classified, nor any Controlled Unclassified Information including, but not limited to, data subject to the US federal Health Insurance Portability and Accountability Act (HIPAA), the US federal Family Educational Rights and Privacy Act (FERPA), or the International Traffic in Arms Regulations (ITAR).
 
For users requiring secure research computing environments to ensure compliance for sensitive data types such as those mentioned above, CURC offers secure research computing services. More information can be found at https://www.colorado.edu/rc/secure-research-computing-resources

<br>

### Login nodes

The RC login nodes are lightweight virtual machines that serve as gateways to CURC computing resources including both Blanca 
and Alpine. They are strictly intended for non-computational tasks including editing scripts, moving files, scheduling jobs to run 
on CURC computing resources, and non-intensive workflow monitoring/management tasks. They are not intended for computational tasks 
of any kind. CURC personnel regularly monitor processes on the login nodes and reserve the right to terminate processes in 
violation of this policy without notice. Repeated violations by the same user may result in a suspended account.

<br>

### Software installations

CURC will perform software installations for users of CURC resources in a globally accessible module stack provided:

- A user requires a specified software that is unavailable on the current stack.
- A user requires a different version of a currently existing software which provides additional functionality required for the 
user’s work.
- The user provides all of the relevant information including release, version, etc.
- The installation will not violate the software’s User Agreement policy.
- The installation is not better suited for a local install (i.e., Anaconda environments, Singularity containers).

Furthermore, licensed/proprietary software are subject to the following requirements:

- The user has access to a license that is valid for cluster usage.
- The license can be installed on the cluster or accessed from the cluster if it is hosted on a license server.

Software accepted to be installed will be given an estimated installation time based on team capacity and urgency of the request. 
Note that this time is an estimation and not a hard-set deadline. Installed software will be available to load with a module in 
the ‘User Software’ category in the software stack. Unused modules will be pruned after 12 months without usage. Any pruned module 
may be restored by user request.

Core software such as compilers, MPIs, and relevant libraries will be updated at regular intervals. A different version of these 
core software can be requested at any point, but installation may be performed in accordance to that timeline.

All software installations are “Best Effort” and are not guaranteed. RC reserves the right to deny any software installation that 
is requested on CURC resources.

To request a software installation please fill out the [Software Request 
Form](https://www.colorado.edu/rc/userservices/software-request).

<br>

### Scratch file purge

Scratch space should be used for all compute jobs run on CURC systems. These high-performance scratch directories are not backed 
up and are not appropriate for long-term storage. Files are automatically deleted 90 days from the date they were copied to or 
created on the filesystem. However, data may be purged at shorter intervals subject to overall system needs. 

Users requiring longer-term retention of their files should perform regular backups to their local machine if they have not 
purchased space on the [PetaLibrary](https://curc.readthedocs.io/en/latest/storage/petalibrary/index.html). Inappropriate use of 
scratch storage, including attempts to circumvent the automatic file purge policy, may result in loss of access to Research 
Computing resources.

<br>

### Alpine scratch quota increases

Each user is allocated 10 TB in `/alpine/scratch/`. Users requiring more than 10 TB may request a supplemental space allocation by 
submitting a brief (approximately one paragraph) justification. The justification should describe why a group's workflow requires 
the requested amount.

The CURC allocations committee will review the request and may ask for additional information or changes if necessary. Once 
approved, supplemental Alpine scratch allocations will be provisioned by the CURC storage team. Users should note that 
supplemental Alpine scratch allocations are subject to the 90-day purge policy.  

CURC reserves the right to actively manage the Alpine scratch filesystem in order to ensure it is performant and that all users 
have adequate space. This includes the right to:
- deallocate supplemental Alpine scratch space, and/or 
- shorten the 90-day data purge window if the need arises, and/or
- subject supplemental Alpine scratch allocations to annual renewal through the CURC allocations process

If at all possible, CURC will provide at least 1 week of notice if such measures are taken, in order to provide users the 
opportunity to copy their needed data elsewhere. 



<br>

### Compute allocations

The cumulative computing allocations of a single research group across all projects may not exceed 5 M SU/year or 2.5 M SU over 6 
months. Project allocations submitted by members of the same research group should have distinguishable research objectives. CURC 
reserves the right to reject new project allocation requests and/or suggest amendments to existing allocations. 

<br>

### Planned Maintenance 
The first Wednesday of each month is reserved for Planned Maintenance (PM). CURC resources, including compute clusters, file systems, and servers, will be unavailable during this time. Users are encouraged to check 
[https://curc.statuspage.io/](https://curc.statuspage.io/) for updates on PMs. RC reserves the right to cancel, move, or extend 
the maintenance window as needed. 

<br>

