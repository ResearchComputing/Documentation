## Duo Instructions

1. Open your duo invitation email (from duo security or duo.com) on a desktop/laptop computer
1. Login with your CU identikey and follow the instructions to setup 
1. Install the Duo Mobile app and provision for Duo Push
         Note: If you want to use the app do not request a phone call for authentication!
1. Test your login process, in this case via ssh to the RC login nodes:
* Use your CU IdentiKey username "ssh @login.rc.colorado.edu" or "ssh -l login.rc.colorado.edu" and note that "ssh -l" uses a lowercase L.
*  Enter "duo:" followed by your IdentiKey Password at the password prompt, i.e. if your password is "MyUCB_PW" you enter "duo:MyUCB_PW" (omitting the quotes) as your password. 
*  Open the duo app and authorize the login via the Duo app.

## Issues to note:

* Duo Invite email may go to your Spam folder.
* Do not request a phone call instead of Push for authentication.
* Each login will need to be approved and confirmed (two presses) through the duo app.
* Duo accounts are purged if unused for 3-6 months.
* If you need additional help or Duo does not work for you please contact us at rc-help@colorado.edu

