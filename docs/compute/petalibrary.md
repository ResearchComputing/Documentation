## The PetaLibrary

### Description of service

The University of Colorado Boulder Research Computing _PetaLibrary_ research data storage service is available to any researcher affiliated with the University of Colorado Boulder. Storage space is pre-purchased, with a minimum purchase of 1 TB for 1 year.

#### Access

External access to PetaLibrary storage is provided primarily via the Research Computing data transfer service which supports Globus, SFTP, and (by request only) anonymous FTP data transfer protocols.

#### Service classes

Two primary classes of storage are available:

__Active__

* Appropriate for data that is frequently written or read
* Stores data in a parity-protected RAID array or similar
* Directly accessible (read+write) from Research Computing compute resources

__Archive__

* Appropriate for data that is infrequently accessed
* Stores data on tapes in a robotic tape library, with all data written to at least two tapes

### Allocations

PetaLibrary storage is presented as a file system directory with an administratively-defined and automatically-enforced size limit. When an allocation is created the full, supported path is defined and provided, based on an agreed _allocation name_.

#### Allocation contacts

Each PetaLibrary allocation must define an _allocation owner_. This contact is often, but is not required to be, the Principal Investigator for a related research effort. Among other responsibilities, the allocation owner is required to ensure compliance with PetaLibrary Terms of Service, for themself and their authorized allocation users.

An optional _technical contact_ and _billing contact_ may also be defined. These contacts are treated as delegates of the allocation owner for normal or regular operation.

Additional _allocation users_ may also be granted access to the allocation.

#### Access control

Access to a PetaLibrary allocation is granted using an _access group_. This group may be an existing group in the Research Computing environment or a new group created specifically for the purpose of managing access to the allocation. _Allocation users_ are made members of this access group using their existing Research Computing accounts by request of the allocation owner or delegate contact to rc-help@colorado.edu. Changes to the access group membership must be authorized by the allocation owner or delegate contact. The allocation owner or delegate contact should audit access group membership at least annually.

The PetaLibrary relies on the overall Research Computing identity management directory and the CU Boulder identity management and “IdentiKey” authentication infrastructure. All PetaLibrary users must have a valid Research Computing user account.

All PetaLibrary allocations are also eligible to use the Globus Sharing service, with which Globus Online can be used to provide read and/or write access to your allocation to anyone with a Globus account, including individuals who do not have a Research Computing user account. Research Computing will sponsor one Globus Plus account (for share administration) per PetaLibrary allocation, typically via the allocation’s technical contact.

#### Fees

PetaLibrary storage is provided for an annual fee based on accessible capacity. Actual fees are evaluated internally and subject to change annually. Current rates are published at https://www.colorado.edu/rc/resources/petalibrary/storageandrates.

We do not provide refunds or pro-rate the PetaLibrary fee for any time lost due to repairs, maintenance events (planned or otherwise), or any other temporary down time.

#### Reports

A report indicating each allocation’s capacity, load, and access is automatically generated and distributed to each allocation owner and delegate contact.

#### Expiration and deletion

An allocation that has not been funded for its upcoming period is considered expired. When an allocation expires a notification is sent to the allocation owner and all allocation contacts notifying them of the allocation expiry. If the allocation remains unfunded for 30 days it may be made “read-only.” If the allocation remains unfunded for 60 days the allocation may be deleted, including all data.

### Reliability
The PetaLibrary is designed for low-cost, reliable, remote-accessible research data storage. Data stored in the PetaLibrary is protected from hardware failure by redundancies (either redundant copies or parity) __but is not “backed up.”__ The PetaLibrary may serve as a backup for data stored elsewhere. Optionally, replication of data between the active and archive storage classes may be sufficient for some needs.

The infrastructure supporting the PetaLibrary is funded through the Office of Information Technology. Operation of the PetaLibrary is expected to continue with regular funding through “renewal and replacement” contributions. In the event that Research Computing is unable or otherwise ceases to provide the PetaLibrary or any comparable service, at least 60 days advance notice will be given to all allocation owners and delegate contacts. It will be the responsibility of the client to transfer their data to other storage resources within that time window.

### Support

Authorized PetaLibrary users may request support and assistance via rc-help@colorado.edu. While Research Computing will make every effort to address each support request, those support requests which require domain-specific knowledge or expertise may not be able to be handled by Research Computing alone. In these cases, the support request may be forwarded to the allocation’s technical contact.

The PetaLibrary infrastructure is operated as a “best effort” service, with regular business hours 08:00 - 17:00, Monday - Friday. There is no guarantee of assistance or incident response after-hours, on weekends, or during campus holidays. Support requests, including, but not limited to, access control and account creation, are addressed during regular business hours.

While every reasonable effort will be made to ensure the reliability and availability of the PetaLibrary and of the data stored on it, access to data in the PetaLibrary may be affected by circumstances outside of the control of Research Computing.

### Maintenance

Planned maintenance of the PetaLibrary is usually scheduled on the first Wednesday of a given month. Upcoming maintenance, both planned and emergency, is announced at https://curc.statuspage.io.

### Performance
Research Computing will publish expected performance capabilities of each PetaLibrary class at https://www.colorado.edu/rc/resources/petalibrary; however, the PetaLibrary is a shared infrastructure, and actual, individual performance will vary depending on each individual workload and competing workloads from other clients.

The PetaLibrary service is designed for file storage and retrieval, and is not an ideal backend for highly transactional workloads (e.g., relational databases).


Use the PetaLibrary to store, archive and share research data.

- Minimum project size: 2 TB
- 2 classes of storage: active and archive
     * 5 different storage options within these classes
     * See our website for pricing information
- New customers are limited to either
     * 75 TB in Active Storage, or
     * 100 TB in Archive Storage
     * Email <rc-help@colorado.edu> to request more space if necessary


### Getting Started

Request access to the PetaLibrary by:

- Reading the PetaLibrary [Memorandum of
  Understanding](https://www.colorado.edu/rc/sites/default/files/attached-files/petalibrary_mou.pdf)

- Filling out the attached End User Agreement and Order Form (found in the MOU), and emailing those documents to <rc-help@colorado.edu>

Each person who accesses the PetaLibrary is required to have a Research Computing account and two-factor authentication. 

Your PetaLibrary allocation will have a name that is selected by you.  For example, Jane Doe might name her lab's allocation `jdoe_lab`. 

* **active** storage allocations will have the path `/pl/active/<your_allocation_name>` (e.g., `/pl/active/jdoe_lab`)

* **archive** storage allocations will have the path `/pl/archive/<your_allocation_name>` (e.g., `/pl/archive/jdoe_lab`)

Note that access via the login nodes is not recommended for frequent or large read/writes of archived data.

### Video tutorial

<iframe width="560" height="315" src="https://www.youtube.com/embed/i1TVYj4OQOY" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

### More information

* [https://www.colorado.edu/rc/resources/petalibrary](https://www.colorado.edu/rc/resources/petalibrary)
