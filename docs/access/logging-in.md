## Logging In

Research Computing offers a variety of resources for researchers to use in their own projects. To get started with Research Computing resources you need the following: 

- [A Research Computing account](https://rcamp.rc.colorado.edu/accounts/account-request/create/organization)
- [Duo 2 factor authentication](duo-2-factor-authentication.html)
- [The PuTTY application](https://www.putty.org/) (if you are a Windows user)  

Users accessing RC's resources will be connected to a login node. A login node is a outward facing node within the Research Computing environment that users can connect to from their local machines. Once on a login node, users can perform a limited number of tasks:

+ Edit files
+ Transfer Data
+ Submit Jobs
+ Access storage resources  

Note that the login nodes should not be used for resource-intensive tasks such as running code. For all other tasks, users should submit batch jobs, interactive jobs, or use the compile nodes.

+ **For CSU users, please refer to the [CSU login guide.](https://www.acns.colostate.edu/hpc/#remote-login)**  
+ **For RMACC users, pleaser refer to [RMACC Access to Summit.](rmacc.html)**

<iframe id="ytplayer" type="text/html" width="640" height="360" src="https://www.youtube.com/embed/PCMy5qDw3Nw?autoplay=0" frameborder="0" allowfullscreen="allowfullscreen"></iframe>  

---

### Getting an account

Although Research Computing resources are free and available to the CU Boulder research community, they are also managed resources with large value and high demand. Therefore, Research Computing mandates that each user obtain a Research Computing account. Please note that **Research Computing accounts are separate from your CU accounts. You must sign up for an individual Research Computing account if you wish to access Research Computing resources.**

A Research Computing account can be secured quickly and easily [by filling out the form here](https://rcamp.rc.colorado.edu/accounts/account-request/create/organization). Once you've received an account with Research Computing, you will automatically be sent an invitation for Duo enrollment via email. After you have accepted the Duo invitation, you will be able to authenticate via Duo and log into the system.
  
### Logging in from a Windows Machine

Logging in from a Windows machine requires the additional step of [installing the PuTTY ssh client](https://www.putty.org/) onto your local machine. This application allows users to connect to remote servers with the ssh protocol. Note that there are other ssh clients that allow Windows machines to connect to remote ssh servers; Research Computing recommends PuTTY for reliability and simplicity.

1. Open the PuTTY application on your computer
    * Under “Host Name (or IP address)”, enter `login.rc.colorado.edu`. Select “SSH” as the connection type. Click on “Open”.
2. Enter your Identikey in response to the “login as” prompt
3. When prompted to enter your password:
    * If you are logging in using Duo Push, simply type your Identikey password. You will then receive an authentication request from the Duo app on your phone. Approve the request.
    * If you are using Duo SMS, Phone Call, or Token login methods, instructions can be [found here](duo-2-factor-authentication.html).
    * Note that as a security feature, PuTTY does not display any text while you type your password


### Logging in from a Mac

Logging in with a Mac requires no extra installation on your local machine. Simply utilize the terminal application that is pre-installed with your operating system to access Research Computing resources. 

1. Under “File”, open a new finder window. Navigate to the “Applications” folder, then the “Utilities” folder. Open a terminal window and type `ssh username@login.rc.colorado.edu`, where `username` is your assigned username. Press enter.
2. Enter your password:
    * If you are logging in using Duo Push, type your Identikey password.  You will then receive an authentication request on the Duo app on your phone. Approve the request.
    * If you are using Duo SMS, Phone Call, or Token login methods, instructions can be [found here](duo-2-factor-authentication.html).

### Logging in from Linux

Much like with Macs, Linux machines require no additional setup to access Research Computing resources. Simply utilize the your Linux terminal to access Research Computing resources. 

1. Open a terminal window from your application menu and type: `ssh username@login.rc.colorado.edu`, where `username` is your research computing username.

2. Enter your password:
    * If you are logging in using Duo Push, simply type your Identikey password. You will then receive an authentication request on the Duo app on your phone. Approve the request.
    * If you are using Duo SMS, Phone Call, or Token login methods, instructions can be [found here](duo-2-factor-authentication.html).

### SSH host keys

The first time you log into an RC login node you will be asked to verify the host key. You can refer to the keys published here to confirm that you are connecting to a valid RC login node.

Note that each login node may support more than one type of key, but only one is used (or displayed) by your client at any given time.

#### login.rc.colorado.edu (as of 9 May 2018)

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

#### blogin01.rc.colorado.edu
A private login node owned by ICS

```
# Fingerprint
# 256 SHA256:SLljPqUgIZZrMPY127ssUeg++52w1vsqJva9NBKB8vk no comment (ECDSA)
ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBNcwOXb6FQ0kOwEtoNHqYur2xc3t+DwidHJbzRBasCqp8+YE/GSr2SGgtI4JkJ40ptAPjkdj+Qq9BRdu4ZExVdE=
```

```
# Fingerprint
# 256 SHA256:wTJn1ncRQOHETKi7M2HSdjPFhzvo7bG4KczP0ugqNX0 no comment (ED25519)
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMIqWL6qCI0y4MzZBgNyRrNX/Wd39/j1F/onx9tPMPos
```

```
# Fingerprint
# 2048 SHA256:MkKuFpFDNn9xWPBURKxHdUk55q5NBcGeRzgh+BANKpI no comment (RSA)
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDjjl4hOTvUCrfyIgFriFn+6ypLKxb7RQtWEmmmS0a8+icnocCiaZLpiS6lC7sMy7NYly6P6jnasTZvYUZ+6hcIm61YyOSDCCsMZCU+LQb66LIUPttz7ZF12KMgC/DDBAE8xj48hRmp9iZjFnYCEQi9eb4y1IN3VJz1k7nDfLa/Ae3DRBorGZVSKCoeBXfzjpTutCZwgoNUSHQUnZlLnwdut4WH9qq7GtnKRnstVJt+i72vOxLCFSuCgskCjBr5KP/aCEiXT5l93R01hceENIzKqN4zm0MhzULef6KXS7aZZDKb/zklOGUtxcHgdrQ9IeEQIESvn385yZU6IZIM+Hsb
```
