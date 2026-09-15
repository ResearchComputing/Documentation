# Amazon Web Services

This applies to customers who are using a **Research Computing Cloud Foundations** managed AWS account.

```{important}
Research Computing Cloud Foundations managed AWS accounts can be provisioned only for direct affiliates (students, faculty, staff) of the University of Colorado. Access to the account can be shared beyond that scope at the discretion of the account holder.
```

## Landing Zones

Each managed AWS account is associated with exactly one landing zone. A landing zone is a consistent group of account configuration, networking, and security controls that are applied to all associated accounts.

Currently we support two landing zones, **LCA0** and **LCA1**.

* LCA0: This is the original landing zone, intended for public data.
* LCA1: This is the next-generation landing zone, designed to support a wider range of data classifications. 

Your landing zone determines how you access your AWS account and which capabilities and controls apply to the account.

### How do I know what landing zone my AWS account is in?

You received an AWS login URL as part of the account onboarding process. The URL indicates which landing zone your account uses:

If you login via [https://aws-classic.colorado.edu/](https://aws-classic.colorado.edu/), you are using **LCA0**.
```{toctree}
:maxdepth: 2
:hidden:
lca0/index
```

If you login via [https://aws.colorado.edu/](https://aws.colorado.edu/), you are using **LCA1**.
```{toctree}
:maxdepth: 2
:hidden:
lca1/index
```
