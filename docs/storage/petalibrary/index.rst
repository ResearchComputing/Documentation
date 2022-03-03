PetaLibrary
===========

The PetaLibrary is a University of Colorado Boulder Research Computing service that supports the storage, archival, and sharing of research data. It is available at a subsidized cost to any researcher affiliated with the University of Colorado System (Boulder, Anschutz, Denver, Colorado Springs). It is available at an unsubsidized cost to researhers from other institutions. 
 
### PetaLibrary Features 
- Minimum project size: 1 TB/year
- 2 classes of storage: active and archive
     * See our [website](https://www.colorado.edu/rc/resources/petalibrary/storageandrates) for pricing information
<br/><br/>
- New customers are initially limited to a maximum allocation size of: 
     * 200 TB* in Active Storage
     * 100 TB* in Archive Storage
		 > _*Pending availability_

PetaLibrary access is subject to the [PetaLibrary Terms of Service](https://www.colorado.edu/rc/resources/petalibrary/tos).


### Accessing the PetaLibrary

#### General Access
Each person who accesses the PetaLibrary is required to have a Research Computing account and Duo two-factor authentication. 

PetaLibrary storage is presented as a file system directory under either:
```
/pl/active/<your_allocation_name>
/pl/archive/<your_allocation_name>
```

Access to a PetaLibrary allocation is granted using an access group. This group may be an existing group in the Research Computing environment or a new group created specifically for the purpose of managing access to the allocation. Allocation users are made members of this access group by requesting that the allocation owner or delegate contact to the RC help desk at [rc-help@colorado.edu](rc-help@colorado.edu) to request their RC account be added to the group.

#### Request a PetaLibrary allocation

Request PetaLibrary storage by filling out the application form at the [RC PetaLibrary page](https://www.colorado.edu/rc/resources/petalibrary), under the "Request a new PetaLibrary allocation" link.  

> Each PetaLibrary allocation *must* define an allocation owner, read more about PetaLibrary [owners and contacts and their individual roles/responsibilities](https://curc.readthedocs.io/en/latest/petalibrary/ownership.html). 


 When a new allocation is created the path to it is defined and provisioned based on a name selected by you. For example, Jane Doe might name her lab's allocation `jdoe_lab`. 

- **To access active storage:** Log in to a Research Computing via login.rc.colorado.edu
    and navigate to: `/pl/active/<your_allocation_name>` (e.g., `/pl/active/jdoe_lab`)

- **To access archive storage:** Archive storage is located at: `/pl/archive/<your_allocation_name>`

Access via the login nodes is **not recommended** for frequent or large read/writes of archived data.

### Service Classes

#### Two primary classes of storage are available:
##### Active
- Appropriate for data that is frequently written or read
- Stores data in a parity-protected RAID array or similar
- Directly accessible (read+write) from Research Computing compute resources
##### Archive
- Appropriate for data that is infrequently accessed
- Stores data on tapes in a robotic tape library, with all data written to at least two tapes
- Not accessible from Research Computing compute resources

### Performance
PetaLibrary is a shared infrastructure and the instantaneous performance will vary depending on each individual workload and competing workloads from other clients.

The PetaLibrary service is designed for file storage and retrieval, and is not an ideal backend for highly transactional workloads (e.g., relational databases).

### More information

* [https://www.colorado.edu/rc/resources/petalibrary](https://www.colorado.edu/rc/resources/petalibrary)

----

.. toctree::
    :maxdepth: 2
    :glob:

    *
