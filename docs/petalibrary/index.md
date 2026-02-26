# Introduction

The PetaLibrary is a University of Colorado Boulder Research Computing service that supports the storage, archival, and sharing of research data. It is available to any researcher affiliated with the University of Colorado System (Boulder, Anschutz, Denver, Colorado Springs) at an internal cost rate. It is available at an external cost rate to researchers from other RMACC institutions.  General information can be found on this page. Information on specific topics can be found in the menu to the left. 

```{note}
All PetaLibrary allocations are subject to the [PetaLibrary Terms of Service](https://colorado.edu/rc/resources/petalibrary/tos).
```

```{warning}
A PetaLibrary allocation on its own is a single copy of your data that is not backed up. Details and options for backing up your research data are described in the [PetaLibrary Allocation Tier](https://curc.readthedocs.io/en/latest/petalibrary/allocation_types.html) documentation.
```
 
## How to obtain a PetaLibrary allocation

Step 1: Choose the [allocation tier](./allocation_types.md) that is right for you.

Step 2: [Request](https://powerforms.docusign.net/189e8917-6143-431e-ad8a-663bddf6a345?env=na2&amp;acct=088d5d64-ef4d-40bb-acf2-480eabbf546d&amp;accountId=088d5d64-ef4d-40bb-acf2-480eabbf546d) a new PetaLibrary allocation (links to Docusign form)

Step 3: Learn to use PetaLibrary via this documentation.

```{note}
* Minimum allocation size: 1 TB
* Maximum _initial_ allocation size for new customers: 200 TB, pending availability.
```

## Requirements

### Ownership
Each PetaLibrary allocation *must* define an allocation owner, read more about PetaLibrary [owners and contacts and their individual roles/responsibilities](./ownership.md). 

### CURC Account
Each person who accesses the PetaLibrary is required to have a Research Computing account and Duo two-factor authentication. PetaLibrary storage is presented as a file system directory based on the type of allocation. For more information about obtaining a CURC account, see our [Logging In](../getting_started/logging-in.md) page. 

### Access
Access to a PetaLibrary allocation is granted using an access group. This group may be an existing group in the Research Computing environment or a new group created specifically for the purpose of managing access to the allocation. To add new users to the allocation, the allocation owner or their authorized technical contact should follow the instructions provided in the FAQ [How can I add users to a Linux group?](../getting_started/faq.md#how-can-i-add-users-to-a-linux-group) dropdown, where the `Path to directory/file` is the PetaLibrary allocation location. This request can be made at any time. 

### Acknowledgement

When data stored in PetaLibrary is used in a publication please include a [citation](../getting_started/acknowledge_curc_resources.md#acknowledging-petalibrary).

## Performance
PetaLibrary is a shared infrastructure and the instantaneous performance will vary depending on each individual workload and competing workloads from other clients. The PetaLibrary service is designed for file storage and retrieval, and is not an ideal service for highly transactional workloads (e.g., relational databases).



