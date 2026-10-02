# Amazon Web Services

```{important}
Cloud Foundations managed AWS accounts can be provisioned only for direct affiliates (students, faculty, and staff) of the University of Colorado. Access to the account can be shared beyond that scope at the discretion of the account holder.
```

## Landing Zones

Every managed AWS account is associated with exactly one landing zone. A landing zone is a standardized set of account configuration, networking, and security controls that is applied to the accounts associated with it.

Currently we support two landing zones:

| Landing zone | Description |
| --- | --- |
| LCA0 | The original landing zone, intended for public data. |
| LCA1 | The next-generation landing zone, designed to support a wider range of data classifications. |

Your account's landing zone determines how you access your AWS account and which capabilities and security controls are available.

### How do I know what landing zone my AWS account is in?

You can determine which landing zone your AWS account uses from the AWS login URL provided during account onboarding.

If you access your AWS account through [https://aws-classic.colorado.edu/](https://aws-classic.colorado.edu/), you are using **LCA0**.
```{toctree}
:maxdepth: 2
:hidden:
lca0/index
```

If you access your AWS account through [https://aws.colorado.edu/](https://aws.colorado.edu/), you are using **LCA1**.
```{toctree}
:maxdepth: 2
:hidden:
lca1/index
```