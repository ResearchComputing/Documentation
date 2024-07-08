## PetaLibrary Allocation Types

#### Active

PetaLibrary active allocations are the most performant PetaLibrary tier (please note that performant is a relative term -- our parallel scratch filesystem will outperform any PetaLibrary tier). The underlying hardware is configured to be suitable for direct compute access, and as such is accessible from all compute environments (Alpine, Blanca, Open OnDemand). All active allocations offer the following features:

 - interactive (NFS) access from RC login and compute nodes
 - accessible using Globus/rsync/sftp via the data transfer node (DTN) hosts
 - SMB access (not enabled by default, only accessible from UCB campus network)
 - no object (file/directory) limit
 - double parity (up to two simultaneous disk failures will not cause data loss)
 - snapshots (see documentation on [snapshots](zfs_snapshots.md) for more information)
 - full data checksumming, validated monthly (via ZFS scrub)
 - lz4 data compression

#### Archive

PetaLibrary archive allocations are configured to maximize data integrity over performance. As such, archive allocations are not accessible from compute nodes, but can be accessed interactively on login nodes. Historically the archive tier was tape-based, although recently is was changed to disk. An object limit of 10,000 files/directories per terabyte of space remains in place to preserve the option to move back to tape in the future, should the service grow to a point where tape-based storage is more fiscally viable.

The archive feature list is similar to active, with the major differences being: no direct access from RC compute nodes, no SMB access, file/directory count is limited, triple parity is used for data protection rather than double parity, and a different compression algorithm is used. In summary, all archive allocations offer the following features:

 - interactive (NFS) access from login nodes
 - accessible using Globus/rsync/sftp via the data transfer node (DTN) hosts
 - 10,000 object (file/directory) per terabyte limit
 - triple parity (up to three simultaneous disk failures will not cause data loss)
 - snapshots (see documentation on [snapshots](zfs_snapshots.md) for more information)
 - full data checksumming, validated monthly (via ZFS scrub)
 - zstd data compression

#### Active+archive

The PetaLibrary active+archive is a means of automatically replicating your data across our active and archive PetaLibrary tiers. Rather than purchase an active and archive allocation and synchronizing data between the two, you can purchase the active+archive tier, and we will manage the replication for you. With this type of allocation, you have full access to the active tier only, and we manage replicating data to the archive tier for you.

The biggest benefit of purchasing an active+archive allocation over purchasing your own active and archive allocations is that a standalone archive allocation is subject to the 10,000 object (file/directory) limit. Since active allocations do not have an object limit, the archive component of an active+archive allocation also does not have an object limit.

Historically RC offered this service when the active and archive tiers were using different underlying storage systems, which made it difficult to do daily replication. The service was not available to customers for several years, but due to recent technical changes, we are able to not only bring back the service, but are also able to replicate data between the two tiers every fifteen minutes.

Note that the means of replication between the active and archive tiers uses ZFS snapshots. The replication process copies any snapshots that exist on the active tier but do not exist on the archive tier, and likewise removes any snapshots that exist on the archive tier but are not present on the active tier. Therefore, if you ask us to prune ZFS snapshots aggressively on your active+archive allocation, this reduces the snapshot count on both the active and the archive tier. The active+archive tier is not an incremental backup, it is a time-delayed mirror of the ZFS snapshots of your active allocation. Snapshots are the best way to preserve your historical data in incremental steps, and replication ensures that your snapshots exist in two physical buildings. Physical isolation is important for events like fire and water damage that could damage one copy of your data beyond hope of recovery.

#### Archive + DR

The PetaLibrary Archive tier is configured to maximize data integrity over performance. Its triple parity data protection makes it a robust system with respect to disk failures. Although the Archive allocation tier is robust, all current allocations within this tier are hosted in a single location. In the event of a disaster at this location, we cannot guarantee the safety of this data. To add an extra layer of protection, we offer the Archive + DR (Disaster Recovery) tier. The Archive + DR tier offers the same benefits as the Archive tier (see [Archive](#archive) section above) in addition to a monthly backup of the data to an offsite location. The backup process and any needed restoration efforts will be managed entirely by CURC staff.