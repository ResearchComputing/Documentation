# PetaLibrary and data redundancy 

A PetaLibrary `active` or `archive` allocation is a single copy of your data that is not backed up. You may be familiar with the 3-2-1 backup strategy, which recommends having three copies of your data, using two different types of media, and having one copy at a different location. An active or archive PetaLibrary allocation is a **single** copy of your data on one type of media in a single location, so PetaLibrary can be a component of a good backup strategy, but for data that cannot be replaced, an active or archive PetaLibrary should not be the only copy. 

PetaLibrary does have some forms of redundancy, such as RAID (whereby your copy of data is written to multiple disks on our system) to minimize service outages caused by disk failures, and snapshots which can be useful if files are accidentally damaged or removed. Neither RAID nor snapshots are an effective backup strategy to protect against other causes of data loss such as hardware and software failures, or user and administrative errors. The only way to mitigate the risk to your data is to not rely on a single active or archive PetaLibrary allocation to be the sole copy. 

## Options for backing up your data

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


