## PetaLibrary Allocation Types

#### Active

PetaLibrary active allocations are the most performant PetaLibrary tier
(please note that performant is a relative term -- our parallel scratch
filesystem will outperform any PetaLibrary tier). The underlying hardware
is configured to be suitable for direct compute access, and as such is
accessible from all compute environments (Alpine, Blanca, Open OnDemand). All active allocations offer the following options:

 - interactive (NFS) access from RC login and compute nodes
 - accessible using Globus/rsync/sftp via the data transfer node (DTN) hosts
 - SMB access (not enabled by default, only accessible from UCB campus network)
 - no object (file/directory) limit
 - double parity (up to two simultaneous disk failures will not cause data loss)
 - snapshots (default schedule saves snapshots for one week)
 - full data checksumming, validated monthly (via zfs scrub)
 - lz4 data compression

#### Archive

PetaLibrary archive allocations are configured to maximize data integrity
over performance. As such, archive allocations are not accessible
from compute nodes, but can be accessed interactively on login
nodes. Historically the archive tier was tape-based, although recently
is was changed to disk. An object limit of 10,000 files/directories per
terabyte of space remains in place to preserve the option to move back
to tape in the future, should the service grow to a point where tape-based storage is more 
fiscally viable.

The archive feature list is similar to active, with the major differences
being: no direct access from RC compute, no SMB access, file/directory
count is limited, triple parity is used for data protection rather than
double parity, and a different compression algorithm is used. In summary, all archive allocations offer the following features:

 - interactive (NFS) access from RC login nodes
 - accessible using Globus/rsync/sftp via the data transfer node (DTN) hosts
 - 10,000 object (file/directory) per terabyte limit
 - triple parity (up to three simultaneous disk failures will not cause data loss)
 - snapshots (default schedule saves snapshots for one week)
 - full data checksumming, validated monthly (via zfs scrub)
 - zstd data compression

#### Active+archive

The PetaLibrary active+archive is a means of automatically replicating
your data across our active and archive PetaLibrary tiers. Rather than
purchase an active and archive allocation and synchronizing data between
the two, you can purchase the active+archive tier, and we will manage
the replication for you. With this type of allocation, you have full
access to the active tier only, and we manage replicating data to the
archive tier for you.

The biggest benefit of purchasing an active+archive allocation over
purchasing your own active and archive allocations is that a standalone
archive allocation is subject to the 10,000 object (file/directory)
limit. Since active allocations do not have an object limit, the archive
component of an active+archive allocation also does not have an object
limit.

Historically RC offered this service when the active and archive tiers
were using different underlying storage systems, which made it difficult
to do even daily replication. The service was not available to customers
for several years, but due to recent technical changes, we are able to
not only bring back the service, but are also able to replicate data
between the two tiers every fifteen minutes.

Note that the means of replication between the active and archive
tiers uses zfs snapshots. The replication process copies any snapshots
that exist on the active tier but do not exist on the archive tier,
and likewise removes any snapshots that exist on the archive tier but
are not present on the active tier. Therefore, if you ask us to prune
zfs snapshots aggressively on your active+archive allocation, this
reduces the snapshot count on both the active and the archive tier. The
active+archive tier is not an incremental backup, it is a time-delayed
mirror of your active allocation. Snapshots are the best way to preserve
your historical data in incremental steps, and replication is the best
way to ensure that a catastrophe does not destroy a single piece of
hardware that contains your data.
