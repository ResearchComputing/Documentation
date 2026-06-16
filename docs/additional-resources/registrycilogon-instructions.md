# Uploading an SSH Key to CILogon Registry  

CU Boulder Research Computing uses [CILogon](https://www.cilogon.org/) to manage key-based login (CU Anschutz users, only) and passwordless data transfers with `scp` and `rsync` (CU Boulder and AMC, only). Access to the [RMACC CILogon Registry](https://registry.cilogon.org/registry/) is available by invitation only.

## *Step 1: Enroll in the RMACC CILogon Registry*

Request an invitation to the RMACC CILogon Registry by submitting a [support request form](https://colorado.service-now.com/req_portal?id=ucb_sc_rc_form) and explaining your intended use case (e.g., automated data transfers). After your case has been assigned, you will receive an email from <registry@cilogon.org> inviting you to enroll in the RMACC Registry. 
<br>

![](./registry-images/email_invitation.png)

Follow the invitation URL and click "Accept". __The invitation link becomes invalid once you click "Accept", so be sure to complete [Step 1](#step-1-enroll-in-the-rmacc-cilogon-registry), [Step 2](#step-2-generate-an-ssh-key), and [Step 3](#step-3-upload-your-ssh-key-to-registrycilogonorg) before closing your browser tab.__ 

![](./registry-images/accept_invitation.png)

You will be automatically routed to the login page. If you access CURC resources with a CU Boulder account, select "University of Colorado at Boulder" from the Identity Provider dropdown menu and click "Log On". 
If you access CURC resources with an ACCESS account, select "ACCESS CI (XSEDE)" from the dropdown menu.
<br>
![](./registry-images/cu-boulder-dropdown.png)


Enter your CU Boulder or ACCESS username and password and click "Login". Accept the Duo push from your device.

```{important}
You can move on to Step 2, but please make sure 10 minutes have elapsed between completing Step 1 and beginning Step 3.
```

## *Step 2: Generate an ssh key*

You are strongly encouraged to set a passphrase for your key pair. You will be prompted to enter the passphrase each time you log in. You are also strongly encouraged to create an ed25519 key type.

### SSH Key Generation for Windows Users: 
- It is recommended you use Powershell, but command prompt or a basic windows terminal will also work:
Once inside Powershell (or similar), execute the following command:
```
ssh-keygen -t ed25519
```
- After, it is important that you **_create a passphrase_** and note the file path of the generated key. This will be important for step 3. Example output:

```
Z:\> ssh-keygen -t ed25519
Generating public/private ed25519 key pair.
Enter file in which to save the key (C:\Users\username/.ssh/id_ed25519):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in C:\Users\username/.ssh/id_ed25519.
Your public key has been saved in C:\Users\username/.ssh/id_ed25519.pub.
The key fingerprint is :
SHA256:<key here>
The key's randomart image is:
+-- [ED25519 256] --+
|   .++*=B=.        |
...
+---- [SHA256] -----+
```
<br>

- Using PuTTY: <https://devops.ionos.com/tutorials/use-ssh-keys-with-putty-on-windows/>

### SSH Key Generation for Mac and Linux Users: 
- From a terminal window, execute the following command:
```
ssh-keygen -t ed25519
```
- After, it is important that you **_create a passphrase_** and note the file path of the generated key. This will be important for step 3. Example output:

```
username$ ssh-keygen -t ed25519
Generating public/private ed25519 key pair.
Enter file in which to save the key (/Users/username/.ssh/id_ed25519):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /Users/username/.ssh/id_ed25519.
Your public key has been saved in /Users/username/.ssh/id_ed25519.pub.
The key fingerprint is :
SHA256:<key here>
The key's ranomart image is:
+-- [ED25519 256] --+
|   .++*=B=.        |
...
+---- [SHA256] -----+
```
<br>
- NOTE for Mac users: There is a chance you need to create or alter your ssh config file (~/.ssh/config). See more in the [Troubleshooting](#troubleshooting) section below.

## *Step 3: Upload your ssh key to registry.cilogon.org*

After logging into [registry.cilogon.org](https://registry.cilogon.org/registry/) with your credentials, click on the dropdown menu in the upper right hand corner by your name. 
Select "MY PROFILE (RMACC)".

Select "Authenticators" from the menu on the right. 
<br>

![](./registry-images/menu_options.png)
<br>

Click "Manage" in the SSHKeyAuthenticator row. 
![](./registry-images/manage_sshkeyauthenticator.png)

Select "Add SSH Key".
![](./registry-images/add_sshkey.png)

Click "Choose File". If you store your SSH keys in a hidden directory (e.g. `~/.ssh`), it may be difficult to locate your public key using a Finder/File Explorer window. As a workaround, you can copy your public key to an easily discoverable location using the Terminal App/Windows Command Prompt:

```
cp ~/.ssh/id_rsa.pub ~/Desktop
```

Locate your __public__ key (`<keyname>.pub`) on your local drive, then click "UPLOAD".
![](./registry-images/upload_sshkey.png)

<br>

A green message box will notify you that your SSH key was successfully added to your account.
<br>
![](./registry-images/sshkeyadded.png)

## Deleting or Replacing SSH Keys in RMACC CILogon Registry

Log in at [registry.cilogon.org](https://registry.cilogon.org/registry/) and navigate to the "Authenticators" section of your profile (see [Step 3](#step-3-upload-your-ssh-key-to-registrycilogonorg), above). Click "Delete", then repeat the process for adding a new key. It will take a few minutes before you can log in with your new key.

## Troubleshooting
* For Mac users: If you have set up the key and followed all the steps above but are prompted for a **__password__** instead of a **__passphrase__**, you may need to edit or create a config file (~/.ssh/config). If you don't have an ssh config file, you can create it from the terminal window with the command `touch ~/.ssh/config`. After, edit the file and add the following 3 lines before trying again:
```
Host *
HostKeyAlgorithms ssh-ed25519
PubkeyAcceptedAlgorithms ssh-ed25519
```
* If you receive an error message indicating that you are not in the COmanage registry (see screenshot below), please submit a [support request form](https://colorado.service-now.com/req_portal?id=ucb_sc_rc_form). 

![](./registry-images/notregistered_error.png)
<br>
