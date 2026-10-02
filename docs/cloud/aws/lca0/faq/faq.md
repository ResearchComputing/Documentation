# Frequently Asked Questions

If you are looking for help with specific errors, please visit the [Troubleshooting](../troubleshooting/troubleshooting.md) guide.


## What is the URL for the Single Sign-On Console?
**Answer:**
Login using your [CU IdentiKey](https://oit.colorado.edu/services/identity-access-management/identikey) at [https://aws-classic.colorado.edu/](https://aws-classic.colorado.edu/).


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
No, the root user is owned by the **Cloud Foundations Service** team. You must use your `CustomerAdmin` role.


## Are MTurk users supported?
**Answer:**
MTurk users are only supported for programmatic access (AWS CLI).
Console users are not supported because it requires root user access.

## How do I close my AWS account?
**Answer:**
Submit a request using the [support request form](https://colorado.service-now.com/req_portal?id=ucb_sc_rc_form) and provide the account number or account alias for the AWS account you want to close. Leave your purchase order (PO) open for two billing cycles after the account is closed so any remaining charges can be processed before you close the PO.


## How do I find my Account ID and Alias?
**Answer:**
Click on the drop down on the top right corner of the console page to expand your account information.
```{image} faq_images/AcctNum.png
:alt: AWS console home page with account information drop-down highlighted. Described under How do I find my Account ID and Alias?
:align: center
```


## Can I alter or remove CFS resources?
**Answer:**
No. Resources owned by the **Cloud Foundations Service (CFS)** team cannot be altered or removed and they can be identified by name prefix and/or resource tags. Any resources with the prefix `oitcld-` are owned by CFS, in addition to those with the below tag attached.
```{image} faq_images/CFSTag.png
:alt: AWS resource tag with key oit-cld:management:central and value true. Described under Can I alter or remove CFS resources?
:align: center
```