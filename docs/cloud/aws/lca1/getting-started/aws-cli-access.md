# Accessing the AWS CLI

AWS CLI temporary credentials are valid for **4 hours** and can be established through any of the methods outlined below.

**Note:** The `$` in the examples below indicates your prompt. Do not type it as input.

## Prerequisites

* The [AWS CLI tools](https://aws.amazon.com/cli/) is installed. Please refer to the [AWS CLI installation documentation](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) for instructions.

* The [DUO Multi-Factor Remote Access](https://oit.colorado.edu/services/identity-access-management/multi-factor-remote-access) (MFA) app is installed and enrolled. Visit OIT's [DUO Multi-Factor Remote Access](https://oit.colorado.edu/services/identity-access-management/multi-factor-remote-access) documentation to install and enroll MFA.

## Option 1: Environment variables from the web browser

This option is recommended when you have a quick task to do from a single shell.

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
5. You will be presented with a list of account names and numbers to which you have access. Click on the name of the desired account to expand the roles allocated to you. Click on "Access Keys" next to the name of the desired role.
    ```{image} images/aws-cli-access/select-access-keys.png
    :alt: AWS SSO account and role selection page with "Access Keys" circled in red
    ```
6. You will be presented with multiple options for acquiring access keys for the CLI. Click on the tab that matches your operating system (OS).
    ```{image} images/aws-cli-access/browser-cli-os-selection.png
    :alt: AWS CLI credentials access page with "macOS and Linux" circled in red
    ```
7. Expand the section named "Option 1: Set AWS environment variables" and click on the overlapping squares icon to copy the environment variable commands that contain your credentials. The exact commands displayed will vary by OS and shell.
    ```{image} images/aws-cli-access/browser-cli-option1.png
    :alt: AWS CLI credentials access page with the copy icon circled in red next to a list of environment variable commands
    ```
8. In a terminal on your local machine, paste in the environment variable commands that you just copied and hit Enter. If you require authentication in multiple shell sessions, you'll need to paste the same keys in each one.
    ```bash
    $ export AWS_ACCESS_KEY_ID="AAAAAAAAAAAAAAAAAAAA"
    export AWS_SECRET_ACCESS_KEY="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    export AWS_SESSION_TOKEN="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    $
    ```
9. Your session in the window where you pasted the credentials (only) is now authorized for AWS from the CLI. Confirm your access by querying your AWS identity.
    ```bash
    $ aws --no-cli-pager sts get-caller-identity
    {
        "UserId": "AAAAAAAAAAAAAAAAAAAAA:ralphie@colorado.edu",
        "Account": "111111111111",
        "Arn": "arn:aws:sts::111111111111:assumed-role/AWSReservedSSO_MyRole_aaaaaaaaaaaaaaaa/ralphie@colorado.edu"
    }
    ```
10. You can now use AWS CLI commands and libraries that auto-detect credentials (like [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)) in this shell session. To log out, just exit the shell session.

## Option 2: Configuration file from the web browser

This option is recommended when you want to use multiple shell sessions to access a single AWS account.

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
5. You will be presented with a list of account names and numbers to which you have access. Click on the name of the desired account to expand the roles allocated to you. Click on "Access Keys" next to the name of the desired role.
    ```{image} images/aws-cli-access/select-access-keys.png
    :alt: AWS SSO account and role selection page with "Access Keys" circled in red
    ```
6. You will be presented with multiple options for acquiring access keys for the CLI. Click on the tab that matches your operating system (OS).
    ```{image} images/aws-cli-access/browser-cli-os-selection.png
    :alt: AWS CLI credentials access page with "macOS and Linux" circled in red
    ```
7. Expand the section named "Option 2: Add a profile to your AWS credentials file" and click on the overlapping squares icon to copy the configuration block that contain your credentials.
    ```{image} images/aws-cli-access/browser-cli-option2.png
    :alt: AWS CLI credentials access page with the copy icon circled in red next to a list of configuration lines that contain the current credentials and profile name
    ```
8. Append the credential block you copied in the previous step to your AWS credentials file. This file is located at `~/.aws/credentials` (for macOS and Linux) or `%USERPROFILE%\.aws\credentials` (for Windows). It's okay if other configuration is already present in this file.
    ```bash
    $ cat ~/.aws/credentials
    [111111111111_MyRole]
    aws_access_key_id=AAAAAAAAAAAAAAAAAAAA
    aws_secret_access_key=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    aws_session_token=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    ```
9. While these credentials can be used from any shell window, you'll need to specify the profile name to select them. You can do this by setting the environment variable `AWS_PROFILE` to the profile name or passing it on the command line.  Confirm your access by querying your AWS identity.

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
10. You are now authenticated for the AWS CLI. To log out, delete the lines you added from `~/.aws/credentials`.

## Option 3: CLI SSO Integration

This option is recommended when you want to use multiple shell sessions to access multiple AWS accounts or want to refresh credentials after the timeout period from the command line. For more information, please see the [official AWS SSO CLI documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html).

1. Configure CLI SSO settings. Append the following to your AWS CLI configuration file. This file is located at `~/.aws/config` (for macOS and Linux) or `%USERPROFILE%\.aws\config` (for Windows). You only have to do this once.
    ```ini
    [sso-session fedauth]
    sso_start_url = https://cuboulder.awsapps.com/start
    sso_region = us-west-2
    sso_registration_scopes = sso:account:access
    ```
2. Create a profile for each AWS account you want to configure in your `~/.aws/config` file. You can find appropriate account numbers and role names at the AWS access portal that you use when [logging in via a web browser](aws-console-access). Append an entry for each account as shown below. You only have to do this once.
    ```ini
    [profile awsucob0myaccount]
    sso_session = fedauth
    sso_account_id = 111111111111
    sso_role_name = MyRole
    region = us-west-2
    output = json

    [profile awsucob0myotheraccount]
    sso_session = fedauth
    sso_account_id = 222222222222
    sso_role_name = MyOtherRole
    region = us-west-2
    output = json
    ```
3. Log into SSO.
    ```bash
    $ aws sso login --sso-session fedauth
    Attempting to automatically open the SSO authorization page in your default browser.
    If the browser does not open or you wish to use a different device to authorize this request, open the following URL:

    https://device.sso.us-west-2.amazonaws.com/

    Then enter the code:

    ABCD-1234
    ```
    You will be prompted to log in via your default browser. Follow the [same flow as used when accessing the AWS console](aws-console-access). After authentication, you will be prompted to allow CLI access to your session. Enter the code ("ABCD-1234" in this example) and press "Submit and continue".
    ```{image} images/aws-cli-access/authorize-request.png
    :alt: AWS CLI authorization request web form with example credentials shown
    ```
    On the following page that says "Allow botocore-client-fedauth to access your data?", click "Allow access".
    ```{image} images/aws-cli-access/allow-botocore.png
    :alt: AWS CLI botocore authorization prompt
    ```
    You will be taken to a success page. 
    ```{image} images/aws-cli-access/request-approved.png
    :alt: AWS CLI authorization approved success page
    ```
    You can now close this page in your browser and return to the terminal. The terminal should say:
    ```bash
    Successfully logged into Start URL: https://cuboulder.awsapps.com/start
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
6. (Optional) Some AWS clients, notably [Terraform](https://github.com/hashicorp/terraform-provider-aws/issues/10851), don't support AWS SSO profiles for login. You can work around this by exporting SSO temporary credentials into your environment. **Note:** Exported credentials are not automatically refreshed when they expire.

    For macOS and Linux:
    ```bash
    $ export AWS_PROFILE=awsucob0myaccount
    $ eval $(aws configure export-credentials --profile $AWS_PROFILE --format env)
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
    $ iex ((aws configure export-credentials --profile $Env:AWS_PROFILE --format powershell) -join "`n")
    $ aws --no-cli-pager sts get-caller-identity
    {
        "UserId": "AAAAAAAAAAAAAAAAAAAAA:ralphie@colorado.edu",
        "Account": "111111111111",
        "Arn": "arn:aws:sts::111111111111:assumed-role/AWSReservedSSO_MyRole_aaaaaaaaaaaaaaaa/ralphie@colorado.edu"
    }
    ```
7. When done, log out from SSO and all accounts with:
    ```bash
    aws sso logout
    ```
