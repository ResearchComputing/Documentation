# Network Information
LCA1 has 2 networks in 2 Availability Zones (az1 or az2) for customer use.

```{list-table} Customer Networks
:widths: 10 20 70
:header-rows: 1

* - Shortname
  - Full Name
  - Use
* - Internet
  - oit-cld-lza-internet-az1
  - Deployments with direct inbound/outbound internet access.
* - Internet
  - oit-cld-lza-internet-az2
  - Deployments with direct inbound/outbout internet access.
* - Private
  - oit-cld-lza-private-az1
  - Deployments that need direct access to campus resources or that should not be exposed to the internet directly.
* - Private
  - oit-cld-lza-private-az2
  - Deployments that need direct access to campus resources or that should not be exposed to the internet directly.

```
# Network Protection

## OIT Managed Firewall

Both the Internet and Private customer networks route through an OIT managed firewall.  The OIT managed firewall allows select, well known, applications to the Internet network by default.  Connections to/from campus to the Private network are generally allowed by default with exceptions listed below.  The firewall protects deployments by preventing connections from:

### Internet network
- Curated list of known bad actors 
- High Risk Applications
- Internet port scans

### Private network
- High Risk Applications
- CU Boulder ResNet
- CU Boulder UCB Wireless
- CU Boulder Guest Wireless


## Customer Managed Security Groups

Internet and Private Subnets can also utilize [AWS Security Groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) for granular controls.  Security Groups use IP Source/Destination addresses and TCP/UDP Source/Destination Ports for filtering.

Security Groups are within the customer's span of control.  This means you can deployed, or modify, Security Groups quickly with your security requirements.   

## VPN
Connectivity to CU Boulder networks is through redundant VPN tunnels.  These tunnels use advanced ecryption alogrithms to secure connections between the Private network and the CU Boulder campus.  These tunnels will carry campus:
- public Networks
- private Networks
- DNS lookups for public/private namespace

```{note}
The Internet network does not route through the VPN tunnel.  Customer deployments in the Internet network may require firewall exception at the campus Border Firewall in order to access some CU Boulder resources.
```


## FAQS

```{list-table} Frequently Asked Questions
:widths: 30 70
:header-rows: 1

* - Question
  - Answer
* - Can I use both the managed firewall and security groups
  - YES!  All traffic is routed through the managed firewall so you can work with OIT to identify and permit/block applications.  The managed firewall is application aware so there may be use cases that leverage this awarness.  An example, preventing a SQL packet from using a TCP 22 allowance that was intended to allow SSH.
* - Can I only have AWS Security Groups
  - YES!  The managed firwall items listed above will always be allowed/denied respectively but after that AWS Security Groups can be the customers exclusive method to control connections.
```

```{toctree}
:maxdepth: 2
:caption: LCA1-Network
```  
