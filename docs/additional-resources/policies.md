# CURC User Policies

<br>

## Acceptable use of CURC resources

Use of CU Research Computing resources is subject to the [CU Boulder OIT Acceptable Use Policy](https://www.colorado.edu/compliance/policies/acceptable-use-cu-boulders-it-resources) and as well as the policies noted below.  CU Research Computing resources may not be used for non-research purposes or for personal financial gain and/or commercial purposes, whether for-profit or nonprofit.

For security compliance purposes, system activity on CU Boulder Research Computing resources is logged and retained for a minimum period of 90 days. Logged activity may include the following: 
* Sudo command execution (privileged access)
* Authentication events (successful and failed logins)
* User session activity
* Password changes
* Failed access attempts
* Security or privacy attribute changes
* Administrative privilege usage
* Personal Identity Verification (PIV) credential usage (where applicable)
* Data action changes
* Query parameters
* External credential usage

<br>

## Acceptable data storage and use on CURC resources

CURC systems and services (Alpine, Blanca, Open OnDemand, Petalibrary, core storage, etc.) should not be used to store any data that is US government Classified, nor any Controlled Unclassified Information including, but not limited to, data subject to the US federal Health Insurance Portability and Accountability Act (HIPAA), the US federal Family Educational Rights and Privacy Act (FERPA), or the International Traffic in Arms Regulations (ITAR).
 
For users requiring secure research computing environments to ensure compliance for sensitive data types such as those mentioned above, CURC offers secure research computing services. More information can be found on the [Secure Research Computing Resources](https://www.colorado.edu/rc/secure-research-computing-resources) webpage.

<br>

## Core storage data retention

The data retention policy for CU Research Computing “core” storage (user data in `/home` and `/projects` spaces) is a period of six years beyond the user’s last login to a CU Research Computing service. This duration is in alignment with the University’s data retention policy for research records associated with grants and contracts. The policy will be enacted via a “5 + 1” approach: after a period of five years since the user’s last login, a communication will be sent to the email address associated with the user’s account, and cc’d (as a courtesy) to persons belonging to the group associated with the user’s `/projects` space. The communication will note that data in their `/home` and `/projects` spaces will be archived after one additional month and purged after one additional year if no action is taken by the user or group members to retain the data. The user will be given the opportunity to request that the data not be deleted if still needed on CURC systems.  If no longer needed on CURC systems, the user may (if they wish to keep the data) copy the data to an alternate offsite location during the final year prior to deletion from core storage.  If the user (and only the user) does not respond within the year, the data will be deleted upon reaching year six. 

```{note}
* This policy does not apply to data stored in PetaLibrary.  Data in PetaLibrary are subject to the PetaLibrary Terms of Service. 

* This policy only applies to CU Boulder users at this time. 
```

<br>

## PetaLibrary non-payment

_Effective July 1, 2024_

In the event of non-payment, CURC will act to ensure optimal system use and storage availability. This includes restricting access and eventual data deletion. 

The timetable will be as follows: 

* After 30 days, CURC will revoke access to your data. The data will not be deleted. 
* After 90 days, data and allocation(s) are subject to deletion. 

Time is measured in full days, including weekends and holidays, starting the day after the first billing due date where the allocation owner or a representative does not make a payment. For existing allocations not up to date on payments as of the effective date of this policy, the clock will start on the effective date, July 1, 2024. 

Users may request in writing extended time to secure payment if contracting and procurement are in process but not yet complete in the stated window. The owner or a representative may make the request by submitting a [support request form](https://colorado.service-now.com/req_portal?id=ucb_sc_rc_form). Exceptions are subject to approval CURC. Users should not expect approval by CURC until confirmed in writing. 

_This policy subject to change at any time._ 

<br>

## Login nodes

The RC login nodes are lightweight virtual machines that serve as gateways to CURC computing resources, such as Blanca 
and Alpine. They are strictly intended for non-computational tasks including editing scripts, moving files, scheduling jobs to run 
on CURC computing resources, and non-intensive workflow monitoring/management tasks. They are not intended for computational tasks 
of any kind. CURC personnel regularly monitor processes on the login nodes and reserve the right to terminate processes in 
violation of this policy without notice. Repeated violations by the same user may result in a suspended account.

<br>

## Software installations

CURC will perform requested software installations for users in a globally accessible module stack provided all the following conditions are met:

* The software is needed by multiple users across more than one group or laboratory.

* The software is unavailable in the current module stack, or the user requires a different version of a software package currently in the module stack. The user provides all relevant information including release, version, installation instructions and other relevant documentation.

* The software complies with CU Boulder Office of Information Technology software and security policies

* The software complies with CURC policies, including but not limited to CURC User Policies.

* The software does not require user-specific configurations, packages, and/or other features that would make it better suited for local installation under individual user accounts.

* The user has confirmed that the software has not already been installed by a colleague in their laboratory. In this case, the colleague may request that CURC grant the user access to the software installation.

* The software is compatible with CURC’s Linux-based operating system. Furthermore, if the software is licensed for use by the user’s laboratory or department, the following requirements must be met: the user has confirmed the use of the software on CURC resources adheres to the software license agreement, as well as the licensed software requirements in the CU Boulder Office of Information Technology software policy.  

* The license is valid for cluster-wide usage; i.e., it is not restricted to a single node (aka “machine”, “computer”, or “workstation”).

* If the license is a “floating license”, the user is responsible for hosting and maintaining the license server and ensuring the server is accessible from CURC systems.

If the above requirements are not fully met, CURC will discuss alternatives with the user, such as installing the software in a location that is only accessible to the user’s group (e.g., a group-owned PetaLibrary allocation), or installing the software on a virtual machine hosted by a commercial or academic cloud provider.

Software accepted to be installed will be given an estimated installation time based on team capacity and urgency of the request. Note that this time is an estimation and not a hard-set deadline. All software installations are “Best Effort” and are not guaranteed. RC reserves the right to deny any software installation that is requested on CURC resources.

Core software such as compilers, MPIs, and relevant libraries will be updated at regular intervals. A different version of these core software packages can be requested at any point, but the installation timeframe will be subject to team capacity and build requirements.

Unused modules may be pruned after 12 months without usage. Any pruned module may be restored by user request with sufficient justification. 

CURC reserves the right to remove software that is not in compliance with CU Boulder Office of Information Technology  software or security policies.

To request a software installation, please follow the instructions provided under the FAQ How can I submit a software installation request? dropdown.

<br>

## Scratch file purge

Scratch space should be used for all compute jobs run on CURC systems. These high-performance scratch directories are not backed 
up and are not appropriate for long-term storage. Files are automatically deleted 90 days from the date they were copied to or 
created on the filesystem. However, data may be purged at shorter intervals subject to overall system needs. 

Users requiring longer-term retention of their files should perform regular backups to a remote machine or
a purchased storage, such as [PetaLibrary](../petalibrary/index.md). Inappropriate use of 
scratch storage, including attempts to circumvent the automatic file purge policy, may result in loss of access to Research 
Computing resources.

<br>

## Alpine scratch quota increases

Each user is allocated 10 TB in `/scratch/alpine`. Users requiring more than 10 TB may request a supplemental space allocation by 
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

## Compute allocations

The cumulative computing allocations of a single research group across all projects may not exceed 6 M SU/year. Project allocations submitted by members of the same research group should have distinguishable research objectives. CURC 
reserves the right to reject new project allocation requests and/or suggest amendments to existing allocations. 

<br>

## Planned Maintenance 
The first Wednesday of each month is reserved for Planned Maintenance (PM). CURC resources, including compute clusters, file systems, and servers, will be unavailable during this time. Users are encouraged to check 
[https://curc.statuspage.io/](https://curc.statuspage.io/) for updates on PMs. RC reserves the right to cancel, move, or extend 
the maintenance window as needed. 

<br>

