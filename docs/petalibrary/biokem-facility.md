## BioKEM Facility

### Overview

BioKEM facitlity users can choose to have their data deposited directly into their PetaLibrary allocations. This process involves creating a biokem-deposit directory in your allocation's root directory and setting permissions to a biokem specific owner and group. The process is outlined below for the for full transparency.

```
dir="/pl/active/${ALLOCATION}/biokem-deposit"
mkdir ${dir}
group=$( stat -c %G ${dir} )
chown biokem:${group} ${dir}
chmod o+x ${dir}
chmod 2770 ${dir}
```

If you would like to have a biokem-deposit directory added to your PetaLibrary allocation please have the allocation owner contact rc-help@colorado.edu with the name of the allocation.
