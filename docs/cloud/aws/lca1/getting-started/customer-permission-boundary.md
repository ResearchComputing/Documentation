# Customer Admin Role Permission Limits

The `CustomerAdmin` role is the default role that customers use to administer their AWS account. This role should be used to set up new IAM roles and deploy required cloud infrastructure. In order to protect resources owned by other systems, some permissions are limited.

If you have any questions about `CustomerAdmin` permissions or they are blocking the deployment of cloud resources, please reach out to [rc-help@colorado.edu](mailto:rc-help@colorado.edu).

## Exclusions

Explicitly denied actions to the `CustomerAdmin` role include:

* Access to AWS GuardDuty
* Changes to AWS CloudTrail
* Changes to AWS Config
* Changes to AWS Control Tower
* Changes to AWS Identity Center
* Changes to AWS Organizations
* Changes to Account Aliases
* Changes to Default Account Password Policies
* Changes to OIT Cloud Foundations (CFS) resources
* Changes to VPC networking

```{note}
CFS-managed resources may be identified by one or more of the following:
* Tag: `oit-cld:management:central = true`
* Naming Prefix: `oitcld`
* Naming Prefix: `oit-cld-lza`
```

## Creating Users and Roles

The `Customeradmin` role should be treated similarly to other administrative accounts (think root or Administrator accounts) and only used when its privileges are needed. Customers are encouraged to create application-specific roles with permissions reduced to only what the application needs.

Creation of new users and roles is permitted with a few caveats:

* Users and roles must be assigned the `CustomerRolesPermissionBoundary` permissions boundary during creation.
* Customers take on the responsibility for managing and rotating any static credentials associated with AWS IAM users they create.

```{note}
Roles are preferred over users since they rely exclusively on temporary credentials for authentication.
```

```{important}
When using some AWS wizards to configure services, the wizard will try to create a new role. Often the wizard is not sophisticated enough to add a permissions boundary when creating a role, so it will fail. When encountering this situation, customers must manually create the role with the proper permissions and attach the permissions boundary discussed above. Then, in the wizard, pick the role that has already been created instead of allowing it to make a new one.
```

## Attaching Permissions Boundary

When creating new AWS Roles or Users, customers must set the permissions boundary.

On Step 2 of the "Create role" or "Create user" wizard, search for and add the `oitcld-customer-roles-permission-boundary` policy to the "Set permissions boundary" section.

```{image} images/customer-permission-boundary/permissions-boundary.png
:alt: Attaching a permissions boundary to a new role in the AWS console
```
