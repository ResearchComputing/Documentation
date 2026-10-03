# LCA0

This page describes how to access your CU Boulder AWS environment through the AWS Management Console and AWS CLI.

## Accessing the AWS Management Console

### Prerequisites

1. If you are a member of CU Boulder, you will be using your CU Identikey. If you are from another institution but have access to CU Boulder AWS resources, sign in using your institution's credentials.

2. If you are a member of another CU campus:

    a. **CU Anschutz users**: To get your account synced to the Boulder Entra tenant, send a ticket to the [CU Anschutz OIT Service Desk](https://www.ucdenver.edu/offices/office-of-information-technology/get-help) and request access to Boulder's AWS instance. As part of this process, you'll need to set up Microsoft MFA, so have your mobile phone number ready.

    b. **CU System (UIS) users**: To access campus cloud content/resources such as AWS, Microsoft 365 (Teams, SharePoint, Azure), please email [help@cu.edu](mailto:help@cu.edu) and provide the following:

    * Which campus do you need access to?
    * Which resources are you trying to access?
    * Indicate your justification for access to these resources.

    c. [UCCS HaloITSM Knowledge Base Portal](https://uccs.haloitsm.com/portal/anonymouskb?&key=f9709e6e-0c9f-4a83-94a1-b0e61d525d66&token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYklkIjoiMjg1ZDA2ZjUtMjcyZS00MWM1LWJjZDgtOWI5OTI5M2NlOTcxIiwicElkIjoiMjQ1IiwiaWQiOiJmOTcwOWU2ZS0wYzlmLTRhODMtOTRhMS1iMGU2MWQ1MjVkNjYiLCJuYmYiOjE3ODQzMDg5MTMsImV4cCI6MTMwNjMzMzI3NzMzLCJpYXQiOjE3ODQzMDg5MTN9.zTs2Vr2ZBTEv1hhVnwM4LE5K9Ea-BUpIPkX8nxQincM)

3. The [Microsoft authenticator App](https://oit.colorado.edu/tutorial/microsoft-365-multi-factor-authentication-register-and-set-microsoft-authenticator-app) (MFA) app is installed and enrolled.
Visit OIT's [Microsoft 365 Multi-Factor Authentication](https://oit.colorado.edu/services/identity-access-management/microsoft-multi-factor-authentication) documentation to install and enroll MFA.


### Single Sign-On

Users access the [AWS Management Console](https://aws-classic.colorado.edu) using their university login credentials (like [CU IdentiKey](https://oit.colorado.edu/services/identity-access-management/identikey) for CU Boulder) in Microsoft Entra.
The Single Sign-On (SSO) URL is [https://aws-classic.colorado.edu](https://aws-classic.colorado.edu).
You can access your AWS Account from anywhere with internet access.  You do not need to have a VPN connection to campus.

1. Launch the [AWS Management Console (SSO URL)](https://aws-classic.colorado.edu).
2. Provide your university login credentials (like your [CU IdentiKey](https://oit.colorado.edu/services/identity-access-management/identikey) for CU Boulder) when directed to Microsoft Entra.
    ```{image} lca0_images/aws-console-access/login.png
        :alt: CU single sign-on login page for accessing the AWS Management Console. Described under Single Sign-On.
        :align: center
    ```
3. Choose a method for authentication.  We recommend you select "Send Me a Push".  **NOTE:** You may not see the MFA step if you've recently authenticated and have an active session.
4. Accept the MFA request on your device.
5. You will be presented with a list of account names and numbers to which you have access. Click on the name of the desired account to expand the roles allocated to you.  Select the Account and Role you wish to log in to.
    ```{image} lca0_images/aws-console-access/select-role.png
        :alt: AWS access portal listing accounts and roles that can be selected after sign-in. Described under Single Sign-On.
        :align: center
    ```
6. You will be logged in to the AWS Management Console.  Always be sure to verify you have the AWS Region you are working with selected after logging in.
Once logged in, you have a 4 hour session.  When your session expires, return to the access portal to refresh your credentials.

## Accessing the AWS CLI

AWS CLI temporary credentials are valid for **4 hours** and can be established through any of the methods outlined below.

**Note:** The `$` in the examples below indicates your prompt. Do not type it as input.

### Prerequisites
* The [AWS CLI tools](https://aws.amazon.com/cli/) is installed. Please refer to the [AWS CLI installation documentation](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) for instructions.

* If you are a member of another CU campus:

    * **CU Anschutz users**: To get your account synced to the Boulder Entra tenant, send a ticket to the [CU Anschutz OIT Service Desk](https://www.ucdenver.edu/offices/office-of-information-technology/get-help) and request access to Boulder's AWS instance. As part of this process, you'll need to set up Microsoft MFA, so have your mobile phone number ready.

    * **CU System (UIS) users**: To access campus cloud content/resources such as AWS, Microsoft 365 (Teams, SharePoint, Azure), please email [help@cu.edu](mailto:help@cu.edu) and provide the following:

        * Which campus do you need access to?
        * Which resources are you trying to access?
        * Indicate your justification for access to these resources.

    * [UCCS HaloITSM Knowledge Base Portal](https://uccs.haloitsm.com/portal/anonymouskb?&key=f9709e6e-0c9f-4a83-94a1-b0e61d525d66&token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYklkIjoiMjg1ZDA2ZjUtMjcyZS00MWM1LWJjZDgtOWI5OTI5M2NlOTcxIiwicElkIjoiMjQ1IiwiaWQiOiJmOTcwOWU2ZS0wYzlmLTRhODMtOTRhMS1iMGU2MWQ1MjVkNjYiLCJuYmYiOjE3ODQzMDg5MTMsImV4cCI6MTMwNjMzMzI3NzMzLCJpYXQiOjE3ODQzMDg5MTN9.zTs2Vr2ZBTEv1hhVnwM4LE5K9Ea-BUpIPkX8nxQincM)

* The [Microsoft authenticator App](https://oit.colorado.edu/tutorial/microsoft-365-multi-factor-authentication-register-and-set-microsoft-authenticator-app) (MFA) app is installed and enrolled.
Visit OIT's [Microsoft 365 Multi-Factor Authentication](https://oit.colorado.edu/services/identity-access-management/microsoft-multi-factor-authentication) documentation to install and enroll MFA.

### Option 1: Environment variables from the web browser

This option is recommended when you have a quick task to do from a single shell.

1. Log in to the [AWS Management Console (SSO URL)](https://aws-classic.colorado.edu) using steps 1-4 from [Single Sign-On](#single-sign-on).
2. You will be presented with a list of account names and numbers to which you have access. Click on the name of the desired account to expand the roles allocated to you. Click on "Access Keys" next to the name of the desired role.
    ```{image} lca0_images/aws-cli-access/select-access-keys.png
    :alt: AWS SSO account and role selection page with "Access Keys" circled in red. Described under Option 1: Environment variables from the web browser.
    :align: center
    ```
3. You will be presented with multiple options for acquiring access keys for the CLI. Click on the tab that matches your operating system (OS).
    ```{image} lca0_images/aws-cli-access/browser-cli-os-selection.png
    :alt: AWS CLI credentials access page with "macOS and Linux" circled in red. Described under Option 1: Environment variables from the web browser.
    :align: center
    ```
4. Expand the section named "Option 1: Set AWS environment variables" and click on the overlapping squares icon to copy the environment variable commands that contain your credentials. The exact commands displayed will vary by OS and shell.
5. In a terminal on your local machine, paste in the environment variable commands that you just copied and hit Enter. If you require authentication in multiple shell sessions, you'll need to paste the same keys in each one.
    ```bash
    $ export AWS_ACCESS_KEY_ID="AAAAAAAAAAAAAAAAAAAA"
    export AWS_SECRET_ACCESS_KEY="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    export AWS_SESSION_TOKEN="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    $
    ```
6. Your session in the window where you pasted the credentials (only) is now authorized for AWS from the CLI. Confirm your access by querying your AWS identity.
    ```bash
    $ aws --no-cli-pager sts get-caller-identity
    {
        "UserId": "AAAAAAAAAAAAAAAAAAAAA:ralphie@colorado.edu",
        "Account": "111111111111",
        "Arn": "arn:aws:sts::111111111111:assumed-role/AWSReservedSSO_MyRole_aaaaaaaaaaaaaaaa/ralphie@colorado.edu"
    }
    ```
7. You can now use AWS CLI commands and libraries that auto-detect credentials (like [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)) in this shell session. To log out, just exit the shell session.

### Option 2: Configuration file from the web browser

This option is recommended when you want to use multiple shell sessions to access a single AWS account.

1. Log in to the [AWS Management Console (SSO URL)](https://aws-classic.colorado.edu) using steps 1-4 from [Single Sign-On](#single-sign-on).
2. You will be presented with a list of account names and numbers to which you have access. Click on the name of the desired account to expand the roles allocated to you. Click on "Access Keys" next to the name of the desired role.
    ```{image} lca0_images/aws-cli-access/select-access-keys.png
    :alt: AWS SSO account and role selection page with "Access Keys" circled in red. Described under Option 2: Configuration file from the web browser.
    :align: center
    ```
3. You will be presented with multiple options for acquiring access keys for the CLI. Click on the tab that matches your operating system (OS).
    ```{image} lca0_images/aws-cli-access/browser-cli-os-selection.png
    :alt: AWS CLI credentials access page with "macOS and Linux" circled in red. Described under Option 2: Configuration file from the web browser.
    :align: center
    ```
4. Expand the section named "Option 2: Add a profile to your AWS credentials file" and click on the overlapping squares icon to copy the configuration block that contain your credentials.
    ```{image} lca0_images/aws-cli-access/browser-cli-option2.png
    :alt: AWS CLI credentials access page with the copy icon circled in red next to a list of configuration lines that contain the current credentials and profile name. Described under Option 2: Configuration file from the web browser.
    :align: center
    ```
5. Append the credential block you copied in the previous step to your AWS credentials file. This file is located at `~/.aws/credentials` (for macOS and Linux) or `%USERPROFILE%\.aws\credentials` (for Windows). It's okay if other configuration is already present in this file.
    ```bash
    $ cat ~/.aws/credentials
    [111111111111_MyRole]
    aws_access_key_id=AAAAAAAAAAAAAAAAAAAA
    aws_secret_access_key=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    aws_session_token=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    ```
6. While these credentials can be used from any shell window, you'll need to specify the profile name to select them. You can do this by setting the environment variable `AWS_PROFILE` to the profile name or passing it on the command line.  Confirm your access by querying your AWS identity.

    For macOS and Linux:
    ```bash
    $ export AWS_PROFILE=111111111111_MyRole
    $ aws --no-cli-pager sts get-caller-identity
    {
        "UserId": "AAAAAAAAAAAAAAAAAAAAA:ralphie@colorado.edu",
        "Account": "111111111111",
        "Arn": "arn:aws:sts::111111111111:assumed-role/AWSReservedSSO_MyRole_aaaaaaaaaaaaaaaa/ralphie@colorado.edu"
    }
    ```
    OR for Windows PowerShell:
    ```pwsh
    $ $Env:AWS_PROFILE="111111111111_MyRole"
    $ aws --no-cli-pager sts get-caller-identity
    {
        "UserId": "AAAAAAAAAAAAAAAAAAAAA:ralphie@colorado.edu",
        "Account": "111111111111",
        "Arn": "arn:aws:sts::111111111111:assumed-role/AWSReservedSSO_MyRole_aaaaaaaaaaaaaaaa/ralphie@colorado.edu"
    }
    ```
    OR for macOS, Linux, and Windows:
    ```bash
    $ aws --no-cli-pager --profile 111111111111_MyRole sts get-caller-identity
    {
        "UserId": "AAAAAAAAAAAAAAAAAAAAA:ralphie@colorado.edu",
        "Account": "111111111111",
        "Arn": "arn:aws:sts::111111111111:assumed-role/AWSReservedSSO_MyRole_aaaaaaaaaaaaaaaa/ralphie@colorado.edu"
    }
    ```
7. You are now authenticated for the AWS CLI. To log out, delete the lines you added from `~/.aws/credentials`.

### Option 3: CLI SSO Integration

This option is recommended when you want to use multiple shell sessions to access multiple AWS accounts or want to refresh credentials after the timeout period from the command line. For more information, please see the [official AWS SSO CLI documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html).

1. Configure CLI SSO settings. Append the following to your AWS CLI configuration file. This file is located at `~/.aws/config` (for macOS and Linux) or `%USERPROFILE%\.aws\config` (for Windows). You only have to do this once.
    ```ini
    [sso-session entra]
    sso_start_url = https://ucboit.awsapps.com/start
    sso_region = us-west-2
    sso_registration_scopes = sso:account:access
    ```
2. Create a profile for each AWS account you want to configure in your `~/.aws/config` file. You can find appropriate account numbers and role names at the AWS access portal that you use when [logging in via a web browser](#accessing-the-aws-management-console). Append an entry for each account as shown below. You only have to do this once.
    ```ini
    [profile awsucob0myaccount]
    sso_session = entra
    sso_account_id = 111111111111
    sso_role_name = MyRole
    region = us-west-2
    output = json

    [profile awsucob0myotheraccount]
    sso_session = entra
    sso_account_id = 222222222222
    sso_role_name = MyOtherRole
    region = us-west-2
    output = json
    ```
3. Log into SSO.
    ```bash
    $ aws sso login --sso-session entra
    Attempting to automatically open the SSO authorization page in your default browser.
    If the browser does not open or you wish to use a different device to authorize this request, open the following URL:

    https://device.sso.us-west-2.amazonaws.com/

    Then enter the code:

    ABCD-1234
    ```
    You will be prompted to log in via your default browser. Follow the [same flow as used when accessing the AWS console](#accessing-the-aws-management-console). After authentication, you will be prompted to allow CLI access to your session. Enter the code ("ABCD-1234" in this example) and press "Submit and continue".
    ```{image} lca0_images/aws-cli-access/authorize-request.png
    :alt: AWS CLI authorization request web form with example credentials shown. Described under Option 3: CLI SSO Integration.
    :align: center
    ```
    On the following page that says "Allow botocore-client-entra to access your data?", click "Allow access".
    ```{image} lca0_images/aws-cli-access/allow-botocore.png
    :alt: AWS CLI botocore authorization prompt. Described under Option 3: CLI SSO Integration.
    :align: center
    ```
    You will be taken to a success page. 
    ```{image} lca0_images/aws-cli-access/request-approved.png
    :alt: AWS CLI authorization approved success page. Described under Option 3: CLI SSO Integration.
    :align: center
    ```
    You can now close this page in your browser and return to the terminal. The terminal should say:
    ```bash
    Successfully logged into Start URL: https://aws-classic.colorado.edu
    ```
4. Confirm your access by querying your AWS identity. Per-account credentials will be automatically refreshed when needed until the 8-hour SSO session expires.

    For macOS and Linux:
    ```bash
    $ export AWS_PROFILE=awsucob0myaccount
    $ aws --no-cli-pager sts get-caller-identity
    {
        "UserId": "AAAAAAAAAAAAAAAAAAAAA:ralphie@colorado.edu",
        "Account": "111111111111",
        "Arn": "arn:aws:sts::111111111111:assumed-role/AWSReservedSSO_MyRole_aaaaaaaaaaaaaaaa/ralphie@colorado.edu"
    }
    ```
    OR for Windows PowerShell:
    ```pwsh
    $ $Env:AWS_PROFILE="awsucob0myaccount"
    $ aws --no-cli-pager sts get-caller-identity
    {
        "UserId": "AAAAAAAAAAAAAAAAAAAAA:ralphie@colorado.edu",
        "Account": "111111111111",
        "Arn": "arn:aws:sts::111111111111:assumed-role/AWSReservedSSO_MyRole_aaaaaaaaaaaaaaaa/ralphie@colorado.edu"
    }
    ```
    OR for macOS, Linux, and Windows:
    ```bash
    $ aws --no-cli-pager --profile awsucob0myaccount sts get-caller-identity
    {
        "UserId": "AAAAAAAAAAAAAAAAAAAAA:ralphie@colorado.edu",
        "Account": "111111111111",
        "Arn": "arn:aws:sts::111111111111:assumed-role/AWSReservedSSO_MyRole_aaaaaaaaaaaaaaaa/ralphie@colorado.edu"
    }
    ```
5. (Optional) To switch accounts, just use another profile name. You do not have to re-authenticate.
    ```bash
    $ aws --no-cli-pager --profile awsucob0myotheraccount sts get-caller-identity
    {
        "UserId": "AAAAAAAAAAAAAAAAAAAAA:ralphie@colorado.edu",
        "Account": "222222222222",
        "Arn": "arn:aws:sts::222222222222:assumed-role/AWSReservedSSO_MyRole_aaaaaaaaaaaaaaaa/ralphie@colorado.edu"
    }
    ```
6. When done, log out from SSO and all accounts with:
    ```bash
    aws sso logout
    ```


## What should I read next?

```{toctree}
:maxdepth: 1
faq/faq
```
```{toctree}
:maxdepth: 1
managing-customer-groups
```
```{toctree}
:maxdepth: 1
customer-permission-boundary
```
```{toctree}
:maxdepth: 1
customer-support
```
```{toctree}
:maxdepth: 1
billing/index
```
```{toctree}
:maxdepth: 1
troubleshooting/troubleshooting
```
```{toctree}
:maxdepth: 1
load-balancer/load-balancer
```
```{toctree}
:maxdepth: 1
AWS-Programs-for-Research-and-Education
```