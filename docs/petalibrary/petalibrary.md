## The PetaLibrary

The PetaLibrary is a University of Colorado Boulder Research Computing service that supports the storage, archive, and sharing of research data. It is available at a subsidized cost to any researcher affiliated with the University of Colorado Boulder.
 
### PetaLibrary Features 
- Minimum project size: 1 TB/year
- 2 classes of storage: active and archive
     * See our [website](https://www.colorado.edu/rc/resources/petalibrary/storageandrates) for pricing information
- New customers are limited to either
     * 200 TB* in Active Storage, or
     * 100 TB* in Archive Storage
     * Email <rc-help@colorado.edu> to request more space if necessary
		 > _*Pending availability_

PetaLibrary access is subject to the [PetaLibrary Terms of Service](https://www.colorado.edu/rc/resources/petalibrary/tos).


### Accessing the PetaLibrary

PetaLibrary storage is presented as a file system directory with an administratively-defined and automatically-enforced size limit.

#### Request a PetaLibrary allocation

Request PetaLibrary storage by filling out the Docusign at the [RC PetaLibrary page](https://www.colorado.edu/rc/resources/petalibrary), under the "Request a new PetaLibrary allocation" link.  

Each PetaLibrary allocation must define an allocation owner, read more about PetaLibrary [owners and contacts and their individual roles/responsibilities](https://curc.readthedocs.io/en/latest/petalibrary/ownership.html). 
> _**Note:**_ Each person who accesses the PetaLibrary is required to have a Research Computing account and two-factor authentication. 


 When an allocation is created the full, supported path is defined and provided, based on a name slected by you. For example, Jane Doe might name her lab's allocation `jdoe_lab`. 

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

### Data Transfer
External access to PetaLibrary storage is provided primarily via the Research Computing data transfer service which supports Globus (reccomended), SFTP, and (by request only) anonymous FTP data transfer protocols. Local data backups, mounting PetaLibrary to a local system, and transfering data from Google Drive or a NAS are covered in the respective PetaLibrary documents.  

> More information on [data transfer](https://curc.readthedocs.io/en/latest/compute/data-transfer.html) at CURC



### More information

* [https://www.colorado.edu/rc/resources/petalibrary](https://www.colorado.edu/rc/resources/petalibrary)
