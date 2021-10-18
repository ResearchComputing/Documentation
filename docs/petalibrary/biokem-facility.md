## BioKEM Facility

### Overview

If you are a BioKEM facility user, you can choose to have your data deposited directly into your PetaLibrary allocations. This process involves creating a biokem-deposit directory in your allocation's root directory and setting permissions to a biokem specific owner and group. The process is outlined below:

```
dir="/pl/active/${ALLOCATION}/biokem-deposit"
mkdir ${dir}
group=$( stat -c %G ${dir} )
chown biokem:${group} ${dir}
chmod o+x ${dir}
chmod 2770 ${dir}
```

If you would like to have a biokem-deposit directory added to your PetaLibrary allocation please have the allocation owner contact <rc-help@colorado.edu>. The recommended allocation size is 15 to 20 TB per active EM project that will be using the PetaLibrary allocation. 
