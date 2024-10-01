# Network Information

## Network Layout

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
  - Deployments with direct inbound/outbound internet access.
* - Private
  - oit-cld-lza-private-az1
  - Deployments that need direct access to campus resources or that should not be exposed to the internet directly.
* - Private
  - oit-cld-lza-private-az2
  - Deployments that need direct access to campus resources or that should not be exposed to the internet directly.
* - 
  - oit-cld-lza-fw-internet-az1
  - Not for customer deployments. Infrastructure network.   
* - 
  - oit-cld-lza-fw-internet-az2
  - Not for customer deployments. Infrastructure network.   
* - 
  - oit-cld-lza-fw-private-az1
  - Not for customer deployments. Infrastructure network.   
* - 
  - oit-cld-lza-fw-private-az2
  - Infrastructure network.  Not for customer deployments.
* - 
  - oit-cld-lza-tgw-az1
  - Not for customer deployments. Infrastructure network.   
* - 
  - oit-cld-lza-tgw-az2
  - Not for customer deployments. Infrastructure network.   
```

## Network Protection

### OIT Managed Firewall

Both the Internet network and Private network route through an OIT firewall.  The OIT firewall allows select, well known, applications inbound to the Internet network by default.  Connections to/from campus to the Private network are generally allowed by default with some exceptions.  The OIT firewall protects deployments by preventing connections from:

#### Internet network
- Curated list of known bad actors 
- High Risk Applications
- Internet port scans

#### Private network
- High Risk Applications
- CU Boulder ResNet
- CU Boulder UCB Wireless
- CU Boulder Guest Wireless

### Customer Managed Security Groups

Both Internet and Private networks should also utilize [AWS Security Groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html), which are customer deployed, for granular controls.  Security Groups use IP Source/Destination addresses and TCP/UDP Source/Destination Ports for filtering.

### Security Groups vs OIT Firewall

The OIT firewall is application-aware, which means it can identify an application based off of network behavior in addition to port and protocol.  As an example, it can prevent a SQL packet from using a 22/TCP exception that was intended to allow SSH.  Changes to OIT firewall policy require a ticket to [rc-help@colorado.edu](mailto:rc-help@colorado.edu).

Security Groups are within the customer's span of control.  This means they can modify Security Groups quickly to meet security requirements without engaging an external group.  Security Groups can dynamically reference AWS resources but are not able to identify traffic by network behavior.

## Network Routing

### VPN
Connectivity to CU Boulder networks is through redundant VPN tunnels.  These tunnels use advanced encryption algorithms to secure connections between the Private network and the CU Boulder campus.  These tunnels provide access to:
- CU Boulder Public Networks
- CU Boulder Private Networks
- CU Boulder DNS lookups for public/private domain names

#### Private network
- **Internet:**  Routes to internet via Network Address Translation (NAT), no inbound from internet
- **Campus:**  Routes through the VPN to and from campus, private campus IP subnets and internal DNS supported 
- **Intra VPC:**  Routes directly to other VPC networks in the same account

#### Internet network 
- **Internet:**  Routes directly to and from the internet
- **Campus:**  Routes through public internet, no connectivity to private campus IP subnets and internal DNS 
- **Intra VPC:**  Routes directly to other VPC networks in the same account

```{note}
The Internet network does not route through the VPN tunnel.  Customer deployments in the Internet network may require a firewall exception at the campus Border Firewall in order to access some CU Boulder resources.
```