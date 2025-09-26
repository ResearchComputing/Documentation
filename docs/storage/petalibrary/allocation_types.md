# Allocation Tiers

## Overview of PetaLibrary Tiers

```{eval-rst}
.. figure:: ./pl_feature_comparison_chart.png
   :align: center
   :scale: 100%
```
*Data Integrity terminology definitions can be found [here](#data-integrety-terminology).

**SMB is only available to CU Boulder customers.

## In-depth information on PetaLibrary Tiers

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

The benefits of purchasing an active+archive allocation over purchasing your own active and archive allocations:
* _No object limit_: a standalone archive allocation is subject to the 10,000 object (file/directory) limit. Since active allocations do not have an object limit, the archive component of an active+archive allocation also does not have an object limit.
* _Automatic replication_: We replicate the data between the two tiers for you, every fifteen minutes.

The means of replication between the active and archive tiers uses ZFS snapshots. The replication process copies any snapshots that exist on the active tier but do not exist on the archive tier, and likewise removes any snapshots that exist on the archive tier but are not present on the active tier. Therefore, if you ask us to prune ZFS snapshots aggressively on your active+archive allocation, this reduces the snapshot count on both the active and the archive tier. The active+archive tier is not an incremental backup, it is a time-delayed mirror of the ZFS snapshots of your active allocation. Snapshots are the best way to preserve your historical data in incremental steps, and replication ensures that your snapshots exist in two physical buildings. Physical isolation is important for events like fire and water damage that could damage one copy of your data beyond hope of recovery.

````

````{tab-item} Archive+DR
:sync: tabset-ucb-pl-tier-types-archive-dr

The PetaLibrary Archive tier is configured to maximize data integrity over performance. Its triple parity data protection makes it a robust system with respect to disk failures. Although the Archive allocation tier is robust, all current allocations within this tier are hosted in a single location. In the event of a disaster at this location, we cannot guarantee the safety of this data. To add an extra layer of protection, we offer the Archive + DR (Disaster Recovery) tier. The Archive + DR tier offers the same benefits as the Archive tier in addition to a monthly backup of the data to an offsite location. The backup process and any needed restoration efforts will be managed entirely by CURC staff.

````

`````


## Data Integrety Terminology

A PetaLibrary `active` or `archive` allocation is a single copy of your data that is not backed up. PetaLibrary can be a component of a good backup strategy, but for data that cannot be replaced, an active or archive PetaLibrary should not be the only copy. The PetaLibrary `active+archive` and `archive+DR` (DR=disaster recovery) tiers provide additional redundancy for your data.  Common terms used to describe data redundancy and integrety are defined below. 

* __*Snapshots*__ are read-only representations of your PetaLibrary allocation on the `active` or `archive` tier at the time the snapshot was taken. [Snapshots](./zfs_snapshots.md) enable users to recover data that they have unintentially deleted, during a specified retention period (default is seven days). Snapshots are not "backups" in the strict sense because they are not static, and because they reside on the same storage device as the primary data copy. 
  
* __*Replication*__ in the case of PetaLibrary refers specifically to the `active+archive` tier, and is the process whereby the snapshots from your `active` allocation are mirrored the `archive` tier in a separate data center on the CU Campus.  This process provides an additioal layer of disaster recovery protection compared to `snapshots` (the default for "active" allocations).
  
* __*Backup*__ in the case of PetaLibrary refers specifically to the `active+DR` tier, and is the process whereby a monthly backup copy of the "archive" allocation is made to an offsite data center.  This process provides an additional layer of disaster recovery protection compared to `snapshots` (the default for `archive` allocations).
  
* __*RAID Parity*__ is the process whereby your copy of data on a given PetaLibrary tier is written to multiple disks.  The PetaLibrary `active` tier employs double parity (up to two simultaneous disk failures will not cause data loss), and the `archive` tier employs triple parity (up to three simultaneous disk failures will not cause data loss).  
  
* __*Checksumming*__ is the process whereby a value that is derived from a data object is repeatedly checked over time to confirm that the data has not unnecessarily changed.  Checksumming is a way to detect and mitigate data corruption over time. 
     
## Alternative non-PetaLibrary backup options

Offsite backup options are available from cloud-based storage providers. 

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
