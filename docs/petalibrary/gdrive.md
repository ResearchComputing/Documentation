### Copy data from Google Drive to PetaLibrary

#### Step 1: download/install rclone and make sure you can run it

* Download the latest version from https://rclone.org/downloads/ and install per the developer's documentation.
* To test, run `rclone --version` at your prompt; if the software is installed a version number will be reported back to you, similar to:

```
$ rclone --version
rclone v1.54.1-DEV
- os/arch: freebsd/amd64
- go version: go1.16.2
```

#### Step 2: configure google drive remote configuration

_Note: the steps below are also outlined in the [Rclone Documentation for Google Drive](https://rclone.org/drive/). We only list the critical steps. If a step is left out, assume you can select the default setting._

* Type `rclone config` to create a new profile for transferring files between Google Drive and PetaLibrary
* When prompted for whether to configure a “new” or “existing” profile type `n` for "new remote"
* When prompted to name the new profile provide any descriptive name you like (e.g., `gdrive_johndoe_cu`)
* When prompted for the type of storage to configure, select the number of the option for "Google Drive" (e.g., the number is "15" for _rclone_ v1.54.1)
* When prompted for scope that rclone should use when requesting access from Drive enter '1' for full drive access
* When prompted for "Use Auto config?” choose "Y" for yes (default). Now _rclone_ will give you a URL to use to authenticate against. It may automatically open this URL in your browser.  If it does not, you can paste the URL into your browser if you are configuring on a local machine. If you are working on a remote system (e.g., if you are logged into your lab server from home), then from a terminal you can `ssh` from your computer to the system where you are configuring rclone:

   ```bash
   $ port=53682
   $ ssh -L ${port}:localhost:${port} <machine where rclone is running>
   ```
   
   ...and now entering the url in your local browser should work.

* Once you are in your browser, you may be asked to authenticate to your Google account, and then you will be asked to allow Rclone to access the files in your `gdrive`. Complete this step to grant access.  If successful you'll receive a "success" message. 
* When prompted for whether you want to configure this as a Shared Drive (Team Drive). Choose the appropriate answer; if this is your personal Drive account then choose `no` (default)
* Finally, you will be prompted to review the configuration and confirm whether it is okay. If everything looks okay, choose `yes` (default)
* Now type `q` to quit the configuration. 

##### Now test your Google Drive remote!

On your local machine type:
```bash
$ rclone ls gdrive_johndoe_cu
```
If this step fails, your Google Drive remote is not configured properly. Try reconfiguring your Google Drive remote again or contact rc-help@colorado.edu for assistance.

#### Step 3: Create your PetaLibrary remote configuration

See instructions for creating an [Rclone remote configuration for PetaLibrary](https://curc.readthedocs.io/en/latest/petalibrary/rclone.html#configure-rclone)


* [Rclone documentation](https://rclone.org/)
* [CURC data transfer documentation](https://curc.readthedocs.io/en/latest/compute/data-transfer.html)
