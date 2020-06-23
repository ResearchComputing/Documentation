## Transferring data to CURC without a password (_command line only_)

_Note: you must be logged in to [campus VPN](https://oit.colorado.edu/services/network-internet-services/vpn) to do a passwordless data transfer to CURC_

### Generate an ssh keypair on your local laptop/desktop

You only need to perform this step once. From a local terminal run:

```
ssh-keygen -t ed25519
``` 

This will create `~/.ssh/id_ed25519` and `~/.ssh/id_ed25519.pub` on your local machine (_note: the "~" denotes your home directory_). 

### Copy the public key to ~/.ssh/authorized_keys on a CURC login node 

You only need to perform this step once. From a local terminal run:

```
cat ~/.ssh/id_ed25519.pub | ssh ralphie@login.rc.colorado.edu -T "cat >> ~/.ssh/authorized_keys"
```
...where you should substitute your CURC username for "ralphie"; you will be required to enter your password and accept a Duo push in order to transfer the key.

_Note: If you have trouble running the command above, you can also just login to a CURC login node, open `~/.ssh/authorized_keys` and paste the text from `~/.ssh/id_ed25519.pub` that resides on your local machine._

### Use `rsync` or `scp` to transfer files without a password

Now you are ready to transfer files.  Make sure you are logged on campus or logged into CU VPN. Examples:

User "ralphie" employs _rsync_ to tranfer `myfile.txt` to `/projects/ralphie` on CURC:

```
rsync -av ./myfile.txt dtn-new-data.rc.int.colorado.edu:/projects/ralphie/myfile.txt
```

User "ralphie" employs _scp_ to transfer `myfile.txt` from Ralphie's local machine to a PetaLibrary allocation called "crdds" that Ralphie has access to:

```
scp ./myfile.txt dtn-new-data.rc.int.colorado.edu:/pl/active/crdds/myfile.txt
```
