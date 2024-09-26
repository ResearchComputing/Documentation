# Accessing the AWS Management Console

## Prerequisites

1. You are a member of CUBoulder with a valid [IdentiKey](https://oit.colorado.edu/services/identity-access-management/identikey). Federated access to LCA1 from other institutions is not currently supported.

2. The [DUO Multi-Factor Remote Access](https://oit.colorado.edu/services/identity-access-management/multi-factor-remote-access) (MFA) app is installed and enrolled. Visit OIT's [DUO Multi-Factor Remote Access](https://oit.colorado.edu/services/identity-access-management/multi-factor-remote-access) documentation to install and enroll MFA.

## Single Sign-On

Users access the [AWS Management Console](https://aws.colorado.edu) using their [CU IdentiKey](https://oit.colorado.edu/services/identity-access-management/identikey).
The Single Sign-On (SSO) URL is [https://aws.colorado.edu](https://aws.colorado.edu).
You can access your AWS Account from anywhere with internet access. You do not need to have a VPN connection to campus.

1. Launch the [AWS Management Console (SSO URL)](https://aws.colorado.edu).
2. Provide your [CU IdentiKey](https://oit.colorado.edu/services/identity-access-management/identikey) credentials.
    ```{image} images/aws-console-access/login.png
    :alt: CU FedAuth SSO login page with example user and password
    ```
3. Choose a method for authentication. We recommend you select "Send Me a Push". **NOTE:** You may not see the MFA step if you've recently authenticated and have an active session.
    ```{image} images/aws-console-access/mfa.png
    :alt: Duo MFA authentication method selection page with "Send Me a Push" circled in red
    ```
4. Accept the MFA request on your device.
5. You will be presented with a list of account names and numbers to which you have access. Click on the name of the desired account to expand the roles allocated to you. Click on the name of the desired role to log into the AWS console as that role. **Note:** Your access to the account selection page is valid for **8 hours**. Your access to any specific AWS account console is valid for **4 hours**.
    ```{image} images/aws-console-access/select-role.png
    :alt: AWS SSO account and role selection page
    ```
6. You will be logged in to the AWS Management Console. Always be sure to verify you have the AWS Region you are working with selected after logging in.
    ```{image} images/aws-console-access/select-region.png
    :alt: AWS Console home page with the region selection box circled in red
    ```

7. To log out from the AWS console for an account, click on your role name in the upper right corner and choose "Sign out". To log out from the AWS account selection page, click your username in the upper right corner of the access portal and choose "Sign out".
