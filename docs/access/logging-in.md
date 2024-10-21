# Logging In

## Getting a CURC account

All individuals who would like to access CU Research Computing (CURC) HPC systems (Alpine and Blanca) and storage solutions must have an associated CURC account. CURC systems are utilized by a variety of institutions including CU Boulder, Anschutz Medical Campus (AMC), Colorado State University (CSU), and institutions who are members of the Rocky Mountain Advanced Computing Consortium (RMACC). Given CURC systems host a variety of institutions, each institution has its own method for creating a CURC account. To simplify this process, below we provide tabs that specify instructions on getting a CURC account based on the institution you are affiliated with. 

`````{tabs}

````{tab} CU Boulder

The process for obtaining a CURC account for CU Boulder users is straightforward. Simply navigate to our [Account Request](https://rcamp.rc.colorado.edu/accounts/account-request/create/organization) page, select **"University of Colorado Boulder"**, fill out the provided information, and select **"Verify & Continue"**. Once the form has been completed and submitted, an automatic process will provision your account. Once you've received a CURC account, you will need to enroll in CU Boulder's Duo two-factor authentication service. After installing the Duo mobile app to your phone (available via Apple App Store or Google Play Store), visit [https://duo.colorado.edu](https://duo.colorado.edu) to enroll. 

```{important}
- Research Computing accounts are separate from your CU accounts. You must sign up for an individual Research Computing account if you wish to access Research Computing resources.
- Once your account is provisioned, please wait 15 minutes before signing in. 
```

````

````{tab} CSU

The process for obtaining a CURC account for CSU users is straightforward. Simply navigate to our [Account Request](https://rcamp.rc.colorado.edu/accounts/account-request/create/organization) page, select **"Colorado State University"**, fill out the provided information, and select **"Verify & Continue"**. Once the form has been completed and submitted, an automatic process will provision your account. Once you've received a CURC account, you will need to enroll in Duo two-factor authentication service. For more information on setting up Duo, please visit CSU's [Duo Two Factor Authentication](https://it.colostate.edu/duo-two-factor-authentication/) page. For additional information on using CURC resources as a CSU user, please consult [CSU's Getting Started with Alpine](https://it.colostate.edu/research-computing-and-cyberinfrastructure/compute/get-started-with-alpine/) documentation.  

```{important}
- Once your account is provisioned, please wait 15 minutes before signing in. 
```

````

````{tab} AMC

Currently, AMC users must go through various steps to create a CURC account. These steps are outlined below: 

1. If you do not already have an XSEDE/ACCESS account, follow the [instructions for new user registration](https://identity.access-ci.org/new-user). Please direct any questions about new accounts to the [ACCESS ticketing system](https://access-ci.atlassian.net/servicedesk/customer/portal/2/create/30).
2. Sign and fill out [CU Anschutz's Alpine form](https://ucdenverdata.formstack.com/forms/alpine_eua_and_intake)
3. You will receive an email from <hpcsupport@cuanschutz.edu> in approximately 1-2 weeks confirming your CURC account has been created.

```{important}
- For assistance filling out the Alpine form or updates on the account provisioning process, please email <hpcsupport@cuanschutz.edu>
- Once your account is provisioned, please wait 15 minutes before signing in. 
```

````

````{tab} RMACC

RMACC members can obtain a CURC account by completing the following steps

1. Create an [ACCESS-CI](https://access-ci.org/) account in the ACCESS user portal 
    ```{important} 
    If you already have an XSEDE or ACCESS account, please do not create another one and instead proceed to step 2.
    ```

2. Email CURC user support at <rc-help@colorado.edu> stating that you are requesting a CURC account. In this email, please include the following information:
    - your ACCESS or XSEDE username
    - your institutional affiliation (e.g., "University of Awesome")
    - your role (undergraduate graduate student, postdoc, staff, instructor, faculty or affiliated faculty)
    - your department
    - your first and last name
    - your preferred email address for communication

3. Wait for user support to respond to your email and provision your account

```{important}
- Once your account is provisioned, please wait 15 minutes before signing in. 
- The first time you log in you will be prompted to set up two-factor authentication.
```

````
`````

## Getting access to CURC resources 

Once you have obtained a CURC account, you can proceed to logging in to CURC resources. Users accessing CURC resources will be connected to a login node. A login node is an outward-facing node within the Research Computing environment that users can connect to from their local machines. Once on a login node, users can perform a limited number of tasks:

+ Edit files
+ Transfer data
+ Submit jobs
+ Access storage resources  

```{important}  
The [login node policy](../additional-resources/policies.md#login-nodes) states that login nodes should not be used for resource-intensive tasks such as running code. For all other tasks, users should run batch jobs, interactive jobs, or use the compile nodes. 
```

Similar to obtaining an account, the process of logging in to CURC resources can vary based on the institution you are affiliated with. In the tab sections below we provide details on how each institution can gain access to our login nodes.

`````{tabs}

````{tab} CU Boulder

The process for obtaining a CURC account for CU Boulder users 

````

````{tab} CSU

The process for obtaining a CURC account for CSU users 

+ **For CSU users, please refer to the "Remote Login" section of CSU's [Get Started with Alpine](https://it.colostate.edu/research-computing-and-cyberinfrastructure/compute/get-started-with-alpine/#) page.**  

````

````{tab} AMC

Currently, AMC users 

````

````{tab} RMACC

RMACC members can obtain 

+ **For RMACC users, please refer to [RMACC Access to Alpine.](rmacc.md)**

````
`````

### Terminal access for different operating systems

```{important}
Not all users have the ability to access CURC resources from their personal machine via a terminal. Please consult the appropriate tabbed item in the previous section [Getting access to CURC resources](#getting-access-to-curc-resources) before proceeding. 
```

`````{tabs}

````{tab} Windows 

Logging in from a Windows machine requires the additional step of [installing the PuTTY ssh client](https://www.putty.org/) onto your local machine. This application enables users to connect to remote servers with the ssh protocol. Note that there are other ssh clients that enable Windows machines to connect to remote ssh servers; Research Computing recommends PuTTY for reliability and simplicity.

1. Open the PuTTY application on your computer
    * Under “Host Name (or IP address)”, enter `login.rc.colorado.edu`. Select “SSH” as the connection type. Click on “Open”.
2. Enter your Identikey in response to the “login as” prompt
3. When prompted to enter your password:
    * If you are logging in using Duo Push, simply type your Identikey password. You will then receive an authentication request from the Duo app on your phone. Approve the request.
    * If you are using Duo SMS, Phone Call, or Token login methods, instructions can be on the [Duo 2 Factor Authorization](duo-2-factor-authentication.md) page.
    ```{note}
    As a security feature, PuTTY does not display any text while you type your password
    ```
````

````{tab} Mac

Logging in with a Mac requires no extra installation on your local machine. Simply utilize the terminal application that is pre-installed with your operating system to access Research Computing resources. 

1. Under “File”, open a new finder window. Navigate to the “Applications” folder, then the “Utilities” folder. Open a terminal window and type `ssh username@login.rc.colorado.edu`, where `username` is your assigned username. Press enter.
2. Enter your password:
    * If you are logging in using Duo Push, type your Identikey password.  You will then receive an authentication request on the Duo app on your phone. Approve the request.
    * If you are using Duo SMS, Phone Call, or Token login methods, instructions can be on the [Duo 2 Factor Authorization](duo-2-factor-authentication.md) page.
````

````{tab} Linux

Much like with Macs, Linux machines require no additional setup to access Research Computing resources. Simply utilize the your Linux terminal to access Research Computing resources. 

1. Open a terminal window from your application menu and type: `ssh username@login.rc.colorado.edu`, where `username` is your research computing username.

2. Enter your password:
    * If you are logging in using Duo Push, simply type your Identikey password. You will then receive an authentication request on the Duo app on your phone. Approve the request.
    * If you are using Duo SMS, Phone Call, or Token login methods, instructions can be on the [Duo 2 Factor Authorization](duo-2-factor-authentication.md) page.

````
`````

### SSH host keys

The first time you log into an RC login node you will be asked to verify the host key. You can refer to the keys published here to confirm that you are connecting to a valid RC login node.

```{note}
Each login node may support more than one type of key, but only one is used (or displayed) by your client at any given time.
```

#### login.rc.colorado.edu

```
# Fingerprint
# 256 SHA256:MB+601umlOc1sPXT4AXbV0rNRywUH4UlOIB9oJMuD8Q no comment (ECDSA)
ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBPfjz9VZAwSS0329z6RNZQDNrN3vU1YcthmBRqQAgxmDxBVPJzhazEzKqigoWuuQDHNzfm+05xTOYAmcnL3V7tc=
```

```
# Fingerprint
# 256 SHA256:uNn+9REKipRZ59VZQEKlBzB8xjOCe/9yII8uBgEFOGY no comment (ED25519)
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPub4h8XLU3dXJBNZljS4PdPWOORXoBdSdaKnwFcMTxe
```

```
# Fingerprint
# 2048 SHA256:xZ9xXWtJwBWYqm3ZSvqq2Q7Vq0qnhnImGfTyanytrEk no comment (RSA)
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDQWIqetVDUqKB2im3HyQZJ72PMYXFJUXR2Z+dzhGfOERABAV6m0fKcVcPrBjX9SYR4QYbxR+Yu2bIDDxpK+PZs2sAy/LU4po9mZUN8VAWBE0rwgcEvKfbQriwyhkdqdjEEzbEN5FTx05iYMN2o2vpshmi3dUpHaKMZPI0bhQKmwjM3bf77gpxXWNANsGIag0SdX4bmiWYQhR+CnzUJUis9DVOpVNfN+Jtw4IgnuJedehkZi/z/v7JKvV26jIxXmdq6+VkRCpoVnL3pJkoU5e4vaSc4V5kvgfI9G4tj6BEDGsRgHXAcZXk+hLtNp2nj2VsSocWcOVkn85obSfnVwV/f
```
