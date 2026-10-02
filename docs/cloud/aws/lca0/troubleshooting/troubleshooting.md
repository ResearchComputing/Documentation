# Troubleshooting

This page covers common AWS permission errors in CU Boulder AWS accounts. Most of these errors occur when a new IAM user or role is created without the required permissions boundary.

If you are looking for general account questions, see the [FAQs](../faq/faq.md) section.

## Failed to create role: not authorized to perform: iam:CreateRole

This error appears in the AWS Management Console when you create an IAM role without attaching the required permissions boundary.

```{image} troubleshooting_images/create-role.png
:alt: AWS console error banner stating Failed to create role because iam:CreateRole is denied by a permissions boundary. Error message: User: arn:aws:sts::<account-id>:assumed-role/Shibboleth-Customer-Admin/<user>@colorado.edu is not authorized to perform: iam:CreateRole on resource: arn:aws:iam::<account-id>:role/<role-name> with an explicit deny in a permissions boundary.
:align: center
```

**Solution:**

When creating AWS Roles, you must attach the "Customer_Admin_PermissionBoundary" Permission Boundary.
See [Admin Account Permission Exclusions](../customer-permission-boundary.md) section.

## Unable to create user: not authorized to perform: iam:CreateUser

This error appears in the AWS Management Console when you create an IAM user without attaching the required permissions boundary.

```{image} troubleshooting_images/create-user.png
:alt: AWS console error titled Unable to create user, stating AWS could not create the user you requested. The Error message in the image: User arn:aws:sts::<account-id>:assumed-role/Shibboleth-Customer-Admin/<user>@colorado.edu is not authorized to perform: iam:CreateUser on resource: arn:aws:iam::<account-id>:user/<user-name> with an explicit deny in a permissions boundary.
:align: center
```

**Solution:**

When creating AWS users, attach the `Customer_Admin_PermissionBoundary` permissions boundary. See [Admin Account Permission Exclusions](../customer-permission-boundary.md) section.


## AccessDenied: not authorized to perform: iam:CreateRole | Module Block

This error occurs when creating an Amazon EKS cluster with the [Terraform EKS module](https://registry.terraform.io/modules/terraform-aws-modules/eks/aws/latest) from the Terraform Registry.

This is not an AWS or Terraform bug. It happens when CU Boulder AWS customers use the Customer Admin IAM role to create an EKS cluster without passing the permissions boundary into the module.

The first error is raised from the EKS module IAM role. The second error is raised from the EKS managed node group submodule IAM role.

```{image} troubleshooting_images/create-role-terraform.png
:alt: Terminal output showing two Terraform AccessDenied errors for iam:CreateRole due to a permissions boundary. Error 1 (EKS module IAM role): Error creating IAM Role (<cluster-role-name>): AccessDenied for User arn:aws:sts::<account-id>:assumed-role/Shibboleth-Customer-Admin/<user> to perform iam:CreateRole on resource arn:aws:iam::<account-id>:role/<cluster-role-name> with an explicit deny in a permissions boundary (status code 403) at module.eks.aws_iam_role.this[0] in .terraform/modules/eks/main.tf line 387. Error 2 (EKS managed node group submodule IAM role): Error creating IAM Role (<node-group-role-name>): AccessDenied for the same user on resource arn:aws:iam::<account-id>:role/<node-group-role-name> with an explicit deny in a permissions boundary (status code 403) at module.eks.module.eks_managed_node_group["example"].aws_iam_role.this[0] in .terraform/modules/eks/modules/eks-managed-node-group/main.tf line 497.
:align: center
```

**Solution:**

Pass the `Customer_Admin_PermissionBoundary` permissions boundary twice: once on the EKS module and once on each EKS managed node group.

```
module "eks" {
  iam_role_permissions_boundary = "arn:aws:iam::<AWS-account-number>:policy/Customer_Admin_PermissionBoundary"

  eks_managed_node_groups = {
    example = {
      iam_role_permissions_boundary = "arn:aws:iam::<AWS-account-number>:policy/Customer_Admin_PermissionBoundary"
    }
  }
}
```


## AccessDenied: not authorized to perform: iam:CreateRole | Resource Block

This error occurs when creating an EKS cluster with an [AWS IAM role Terraform resource](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role).

This is not an AWS or Terraform bug. It happens when CU Boulder AWS customers use the Customer Admin IAM role to create an EKS cluster without attaching the permissions boundary to the role resource.


```{image} troubleshooting_images/create-role-terraform-resource.png
:alt: Terminal output showing a Terraform AccessDenied error for iam:CreateRole on an aws_iam_role resource because of a permissions boundary. Error message: Error creating IAM Role (eks-cluster-example): AccessDenied: User arn:aws:sts::<account-id>:assumed-role/Shibboleth-Customer-Admin/<user> is not authorized to perform iam:CreateRole on resource arn:aws:iam::<account-id>:role/eks-cluster-example with an explicit deny in a permissions boundary (status code 403) with aws_iam_role.example on eks.tf line 39 in resource "aws_iam_role" "example".
:align: center
```

**Solution:**

Attach the `Customer_Admin_PermissionBoundary` permissions boundary on the IAM role resource:

```
resource "aws_iam_role" "example" {
  permissions_boundary = "arn:aws:iam::<AWS-account-number>:policy/Customer_Admin_PermissionBoundary"
}
```