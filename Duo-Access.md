Note: Once you have Duo set up you can make changes via the [duo.colorado.edu](duo.colorado.edu) website.
 
## Duo Instructions
1. CU Identity verification (done)
2. A Duo account is created for you and Duo sends you an invitation email, which comes from duosecurity.com or duo.com
3. You install the relevant Duo Mobile app if you want to use a smartphone (search for Duo Mobile in your app store)
4. You respond to the invitation and provision your Duo smartphone app for Duo Push
   * It is best to open the Duo Invite email on a desktop or laptop so you can scan the barcode with the phone.
   * If you want to use the app be sure not to request a phone call for authentication!
   * Scan the barcode in the email with your Duo app to provision it.
5. Test your login process, in this case via ssh to the RC login nodes:
   * Use your CU IdentiKey username `ssh <username>@login.rc.colorado.edu` or `ssh -l <username> login.rc.colorado.edu` and note that you should remove the <> from the command and that `ssh -l` uses a lowercase L.
   * You enter "duo:" followed by your IdentiKey Password at the password prompt, i.e. if your password is `MyUCB_PW` you enter `duo:MyUCB_PW` as your password. Our system recognizes the duo: prefix and knows you are using Duo rather than the hardware device option.
   * Duo contacts your smartphone and requests that you authorize the login via the Duo app.
   * You open the app and approve/deny the login request
   * Also confirm approval in the app
   * If your request is approved and confirmed in your app, you should be logged in
 
## Issues:
- Duo Invite email (from duosecurity.com) goes to Spam folder or is overlooked.
- Users open the email on their phone and then struggle with the provisioning, unable to scan the barcode on the screen.
- Users request a phone call instead of Push for authentication.
- Users tend to set up Duo without realizing they need to approve each login, then ignore the Duo requests on their phones.
- Users approve the login but do not Confirm the login with a second press in the phone app.
- Users get registered and then forget how to do the Duo-specific login procedure (password duo:IDKey_password)
- Users get new phones and need to re-do the provisioning process
- Device has no or a slow data connection (try wifi)
- Duo accounts are purged if unused for 3-6 months with no warning and no notification, after which login will not work until a new account is requested and a new invitation email sent.
- Users are distracted by the passcode that can be located in the phone app (we are not using it).
- The Duo request to the phone does not arrive due to a poor signal, you may need a WiFi connection in some buildings or areas.