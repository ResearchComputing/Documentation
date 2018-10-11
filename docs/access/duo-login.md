## Duo Login

This document will describe how to use Duo to log into Research Computing resources.

### Using Duo Push

Method 1: Using Duo Push (if you have a smart phone and have downloaded the duo app)

1. Type: `ssh username@login.rc.colorado.edu` into the command line. For example, if my username is jodo2018 I would type `ssh jodo2018@login.rc.colorado.edu`
2. Enter your password when prompted. For example, if my password is Ih3artdu0 I would type: `Ih3artdu0`
3. Wait for a push to your phone.


### Using Duo SMS

Method 2: Using Duo SMS (if you do not have a smart phone or prefer not to use the Duo app):

1. `ssh username@login.rc.colorado.edu` . For example, if my username is jodo2018 I would type `ssh jodo2018@login.rc.colorado.edu`
2. Enter your password when prompted, as `mypassword,sms`. For example, if my password is Ih3artdu0 I would type: `Ih3artdu0,sms`
3. A list of one-time-passwords (OTPs) will be texted to you via SMS. Another login prompt will appear on your screen. Using the first OTP in the list, login with your password as `mypassword,OTP`. For example, if my password is Ih3artdu0 and my OTP is 330456 I would type (without quotes): `Ih3artdu0,330456`.
4. Note that the next time you login, you can either request a new list of OTPs using Step 2 and then enter the first OTP via Step 3, or you can just use the next OTP in the list, and skip directly to Step 3.

### Using Duo Phone Call

Method 3: Using Duo phone call: (if you have a land line, or if you do not have a smart phone, or if you prefer not to use SMS):

1. Type `ssh username@login.rc.colorado.edu` into the command line . For example, if my username is jodo2018 I would type `ssh jodo2018@login.rc.colorado.edu`
2. Enter your password when prompted, as `mypassword,phone`. For example, if my password is Ih3artdu0 I would type: `Ih3artdu0,phone`
3. Wait for a phone call. Answer the call, select option #1, and you will automatically be logged in.

### Using the Duo Token

Method 4: using the duo token: (if you prefer a physical device, similar to the Vasco OTP.  You have to arrange with RC staff to acquire a token.  There is a small fee for this device.  Email rc-help@colorado.edu for assistance):

1. `ssh username@login.rc.colorado.edu` . For example, if my username is jodo2018 I would type `ssh jodo2018@login.rc.colorado.edu`
2. Enter your password when prompted, as `mypassword,6-digit-number`. The 6-digit number is given to you on the Duo token.  For example, if my password is Ih3artdu0, and I press the button on the token and it is 123456, I would type: `Ih3artdu0,123456`
