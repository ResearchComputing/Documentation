- [Overview](#overview)
- [Logging in from a Windows Machine](#logging-in-from-a-windows-machine)
- [Logging in from a Mac](#logging-in-from-a-mac)

## Overview

Logging into a Research Computing login node is the first step in accessing resources  

- Requirements for logging in:
    + Research Computing account
    + Either Duo or an OTP device to prove your identity
    + [The PuTTY application](https://www.putty.org/) (if you are a Windows user)  

- Use login nodes only for:
    + Editing
    + Data transfer
    + Job submission
    + Accessing storage resources  

- For all other tasks, use:
    + Scheduled or interactive jobs
    + Compile nodes  

Need more assistance? Watch a tutorial video or read the text below.

## Logging in from a Windows Machine

Watch this [video](https://youtu.be/aUVdIShW7W4) or read the text below:


1. Open the PuTTY application on your computer
    * Under “Host Name (or IP address)”, enter `login.rc.colorado.edu`. Select “SSH” as the connection type. Click on “Open”.
2. Enter your Identikey in response to the “login as” prompt
3. When prompted to enter your password:
    * If you are logging in using Duo, type `duo:` and then your Identikey password. For example, if your Identikey password is 123, type `duo:123`. Press enter. You will then receive an authentication request from the Duo app on your phone. Approve the request.
    * If you are logging in with a Vasco OTP device, enter your four-digit PIN plus the six digits shown when you push the button on your device. For example, if your PIN is “1234” and the device shows “567890”, you will type `1234567890`. Press enter.
    * Note that as a security feature, PuTTY does not display any text while you type your password
Login screen for putty

![alt text](https://www.colorado.edu/p113a299a3a0/sites/default/files/styles/medium/public/page/login.png?itok=23Wma08Q)

## Logging in from a Mac

- Watch this [video](https://youtu.be/Q1_bhA7zgKg) or read the text below:


1. Under “File”, open a new finder window. Navigate to the “Applications” folder, then the “Utilities” folder. Open a terminal window. When the terminal window opens, type `ssh username@login.rc.colorado.edu. Press enter.
2. Enter your password:
    * If you are logging in using Duo, type `duo:` followed by your Identikey password. For example, if your Identikey password is 123, type `duo:123`. Press enter. You will then receive an authentication request on the Duo app on your phone. Approve the request.
    * If you are logging in with a Vasco OTP device, enter your four-digit PIN plus the six digits shown when you push the button on your device. For example, if your PIN is “1234” and the device shows “567890”, you will type `1234567890`. Press enter.
