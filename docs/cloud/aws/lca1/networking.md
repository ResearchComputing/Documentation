# LCA1 Networks
LCA1 has 2 networks for customer use.
| Name      | Use               |
| :---      | :---              |
| Internet  | Workloads         |
| Private   | Load Balancers    |      

# Network Protection

## OIT Managed Firewall

The Internet and Private Subnets are behind an OIT managed firewall.  The managed firewall protects CU Boulder, AWS deployed, resources by preventing connections from:

### LCA1 Internet Subnet
- Curated list of known bad actors 
- High Risk Applications

### LCA1 Private Subnet
- High Risk Applications
- CU Boulder ResNet
- CU Boulder UCB Wireless
- CU Boulder Guest Wireless

The OIT managed firewall allows select, well known, applications to the Internet Subnet by default.

## Customer Managed Security Groups

Internet and Private Subnets can also utilize [AWS Security Groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) for granular controls.  Security Groups are within the customer span of control and can be deployed or modified quickly with customer security requirements.

## VPN
Connectivity to CU Boulder networks, including DNS, is through redundant VPN tunnels.  These tunnels use advanced ecryption alogrithms to secure connections between the LCA1 Private subnet and the CU Boulder campus.

###### NOTE ######
The LCA1 Internet subnet does not route through the VPN tunnel and internet connections to the CU Boulder campus will need to permitted by the campus Border Firewall.

## FAQS
- Can I use both the managed firewall and security groups
    - yes!  The managed firewall is application aware so there may be use cases that leverage this awarness.  An example, preventing a SQL packet from using a TCP 22 allowance that was intended to allow SSH.
- Can I only have AWS Security Groups
    - yes!  The managed firwall items listed above will always be allowed/denied respectively but after that AWS Security Groups can be used exclusively to control connections.


```{toctree}
:maxdepth: 2
:caption: LCA1-Network
```  
