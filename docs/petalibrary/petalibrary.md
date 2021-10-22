## The PetaLibrary

The PetaLibrary is a University of Colorado Boulder Research Computing payed service that supports the storage, archive, and sharing of research data. It is available at a subsidized cost to any researcher affiliated with the University of Colorado Boulder.
 
### PetaLibrary Features 
- Minimum project size: 1 TB/year
- 2 classes of storage: active and archive
     * See our [website](https://www.colorado.edu/rc/resources/petalibrary/storageandrates) for pricing information
- New customers are limited to either: 
     * 200 TB* in Active Storage
     * 100 TB* in Archive Storage
		 > _*Pending availability_

PetaLibrary access is subject to the [PetaLibrary Terms of Service](https://www.colorado.edu/rc/resources/petalibrary/tos).


### Accessing the PetaLibrary

#### General Access

PetaLibrary storage is presented as a file system directory under either:
```
/pl/active/<your_allocation_name>
/pl/archive/<your_allocation_name>
```

Access to a PetaLibrary allocation is granted using an access group. This group may be an existing group in the Research Computing environment or a new group created specifically for the purpose of managing access to the allocation. Allocation users are made members of this access group using their existing Research Computing accounts by request of the allocation owner or delegate contact to the [RC help desk](rc-help@colorado.edu).

> _**Note:**_ Each person who accesses the PetaLibrary is required to have a Research Computing account and two-factor authentication. 

#### Request a PetaLibrary allocation

Request PetaLibrary storage by filling out the application form at the [RC PetaLibrary page](https://www.colorado.edu/rc/resources/petalibrary), under the "Request a new PetaLibrary allocation" link.  

> _**Note:**_ Each PetaLibrary allocation *must* define an allocation owner, read more about PetaLibrary [owners and contacts and their individual roles/responsibilities](https://curc.readthedocs.io/en/latest/petalibrary/ownership.html). 


 When an allocation is created the full, supported path is defined and provided, based on a name selected by you. For example, Jane Doe might name her lab's allocation `jdoe_lab`. 

- **To access active storage:** Log in to a Research Computing via login.rc.colorado.edu
    and navigate to: `/pl/active/<your_allocation_name>` (e.g., `/pl/active/jdoe_lab`)

- **To access archive storage:** Archive storage is located at: `/pl/archive/<your_allocation_name>`

> _**Note:**_ Access via the login nodes is not recommended for frequent or large read/writes of archived data.

### Service Classes

#### Two primary classes of storage are available:
##### Active
- Appropriate for data that is frequently written or read
- Stores data in a parity-protected RAID array or similar
- Directly accessible (read+write) from Research Computing compute resources
##### Archive
- Appropriate for data that is infrequently accessed
- Stores data on tapes in a robotic tape library, with all data written to at least two tapes

### Performance
PetaLibrary is a shared infrastructure, and actual, individual performance will vary depending on each individual workload and competing workloads from other clients.

The PetaLibrary service is designed for file storage and retrieval, and is not an ideal backend for highly transactional workloads (e.g., relational databases).


### More information

* [https://www.colorado.edu/rc/resources/petalibrary](https://www.colorado.edu/rc/resources/petalibrary)
