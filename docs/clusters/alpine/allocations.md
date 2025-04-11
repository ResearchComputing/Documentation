# Alpine Allocations

## What are allocations and why do I need one?

In the simplest terms, an allocation is a way for us to specify your cut 
of Alpine's computational resources. Allocations are referred to as 
accounts in Slurm's documentation and are indicated by the `--account` 
directive:

```
#SBATCH --account=______
```

Allocations are required to run on CURC clusters. They help us keep track 
of system usage for reporting purposes and to ensure we have enough 
resources to accommodate all of our users.  

## FairShare, Priority, and Allocations

### Fairshare Scheduling
The idea behind fairshare scheduling is simple, even though its
implementation is complex: jobs submitted by people who have underutilized
their allocated resources get higher priority, while jobs submitted by
people who have overutilized their allocated resources get lower priority.

### Level Fairshare
A Level Fairshare (`LevelFS`) is a value calculated by [Slurm's Fairshare 
Algorithm](https://slurm.schedmd.com/fair_tree.html). A user's 
assigned shares (determined by their allocation) and usage (based on their 
job history) contribute to their `LevelFS` value. Information on how to 
check your `LevelFS` score can be found on the 
["How can I see my current FairShare priority?"](../../getting_started/faq.md#how-can-i-see-my-current-fairshare-priority) section of our FAQ page.

```{note}
If there are no other pending jobs, and enough resources are 
available, then your job will run regardless of your previous usage.
```

### Priority Score
When you request resources on Alpine, your job's priority determines its 
position in the queue relative to other jobs. A job’s priority is based on 
multiple factors, including (but not limited to) FairShare score, job age, 
resources requested, job size, and QOS. 

### Allocations

```{warning}
**Allocations for CSU and AMC are managed by those institutions.** Please see the **CSU** and **AMC** tabs in each section below for more information.
```


#### Alpine Allocation Tiers

(tabset-ref-alpine-alloc-tiers)=
`````{tab-set}
:sync-group: tabset-alpine-allocs

````{tab-item} CU Boulder
:sync: alpine-cub-inst

**Trailhead:**

When you receive a Research Computing account, you are automatically 
assigned a **Trailhead Auto-Allocation**, which grants you a fixed share 
of `ucb-general`.

The Trailhead is a great allocation for smaller jobs or 
testing and benchmarking your code. However, if you consume more than your allocated share of `ucb-general`,  your `LevelFS` will decrease, causing your 
priority score to decrease. The end result is that your jobs will sit 
lower (i.e., longer) in the queue relative to other jobs.

One way to combat this is to apply for an allocation. In addition to the Trailhead auto-allocation (`ucb-general`) that all users are awarded automatically, CURC offers two 
additional tiers to accommodate larger computing needs on Alpine, called **Ascent** and **Peak**.

**Ascent:**

The **Ascent** allocation tier provides CU Boulder users 
with {{ boulder_ascent_SUs }} SUs over a 12 month period. Please see the table below for a comparison with other allocation tiers; application instructions are in the next section.

**Peak:**

The **Peak Allocation** tier is 
aimed at projects that will consume between {{ boulder_ascent_SUs }} and {{ boulder_peak_SUs }} SUs in a 
12 month period. Please see the table below for a comparison with other allocation tiers; application instructions are in the next section.

**Comparison of Allocation Tiers:**

::::{dropdown} Show 
:icon: note

The following table summarizes the required information, size, approval 
process, and renewal requirements for each tier.

|                          | **Trailhead Auto-Allocation**                                                | **Ascent Allocation**                                                                                                                                                                                                                      | **Peak Allocation**                                                                                                                                                                                                                                                                                                              |
|--------------------------|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Required information** | - None                                                                       | - Title and project description<br>- Funding information<br>- Field of study/research area<br>- PI and role<br>- IdentiKeys of collaborators<br>- Slurm partitions to be used<br>- Acknowledgement of CURC User Polices                    | - All information required by Ascent allocation<br>- Example jobs<br>- List of software the project utilizes and how they will install each application                                                                                                                                                                          |
| **Size**                 | - Approximately {{ trailhead_SUs }} SUs per month                                          | - Equivalent to 0.25% of the system (currently {{ boulder_ascent_SUs }} SUs) for one year<br>- Total SU limit equal to 1% of the system (currently {{ boulder_ascent_SU_group_limit }} SUs) per research group/PI<br>    - Group members may divide this among as many allocations as desired | - Variable (based on user's request), but must not exceed the number of SUs equivalent to 5% of the system (currently {{ boulder_peak_SUs }} SUs) over a one-year period<br>- Members of research group may divide the maximum amount of SUs among as many or as few allocations as they desire                                                      |
| **Approval process**     | - Automatically granted when users register for a Research Computing account | - Approved quickly and without review by the Allocations Committee<br>- User Support will include summary information about Ascent allocations from the previous month in the monthly Allocations Committee meeting                        | - Peak allocation proposals will be initially reviewed by a member of CURC User Support<br>    - Users may be asked to improve the memory efficiency and CPU efficiency of their jobs<br>- Once the team member is satisfied with the proposal, it will be reviewed by the Allocations Committee during the next monthly meeting |
| **Renewal requirements** | - None; Trailhead allocations do not expire                                  | - Sign their acknowledgement of CURC User Policies<br>- There is no limit to the number of renewals                                                                                                                                        | - Same as Ascent allocation renewal requirements, but users may be asked to justify the size of their allocation based on the previous year's usage                                                                                                                                                                              |

Individual and group size limits for new and renewed allocations will be 
reviewed on an annual basis.

::::


````

````{tab-item} RMACC
:sync: alpine-rmacc-inst

**Trailhead:**

When you receive a Research Computing account, you are automatically 
assigned a **Trailhead Auto-Allocation**, which grants you a fixed share 
of `rmacc-general`.

The Trailhead is a great allocation for smaller jobs or 
testing and benchmarking your code. However, if you consume more than your allocated share of `rmacc-general`,  your `LevelFS` will decrease, causing your 
priority score to decrease. The end result is that your jobs will sit 
lower (i.e., longer) in the queue relative to other jobs.

One way to combat this is to apply for an allocation. In addition to the Trailhead auto-allocation (`rmacc-general`) that all users are awarded automatically, CURC offers RMACC users an 
additional tier to accommodate larger computing needs on Alpine, called RMACC Ascent.

**Ascent:**

The RMACC Ascent tier provides users with {{ rmacc_ascent_SUs }} SUs over a 12 month period. Please see the table below for a comparison with other allocation tiers; application instructions are in the next section.

**Peak:**

At this time, RMACC users are not eligible for Peak allocations. However, if you are an RMACC user with additional resource needs beyond the RMACC Ascent allocation, please contact us at (<rc-help@colorado.edu>).

**Comparison of Allocation Tiers:**

::::{dropdown} Show 
:icon: note

The following table summarizes the required information, size, approval 
process, and renewal requirements for each tier.

|                          | **Trailhead Auto-Allocation**                                                | **RMACC Ascent Allocation**                                                                                                                                                                                                                                        |
|--------------------------|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Required information** | - None                                                                       | - Title and project description<br>- Funding information<br>- Field of study/research area<br>- Institutional affiliation<br>- PI and role<br>- ACCESS/XSEDE usernames of collaborators<br>- Slurm partitions to be used<br>- Acknowledgement of CURC User Polices |
| **Size**                 | - Approximately {{ trailhead_SUs }} SUs per month                                          | - Currently {{ rmacc_ascent_SUs }} SUs                                                                                                                                                                                                                                            |
| **Approval process**     | - Automatically granted when users register for a Research Computing account | - Approved quickly and without review by the Allocations Committee                                                                                                                                                                                                 |
| **Renewal requirements** | - None; Trailhead allocations do not expire                                  | - Handled on a case-by-case basis; please contact us  

Individual and group size limits for new and renewed allocations will be 
reviewed on an annual basis.

::::

````

````{tab-item} CSU
:sync: alpine-csu-inst

**Allocations for CSU are managed by that institution.** CSU users who are interested in learning about their institution's Alpine allocation processes should email (<rc-help@colorado.edu>).

````

````{tab-item} AMC
:sync: alpine-amc-inst

**Allocations for AMC are managed by that institution.** AMC users who are interested in learning about their institution's Alpine allocation processes should email (<hpcsupport@cuanschutz.edu>).

````

`````


```{note}
CURC's tiered allocations are structured in a way such that your jobs are 
likely to have a higher priority if they are running in Ascent, Peak, or RMACC Ascent 
Allocations than if they are running in a Trailhead 
Auto-Allocation.
```

#### Get an Allocation

(tabset-ref-alpine-alloc-procs)=
`````{tab-set}
:sync-group: tabset-alpine-allocs

````{tab-item} CU Boulder
:sync: alpine-cub-inst

**Ascent:**

Step 1: Fill out the [Ascent Allocation 
Request](https://forms.office.com/r/eAA15b8Gsg) form. You need to be 
logged in to Office 365 with your CU Boulder account.

Step 2: Look out for an email message from the CURC ticketing system (<rc-help@colorado.edu>) indicating when your allocation is ready to use.

**Peak:**

Step 1: Download and complete the [Peak Allocation Request Supplementary 
Information](https://o365coloradoedu.sharepoint.com/:x:/s/RC-Team/EajdPBAejjpDru7kvEEA29QBI8CoO8lj7-kUjotBIIusEg?e=geLBBP) 
document. You need to be logged into Office 365 with your CU Boulder 
account.

Step 2: Fill out the [Peak Allocation 
Request](https://forms.office.com/r/5VtLpiCh01) form. You need to be 
logged into Office 365 with your CU Boulder account.
The last question will ask you to upload your completed Peak Allocation 
Request Supplementary Information document from step 1. 

Step 3: Look out for email messages from the CURC ticketing system (<rc-help@colorado.edu>). User Support will contact you when the proposal 
is received, during the initial 
review stages, and when the allocation is ready to use.


````

````{tab-item} RMACC
:sync: alpine-rmacc-inst

**Ascent:**

Step 1: Fill out the [RMACC Ascent Allocation 
Request](https://forms.office.com/Pages/ResponsePage.aspx?id=G4vtPQ0HKUaC5MCwGfRgVxVuc407_5dMhLp4SuO1aoJUODlNNThXTTRUNklTQk02TlFKV1gxUUZTWCQlQCN0PWcu) form. You need to be 
logged in to Office 365 with your CU Boulder account.

Step 2: Look out for an email message from the CURC ticketing system (<rc-help@colorado.edu>) indicating when your allocation is ready to use.

**Peak:**

At this time, RMACC users are not eligible for Peak allocations. However, if you are an RMACC user with additional resource needs beyond the RMACC Ascent allocation, please contact us at (<rc-help@colorado.edu>).

````

````{tab-item} CSU
:sync: alpine-csu-inst

**Allocations for CSU are managed by that institution.** CSU users who are interested in learning about their institution's Alpine allocation processes should email (<rc-help@colorado.edu>).

````

````{tab-item} AMC
:sync: alpine-amc-inst

**Allocations for AMC are managed by that institution.** AMC users who are interested in learning about their institution's Alpine allocation processes should email (<hpcsupport@cuanschutz.edu>).

````

`````

#### Renewing Your Allocation

```{note}
**Trailhead** Auto-Allocations do not expire.
```

(tabset-ref-alpine-alloc-renew)=
`````{tab-set}
:sync-group: tabset-alpine-allocs

````{tab-item} CU Boulder
:sync: alpine-cub-inst

**Ascent:**

Step 1: Keep an eye on your email inbox for a notification that your allocation is about to expire. Notifications will be sent one month prior to expiration to give you plenty of time to renew. Allocations will automatically expire one year after they are provisioned. 

Step 2: Fill out the [Ascent Allocation Renewal](https://forms.office.com/r/1ymj7gxQF3) form. You need to be logged into Office 365 with your CU Boulder account.

Step 3: Look out for email messages from the CURC ticketing system (<rc-help@colorado.edu>). User Support will contact you when the renewal request is received and when the renewed allocation is ready to use.

**Peak:**

Step 1: Keep an eye on your email inbox for a notification that your allocation is about to expire. Notifications will be sent one month prior to expiration to give you plenty of time to renew. Allocations will automatically expire one year after they are provisioned. 

Step 2: Fill out the [Peak Allocation Renewal](https://forms.office.com/r/wimT1SCsWz) form. You need to be logged into Office 365 with your CU Boulder account.

Step 3: Look out for email messages from the CURC ticketing system (<rc-help@colorado.edu>). User Support will contact you when the renewal request is received and when the renewed allocation is ready to use.


````

````{tab-item} RMACC
:sync: alpine-rmacc-inst

**Ascent:**

Step 1: Keep an eye on your email inbox for a notification that your allocation is about to expire. Notifications will be sent one month prior to expiration to give you plenty of time to renew. Allocations will automatically expire one year after they are provisioned. 

Step 2: Please send an email to <rc-help@colorado.edu> requesting the renewal of your allocation. Be sure to provide your CURC username, the name of your allocation, and the CURC usernames of any of your collaborators.

Step 3: Look out for email messages from the CURC ticketing system (<rc-help@colorado.edu>). User Support will contact you when the renewal request is received and when the renewed allocation is ready to use.

````

````{tab-item} CSU
:sync: alpine-csu-inst

**Allocations for CSU are managed by that institution.** CSU users who are interested in learning about their institution's Alpine allocation processes should email (<rc-help@colorado.edu>).

````

````{tab-item} AMC
:sync: alpine-amc-inst

**Allocations for AMC are managed by that institution.** AMC users who are interested in learning about their institution's Alpine allocation processes should email (<hpcsupport@cuanschutz.edu>).

````

`````

Alpine is jointly funded by the University of Colorado Boulder, the University of Colorado Anschutz, Colorado State University, and the 
National Science Foundation (award 2201538).