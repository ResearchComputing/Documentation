# PetaLibrary Allocation Types


(tabset-ref-ucb-pl-tier-types)=
`````{tab-set}
:sync-group: tabset-ucb-pl-tier-types

````{tab-item} Active
:sync: tabset-ucb-pl-tier-types-active

PetaLibrary active allocations are the most performant PetaLibrary tier (please note that performant is a relative term -- our parallel scratch filesystem will outperform any PetaLibrary tier). The underlying hardware is configured to be suitable for direct compute access, and as such is accessible from all compute environments (Alpine, Blanca, Open OnDemand). All active allocations offer the following features:

 - interactive (NFS) access from RC login and compute nodes
 - accessible using Globus/rsync/sftp via the data transfer node (DTN) hosts
 - SMB access (not enabled by default, only accessible to UCB customers from UCB campus network)
 - no object (file/directory) limit
 - double parity (up to two simultaneous disk failures will not cause data loss)
 - snapshots (see documentation on [snapshots](./zfs_snapshots.md) for more information)
 - full data checksumming, validated monthly (via ZFS scrub)
 - lz4 data compression

````

````{tab-item} Archive
:sync: tabset-ucb-pl-tier-types-archive

PetaLibrary archive allocations are configured to maximize data integrity over performance. As such, archive allocations are not accessible from compute nodes, but can be accessed interactively on login nodes. Historically the archive tier was tape-based, although recently is was changed to disk. An object limit of 10,000 files/directories per terabyte of space remains in place to preserve the option to move back to tape in the future, should the service grow to a point where tape-based storage is more fiscally viable.

The archive feature list is similar to active, with the major differences being: no direct access from RC compute nodes, no SMB access, file/directory count is limited, triple parity is used for data protection rather than double parity, and a different compression algorithm is used. In summary, all archive allocations offer the following features:

 - interactive (NFS) access from login nodes
 - accessible using Globus/rsync/sftp via the data transfer node (DTN) hosts
 - 10,000 object (file/directory) per terabyte limit
 - triple parity (up to three simultaneous disk failures will not cause data loss)
 - snapshots (see documentation on [snapshots](./zfs_snapshots.md) for more information)
 - full data checksumming, validated monthly (via ZFS scrub)
 - zstd data compression

````

````{tab-item} Active+Archive
:sync: tabset-ucb-pl-tier-types-active-archive

The PetaLibrary active+archive is a means of automatically replicating your data across our active and archive PetaLibrary tiers. Rather than purchase an active and archive allocation and synchronizing data between the two, you can purchase the active+archive tier, and we will manage the replication for you. With this type of allocation, you have full access to the active tier only, and we manage replicating data to the archive tier for you.

The biggest benefit of purchasing an active+archive allocation over purchasing your own active and archive allocations is that a standalone archive allocation is subject to the 10,000 object (file/directory) limit. Since active allocations do not have an object limit, the archive component of an active+archive allocation also does not have an object limit.

Historically RC offered this service when the active and archive tiers were using different underlying storage systems, which made it difficult to do daily replication. The service was not available to customers for several years, but due to recent technical changes, we are able to not only bring back the service, but are also able to replicate data between the two tiers every fifteen minutes.

The means of replication between the active and archive tiers uses ZFS snapshots. The replication process copies any snapshots that exist on the active tier but do not exist on the archive tier, and likewise removes any snapshots that exist on the archive tier but are not present on the active tier. Therefore, if you ask us to prune ZFS snapshots aggressively on your active+archive allocation, this reduces the snapshot count on both the active and the archive tier. The active+archive tier is not an incremental backup, it is a time-delayed mirror of the ZFS snapshots of your active allocation. Snapshots are the best way to preserve your historical data in incremental steps, and replication ensures that your snapshots exist in two physical buildings. Physical isolation is important for events like fire and water damage that could damage one copy of your data beyond hope of recovery.

````

````{tab-item} Archive+DR
:sync: tabset-ucb-pl-tier-types-archive-dr

The PetaLibrary Archive tier is configured to maximize data integrity over performance. Its triple parity data protection makes it a robust system with respect to disk failures. Although the Archive allocation tier is robust, all current allocations within this tier are hosted in a single location. In the event of a disaster at this location, we cannot guarantee the safety of this data. To add an extra layer of protection, we offer the Archive + DR (Disaster Recovery) tier. The Archive + DR tier offers the same benefits as the Archive tier in addition to a monthly backup of the data to an offsite location. The backup process and any needed restoration efforts will be managed entirely by CURC staff.

````

`````


## PetaLibrary and data redundancy 

A PetaLibrary `active` or `archive` allocation is a single copy of your data that is not backed up. You may be familiar with the 3-2-1 backup strategy, which recommends having three copies of your data, using two different types of media, and having one copy at a different location. An active or archive PetaLibrary allocation is a **single** copy of your data on one type of media in a single location, so PetaLibrary can be a component of a good backup strategy, but for data that cannot be replaced, an active or archive PetaLibrary should not be the only copy. 

PetaLibrary does have some forms of redundancy, such as RAID (whereby your copy of data is written to multiple disks on our system) to minimize service outages caused by disk failures, and snapshots which can be useful if files are accidentally damaged or removed. Neither RAID nor snapshots are an effective backup strategy to protect against other causes of data loss such as hardware and software failures, or user and administrative errors. The only way to mitigate the risk to your data is to not rely on a single active or archive PetaLibrary allocation to be the sole copy. 

### Options for backing up your data

- Replicated PetaLibrary `active+archive` allocation:  
    - _Access details:_
        - You purchase an active allocation, and we replicate it to the archive tier for you.
        - For more information see our [Active + Archive](./allocation_types.md#activearchive) description
    - Pros:
        - Convenient
        - No data volume or object limits
        - Likely lower cost compared to AWS option (see below)
    - Cons:
        - You are required to obtain an equivalent amount of archive space as active space
        - On-campus backup facility, so not a completely disaster-proof
        - You incur additional cost
- PetaLibrary `archive+DR` (Disaster Recovery) allocation:  
    - _Access details:_
        - You purchase an archive allocation, and we back it up monthly to an offsite location for you.
        - For more information see our [Archive + DR](./allocation_types.md#archive--dr-disaster-recovery) description
    - Pros:
        - Convenient
        - No data volume limit
        - Likely lower cost compared to AWS option (see below)
    - Cons:
        - limit of 10,000 objects per TB of data
        - You incur additional cost
- Microsoft OneDrive:  
    - _Access details:_  
        - CU Boulder affiliates all have 5 TB of space in Microsoft OneDrive. You can use [Globus](./onedrive.md#using-globus) or [rclone](./onedrive.md#using-rclone) to copy data between PetaLibrary and OneDrive.  
    - _Pros:_ 
        - Free up to 5 TB using OneDrive 
        - Copy of data is off-campus 
    - _Cons:_ 
        - Limits on [file sizes](https://support.microsoft.com/en-us/office/restrictions-and-limitations-in-onedrive-and-sharepoint-64883a5d-228e-48f5-b3d2-eb39e07630fa#individualfilesize)
        - OneDrive can be sensitive to [unconventional file names and long paths](https://support.microsoft.com/en-us/office/restrictions-and-limitations-in-onedrive-and-sharepoint-64883a5d-228e-48f5-b3d2-eb39e07630fa#invalidcharacters)  
- AWS S3 bucket:  
    - _Access details:_ 
        - You can use rclone to copy your data to AWS for a monthly fee. Contact <rc-help@colorado.edu> for options to establish access to AWS. 
    - _Pros:_ 
        - No data volume limit 
        - AWS data integrity assurance is very high 
        - Copy of data is off-campus 
    - _Cons:_ 
        - You incur additional costs 
