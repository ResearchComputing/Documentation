## Logging In

Logging into a Research Computing login node is the first step in accessing resources  

- Requirements for logging in:
    + Research Computing account
    + Duo 2 factor authentication
    + [The PuTTY application](https://www.putty.org/) (if you are a Windows user)  

- Use login nodes only for:
    + Editing
    + Data transfer
    + Job submission
    + Accessing storage resources  

- For all other tasks, use:
    + Scheduled or interactive jobs
    + Compile nodes  

__For CSU users, please refer to the CSU login guide [found here](https://www.acns.colostate.edu/hpc/#remote-login)__

Need more assistance? Watch our tutorial videos for [Mac](https://www.youtube.com/watch?v=2Mnr840YdiE) or [Windows](https://youtu.be/aUVdIShW7W4), or read the text below.

### Logging in from a Windows Machine

Watch this [video](https://youtu.be/aUVdIShW7W4) or read the text below:

[![Logging-In-From-Windows-Video](https://raw.githubusercontent.com/ResearchComputing/Research-Computing-User-Tutorials/master/Logging-in/Logging-In-Windows.jpg)](https://youtu.be/aUVdIShW7W4)

1. Open the PuTTY application on your computer
    * Under “Host Name (or IP address)”, enter `login.rc.colorado.edu`. Select “SSH” as the connection type. Click on “Open”.
2. Enter your Identikey in response to the “login as” prompt
3. When prompted to enter your password:
    * If you are logging in using Duo Push, simply type your Identikey password. You will then receive an authentication request from the Duo app on your phone. Approve the request.
    * If you are using Duo SMS, Phone Call, or Token login methods, instructions can be [found here](duo-login.md).
    * Note that as a security feature, PuTTY does not display any text while you type your password
Login screen for putty
<!--
![Logging-in-example-screen](https://raw.githubusercontent.com/ResearchComputing/Research-Computing-User-Tutorials/master/Logging-in/Logging-In-Pic1.png)
-->

### Logging in from a Mac

Watch this [video](https://www.youtube.com/watch?v=2Mnr840YdiE) or read the text below:

[![Logging-In-From-A-Mac-Video](https://raw.githubusercontent.com/ResearchComputing/Research-Computing-User-Tutorials/master/Logging-in/Logging-In-Mac-Vid.jpg)](https://www.youtube.com/watch?v=2Mnr840YdiE)

1. Under “File”, open a new finder window. Navigate to the “Applications” folder, then the “Utilities” folder. Open a terminal window. When the terminal window opens, type `ssh username@login.rc.colorado.edu`, where `username` is your assigned username. Press enter.
2. Enter your password:
    * If you are logging in using Duo Push, type your Identikey password. For example, if your Identikey password is 123, type `123`. Press enter. You will then receive an authentication request on the Duo app on your phone. Approve the request.
    * If you are using Duo SMS, Phone Call, or Token login methods, instructions can be [found here](https://github.com/ResearchComputing/Research-Computing-User-Tutorials/wiki/Logging-in-with-Duo).

### Logging in from Linux

1. Open a terminal window from your distribution's application menu and type: `ssh username@login.rc.colorado.edu`, where `username` is your research computing username.

2. Enter your password:
    * If you are logging in using Duo Push, simply type your Identikey password. You will then receive an authentication request on the Duo app on your phone. Approve the request.
    * If you are using Duo SMS, Phone Call, or Token login methods, instructions can be [found here](https://github.com/ResearchComputing/Research-Computing-User-Tutorials/wiki/Logging-in-with-Duo).

### SSH host keys

The first time you log into an RC login node you will be asked to verify the host key. You can refer to the keys published here to confirm that you are connecting to a valid RC login node.

Note that each login node may support more than one type of key, but only one is used (or displayed) by your client at any given time.

#### login.rc.colorado.edu (as of 9 May 2018)

<!--
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
-->
