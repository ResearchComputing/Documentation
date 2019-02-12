## RMACC Access to Summit

If you are at an RMACC institution and would like to use Summit, please see the below steps to gain access.  


### Getting an XSEDE account

Visit the XSEDE User Portal and use the “Create Account” button. Complete the form and follow the instructions to create an XSEDE account. As part of the process, you will select an XSEDE username, which will be used to access the XSEDE User Portal and the XSEDE SSO Hub.

![XSEDE User Portal 1](https://raw.githubusercontent.com/ResearchComputing/Documentation/master/XSEDE/xsede1.png)  

![XSEDE User Portal 2](https://raw.githubusercontent.com/ResearchComputing/Documentation/master/XSEDE/xsede2.png)  

### Configuring Duo

Once your XSEDE account has been created, follow the Multi-Factor Authentication setup instructions on the XSEDE website. Multi-factor authentication with Duo is required for access to the XSEDE SSO Hub, which provides access to RMACC Summit.


### Getting authorization for RMACC Summit

Send an email from your institutional email address to rc-help@colorado.edu requesting access to RMACC Summit via XSEDE. Include the full name of your home institution, specific department within the institution, a short summary of why you require access to RMACC Summit, and your XSEDE username. You will receive a response indicating whether your account has been added to the rmacc-summit.colorado.xsede.org project.


### Logging in to CU Boulder RC using the XSEDE SSO Hub

Use an ssh client to connect to the XSEDE SSO Hub using your XSEDE credentials. You will be prompted to authenticate both using your XSEDE password and via Duo.

<!--![XSEDE Single sign on](https://github.com/ResearchComputing/Wiki_Documentation/blob/master/XSEDE/Screen%20Shot%202018-01-18%20at%209.49.55%20AM.png)-->

```
ssh -l <your-xsede-username> login.xsede.org
```

From there, use gsissh (available in the SSO Hub environment) to log into rmacc-summit, which serves as an alias for the CU Boulder RC login environment.

<!--![Summit Login node](https://github.com/ResearchComputing/Wiki_Documentation/blob/master/XSEDE/Screen%20Shot%202018-01-18%20at%209.54.13%20AM.png)-->

```
gsissh rmacc-summit
```
