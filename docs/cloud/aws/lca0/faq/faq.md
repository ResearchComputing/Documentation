# AWS - FAQs

Frequently Asked Questions

If you are looking for help with specific errors, please visit the [Troubleshooting](../troubleshooting/troubleshooting.md) guide.


## What is the URL for the Single Sign-On Console?
**Answer:**
Login using your [CU IdentiKey](https://oit.colorado.edu/services/identity-access-management/identikey) [here:](http://bit.ly/OIT-AWS).


## Why can't I see the AWS resources I created?
**Answer:**
Be sure that you have selected the correct AWS region.
Many AWS services are region specific.
Also make sure you are logged in to the correct AWS account with the correct Role.


## What region has the lowest latency from CU Campus?
**Answer:**
The **us-west-2** AWS region has the lowest latency from Colorado's Front Range region (CU Campuses).


## Can I use the root user?
**Answer:**
No.
The root user is owned by the **Research Computing Cloud Team**.
You must use your Customer-Admin role.


## Are MTurk users supported?
**Answer:**
MTurk users are only supported for programmatic access (AWS CLI).
Console users are not supported because it requires root user access.

## How do I close my AWS account?
**Answer:**
Send an email to [rc-help@colorado.edu](mailto:rc-help@colorado.edu) and provide the account number or account alias for the AWS Account you wish to close.  Be sure to leave your PO open for 2 billing cycles after the account has been closed to make sure there are no further charges before closing your PO.


## How do I find my Account ID and Alias?
**Answer:**
Click on the drop down on the top right corner of the console page to expand your account information.
```{image} images/AcctNum.png
:alt: AWS console home page with account information drop-down highlighted
```
