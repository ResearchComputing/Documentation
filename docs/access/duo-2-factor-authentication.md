## Duo 2-factor Authentication

Research Computing utilizes a 2-factor authentication utility called **Duo** that must be utilized in order to log into RC resources. **This document covers installing and logging in with Duo for CU Boulder users only.**

- For CSU Users please see [CSU's documentation on Duo 2-factor authentication](https://www.acns.colostate.edu/hpc/#remote-login)
- For RMACC Users please see [XSEDE's documentation on Duo 2-factor authentication](https://portal.xsede.org/mfa)

### Setting up Duo

1. You will receive a Duo invitation when your RC account is created. Open your Duo invitation email (from Duo security or duo.com) on a desktop/laptop computer.

   * **Within one business day you should recieve a duo invitation. If you didn't receive an invitation or your invitation has expired, then please contact rc-help@colorado.edu for a new invitation.**
2. Login with your CU identikey and follow the instructions to setup
     - Research Computing recommends users utilize Duo Mobile Push as your method of authenication: install the Duo Mobile app and link your account with your device.
3. Login to RC Resources via ssh [as described below.](#logging-in-with-duo)

#### Common Issues
A few common issues users will come across when using Duo include:

* A Duo Invite email may be sent to your Spam folder.
* Requesting a phone call if you want to use the Push app for authentication.
* A Duo account purged after remaining unused for 6-9 months.
* Having a new device and want to move Duo onto it.
    * [Check out our FAQ for detailed instructions on accomplishing this.](https://curc.readthedocs.io/en/latest/faq.html#i-have-a-new-phone-how-do-i-move-my-duo-onto-it)

Please contact us at rc-help@colorado.edu if you encounter these or any other issues regarding Duo.

### Logging in with Duo

Duo offers a variety of methods to log into your account. Depending on what you select when setting up your Duo account, you should have several different methods of 2-factor authentication when logging into RC Resources. 

#### Using Duo Mobile Push

**Duo Mobile Push is Research Computing's recommended method of 2-factor authentication.** Because Duo Push is tied to your physical smart device instead of a phone number or account, Duo Push is provides a more secure method of 2-factor authentication than either SMS or phone call.

1. Type: `ssh <username>@login.rc.colorado.edu` into the command line. For example, if my username is jodo2018 I would type `ssh jodo2018@login.rc.colorado.edu`
2. Enter your identikey password when prompted. 
3. Wait for a push to your phone.  

<p align="middle">
  <img src="https://raw.githubusercontent.com/ResearchComputing/Documentation/dev/duo2factor/duo_app2.png"/>
  <img src="https://raw.githubusercontent.com/ResearchComputing/Documentation/dev/duo2factor/duo_app1.png" /> 
</p>

**Note: Duo push is tied to your device so [so you will need to add or remove your device if you get a new phone.](#managing-duo-devices)**


#### Using Duo SMS

If you prefer to not use the Duo app or if you don't have a smart device, then Duo offers an SMS method of 2-factor authentication:

1. `ssh username@login.rc.colorado.edu` . For example, if my username is jodo2018 I would type `ssh jodo2018@login.rc.colorado.edu`
2. Enter your password when prompted, as `mypassword,sms`. For example, if my password is Ih3artdu0 I would type: `Ih3artdu0,sms`
3. A list of one-time-passwords (OTPs) will be texted to you via SMS. Another login prompt will appear on your screen. Using the first OTP in the list, login with your password as `mypassword,OTP`. For example, if my password is Ih3artdu0 and my OTP is 330456 I would type (without quotes): `Ih3artdu0,330456`.
4. Note that the next time you login, you can either request a new list of OTPs using Step 2 and then enter the first OTP via Step 3, or you can just use the next OTP in the list, and skip directly to Step 3.

#### Using Duo Phone Call

Duo also provides a phone call solution for 2-factor authorization if you only have a land line, or prefer to not use Push or SMS:

1. Type `ssh username@login.rc.colorado.edu` into the command line . For example, if my username is jodo2018 I would type `ssh jodo2018@login.rc.colorado.edu`
2. Enter your password when prompted, as `mypassword,phone`. For example, if my password is Ih3artdu0 I would type: `Ih3artdu0,phone`
3. Wait for a phone call. Answer the call, select option #1, and you will automatically be logged in.

#### Using the Duo Token

If you prefer a physical device, similar to the Vasco OTP.  You have to arrange with RC staff to acquire a token. There is a small fee for this device.  Email rc-help@colorado.edu for assistance.

1. `ssh username@login.rc.colorado.edu` . For example, if my username is jodo2018 I would type `ssh jodo2018@login.rc.colorado.edu`
2. Enter your password when prompted, as `mypassword,6-digit-number`. The 6-digit number is given to you on the Duo token.  For example, if my password is Ih3artdu0, and I press the button on the token and it is 123456, I would type: `Ih3artdu0,123456` 

### Managing Duo Devices

Users can manage their own Duo devices by visiting <a href="https://duo.colorado.edu">https://duo.colorado.edu</a>. This can allow users to add or remove activated devices at their discretion.

After a CU authorization page, you will be directed to a Duo authentication page. Do not respond to the Push notification and instead click the "Settings" button: 

![](https://raw.githubusercontent.com/ResearchComputing/Documentation/master/FAQ/duo-management1edit.png)

This will bring up a menu that provides several options on device management and general help. 

Clicking "Add a new device" will allow you to add a new smart phone, tablet, or land-line. Simply select the option you wish to add and follow the steps provided by Duo complete setting up your new device. 

Selecting "My Settings & Devices" provides a more detailed list of all devices you have registered. From here you can also add a new device, set your default device, and change your default authentication method when you attempt to log in.
