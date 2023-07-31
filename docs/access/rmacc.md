# RMACC Access to Alpine 

_Note to existing account holders: As of September 1, 2022, Rocky Mountain Advanced Computing Consortium (RMACC) members are 
unable to use the XSEDE SSO Hub to log in to CURC systems. Users will instead use Open OnDemand to access RMACC resources._


### Requesting an RMACC Account on CURC Resources

Step 1: Create an [ACCESS-CI](https://access-ci.org/) account in the ACCESS user portal [Note: If you already have an XSEDE or ACCESS account, please do not create another 
one -- just go to step 2].

<br>

Step 2: Email us at <rc-help@colorado.edu>, and request an account. Please include the following information:

- your ACCESS or XSEDE username
- your institutional affiliation (e.g., "University of Awesome")
- your role (undergraduate graduate student, postdoc, staff, instructor, faculty or affiliated faculty)
- your department
- your first and last name
- your preferred email address for communication

<br>

Step 3: Our team will provision your account and we  will follow up with a confirmation email 

<br>

Step 4: Login to the [RMACC OnDemand](https://curc.readthedocs.io/en/latest/access/rmacc.html#logging-in-to-open-ondemand) portal to access CURC 
resources! The first time you login you will be prompted to set up two-factor authentication.
 
## Logging in to Open OnDemand

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

- Currently, the suggested method for obtaining shell access for RMACC users is to use the Open OnDemand [shell access application](../gateways/OnDemand.html#clusters-shell-access).
- RMACC users may also obtain ssh access into `login-ci.rc.colorado.edu` by requesting it via <rc-help@colorado.edu>. Please note that this form of access is currently on a trial basis.
- If desired, a shell can also be accessed via Jupyter sessions by opening up a "Terminal" within the Jupyter session. 

<br>

## Other Features and Tools

Additional features and tools in RMACC Open OnDemand are under active development. Please see [CURC Open OnDemand documentation](https://curc.readthedocs.io/en/latest/gateways/OnDemand.html?highlight=Open%20OnDemand#jobs) for information about monitoring, creating, and editing jobs using the _Jobs_
menu. 


### Globus Data Transfers

Globus data transfers are supported for RMACC users who have current XSEDE.org or future access-ci.org credentials.  

The Globus Collection for CURC resources is available at "CU Boulder Research Computing ACCESS" and will require login with credentials from one of those providers.

Once connected Globus can be used to transfer data to:

<br>

- `/home`
- `/projects`
- `/pl`


**_Notes on data transfer_**:
  - `scp` is currently unavailable to RMACC users
  - File transfer using Open OnDemand's _Files_ menu is  limited to < 10 GB per file


<br>

Couldn’t find what you need? [Provide feedback on these docs!](https://docs.google.com/forms/d/e/1FAIpQLSeaoraGl8x_ubyGNEYe3WP2cw_wg6aZM7Dy0v4X5s2ND-06RA/viewform)
