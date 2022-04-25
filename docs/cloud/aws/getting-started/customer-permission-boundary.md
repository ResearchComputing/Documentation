## Admin Account Permission Exclusions

todo: https://oitkb.colorado.edu/display/PC/AWS+Getting+Started+-+Admin+Account+Permission+Exclusions

### Standard Customer Administrator Role

The standard CU Boulder AWS Account Baseline sets up a powerful role for use by the administrators in the customer department.
This role will generally be used to set up new IAM roles and to deploy basic infrastructure, but should be treated similarly to other administrative accounts (think root or Administrator accounts) and only used when it's privileges are needed.
Please consider the principal of least privilege when managing your accounts.

In order to ensure that this role is not breaking components deployed as part of the CU Boulder standard AWS Account Baseline there are certain restrictions on what this role can perform.
Outside of these restrictions, the Customer Admin role will have full administrative privileges.


### Permission Boundary (limits permissions of new users or roles created by Customer Admin)

Creation of new users and roles by a Customer Admin role is only allowed if the Permission Boundary is attached at the creation of the user or role.
Permission Boundary is a policy created by Cloud Broker in your account named Customer_Admin_PermissionBoundary

