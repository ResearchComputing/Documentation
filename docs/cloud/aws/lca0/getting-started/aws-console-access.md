# Accessing the AWS Management Console

## Prerequisites
1. If you are a member of CU Boulder, you will be using your CU Identikey. If you are from another institution but have access to CU Boulder AWS resources, sign in using your institution's credentials.

2. CU Anchutz users: to get your account synced to the Boulder Entra tenant, send a ticket to the [CU Anschutz OIT Service Desk](https://www.ucdenver.edu/offices/office-of-information-technology/get-help) and request access to Boulder's AWS instance. As part of this process, you'll need to set up Microsoft MFA, so have your mobile phone number ready.

2. The [Microsoft authenticator App](https://oit.colorado.edu/tutorial/microsoft-365-multi-factor-authentication-register-and-set-microsoft-authenticator-app) (MFA) app is installed and enrolled.
Visit OIT's [Microsoft 365 Multi-Factor Authentication](https://oit.colorado.edu/services/identity-access-management/microsoft-multi-factor-authentication) documentation to install and enroll MFA.

## Single Sign-On

Users access the [AWS Management Console](https://aws-classic.colorado.edu) using their university login credentials (like [CU IdentiKey](https://oit.colorado.edu/services/identity-access-management/identikey) for CU Boulder) in Microsoft Entra.
The Single Sign-On (SSO) URL is [https://aws-classic.colorado.edu](https://aws-classic.colorado.edu).
You can access your AWS Account from anywhere with internet access.  You do not need to have a VPN connection to campus.

1. Launch the [AWS Management Console (SSO URL)](https://aws-classic.colorado.edu).
2. Provide your university login credentials (like your [CU IdentiKey](https://oit.colorado.edu/services/identity-access-management/identikey) for CU Boulder) when directed to Microsoft Entra.
    ```{image} images/aws-console-access/login.png
        :alt: CU SSO login page
    ```
3. Choose a method for authentication.  We recommend you select "Send Me a Push".  **NOTE:** You may not see the MFA step if you've recently authenticated and have an active session.
4. Accept the MFA request on your device.
5. You will be presented with a list of account names and numbers to which you have access. Click on the name of the desired account to expand the roles allocated to you.  Select the Account and Role you wish to log in to.
    ```{image} images/aws-console-access/select-role.png
        :alt: AWS SSO account and role selection page
    ```
6. You will be logged in to the AWS Management Console.  Always be sure to verify you have the AWS Region you are working with selected after logging in.
Once logged in, you have a 4 hour session.  When your session expires, return to the access portal to refresh your credentials.
