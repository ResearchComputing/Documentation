# AWS

Amazon Web Services (AWS) Documentation

This applies to customers who are using a **Research Computing Cloud Foundations** managed AWS account.

## Landing Zones

Each managed AWS account is associated with exactly one landing zone. A landing zone is a consistent group of account configuration, networking, and security controls that are applied to all associated accounts.

The Cloud Foundations team currently supports two landing zones, **LCA0** and **LCA1**. The landing zone associated with your AWS account dictates how you should log in and how the account is designed to work. You should reference documentation below that aligns with your landing zone.

### How do I know what landing zone my AWS account is in?

You received a url to log into your AWS account as part of your onboarding.

If you login via [https://buff.link/aws](https://buff.link/aws) or [https://fedauth.colorado.edu/idp/profile/SAML2/Unsolicited/SSO?providerId=urn:amazon:webservices](https://fedauth.colorado.edu/idp/profile/SAML2/Unsolicited/SSO?providerId=urn:amazon:webservices), your are using **LCA0**.

If you login via [https://aws.colorado.edu/](https://aws.colorado.edu/), you are using **LCA1**.

### Landing Zone: LCA0

LCA0 is the original landing zone, rated only for public data.

```{toctree}
:maxdepth: 2
:caption: LCA0

lca0/index

```

### Landing Zone: LCA1

LCA1 is the next generation landing zone that will be rated to support a variety of data classifications.

```{toctree}
:maxdepth: 2
:caption: LCA1

lca1/index

```
