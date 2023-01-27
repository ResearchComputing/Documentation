## Accessing the AWS Management Console

### Prerequisite

The <a href="https://oit.colorado.edu/services/identity-access-management/multi-factor-remote-access" target="_blank">DUO Multi-Factor Remote Access</a> (MFA) app is installed and enrolled.
Visit OIT's <a href="https://oit.colorado.edu/services/identity-access-management/multi-factor-remote-access" target="_blank">DUO Multi-Factor Remote Access</a> documentation to install and enroll MFA.

### Single Sign-On

Users access the <a href="http://bit.ly/OIT-AWS" target="_blank">AWS Management Console</a> using their <a href="https://oit.colorado.edu/services/identity-access-management/identikey" target="_blank">CU IdentiKey</a>.
The Single Sign-On (SSO) URL is <a href="http://bit.ly/OIT-AWS" target="_blank">http://bit.ly/OIT-AWS </a>.
You can access your AWS Account from anywhere with internet access.  You do not need to have a VPN connection to campus.

1. Launch the <a href="http://bit.ly/OIT-AWS" target="_blank">AWS Management Console (SSO URL)</a>.
2. Provide your <a href="https://oit.colorado.edu/services/identity-access-management/identikey" target="_blank">CU IdentiKey</a> credentials.
![](images/aws-console-access/login.png)
3. Choose a method for authentication.  We recommend you select "Send Me a Push".  **NOTE:** You may not see the MFA step if you've recently authenticated and have an active session.
![](images/aws-console-access/mfa.png)
4. Accept the MFA request on your device.
5. If you only have access to a single AWS Account and a single Role, you will be logged straight in to the AWS Console.
If you have access to multiple AWS Accounts and/or Roles, you will be presented with a list of Accounts/Roles to select.  Select the Account and Role you wish to log in to.
![](images/aws-console-access/select-role.png)
6. You will be logged in to the AWS Management Console.  Always be sure to verify you have the AWS Region you are working with selected after logging in.
![](images/aws-console-access/select-region.png)
Once logged in, you have a 60 minute session.  You will be asked to log back in and re-authenticate using MFA when your session expires.

Couldn't find what you need? [Provide your feedback on these docs!](https://forms.gle/bSQEeFrdvyeQWPtW9)
