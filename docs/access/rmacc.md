# RMACC Access to Alpine 

```{note} 
As of September 1, 2022, Rocky Mountain Advanced Computing Consortium (RMACC) members are unable to use the XSEDE SSO Hub to log in to CURC systems. Users will instead use Open OnDemand to access RMACC resources.
```


## Requesting an RMACC Account on CURC Resources

**Step 1:** Create an [ACCESS-CI](https://access-ci.org/) account in the ACCESS user portal 

```{important} 
If you already have an XSEDE or ACCESS account, please do not create another one -- just go to step 2.
```

<br>

**Step 2:** Email us at <rc-help@colorado.edu>, and request an account. Please include the following information:

- your ACCESS or XSEDE username
- your institutional affiliation (e.g., "University of Awesome")
- your role (undergraduate graduate student, postdoc, staff, instructor, faculty or affiliated faculty)
- your department
- your first and last name
- your preferred email address for communication

<br>

**Step 3:** Our team will provision your account and we will follow up with a confirmation email. 

<br>

**Step 4:** Login to the [RMACC OnDemand](#logging-into-open-ondemand) portal to access CURC resources!

```{important}
The first time you log in you will be prompted to set up two-factor authentication.
```
 
## Logging into Open OnDemand

- Visit [https://ondemand-rmacc.rc.colorado.edu](https://ondemand-rmacc.rc.colorado.edu).
You will be redirected to CILogon.

![](rmacc/cilogon.png)

- Select "ACCESS CI" from the list of identity providers then "Log On". This will redirect you to the ACCESS login page. 
 
![](rmacc/access_cilogon.png)

- Enter your ACCESS/XSEDE username and password.
- Select "Login", then accept the Duo push notification from your device to be directed to the RMACC Open OnDemand homepage.

![](rmacc/ood_homepage.png)

<br>


## Shell Access to Compute Nodes  

- Currently, the suggested method for obtaining shell access for RMACC users is to use the Open OnDemand [shell access application](../open_ondemand/terminal_app.md).
- If desired, a shell can also be accessed via Jupyter sessions by opening up a "Terminal" within the Jupyter session. 

<br>

## Other Features and Tools

Additional features and tools in RMACC Open OnDemand are under active development. Please see [CURC Open OnDemand documentation](../open_ondemand/index.md) for information about the latest features of Open OnDemand. 


## Globus Data Transfers

Globus data transfers are supported for RMACC users who have current XSEDE.org or future access-ci.org credentials.  

The Globus Collection for CURC resources is available at "CU Boulder Research Computing" and will require login with credentials from one of those providers.

Once connected Globus can be used to transfer data to:  

- `/home`
- `/projects`
- `/pl`

```{warning} 
  - `scp` is currently unavailable to RMACC users.
  - File transfer using Open OnDemand's _Files_ menu is limited to < 10 GB per file.
```

<br>

