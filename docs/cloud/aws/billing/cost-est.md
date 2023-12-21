# AWS - Network Cost Guide

## Document Purpose

This document gives some sample cost estimates for select network access methods and provides the URL's to find current pricing. 

## Network access methods 

1) Internet Gateway - used with public IP
2) NAT Gateway - used with private IP
3) CFS Transit Gateway (VPN) - used with private IP address, VPN connects back to CU Boulder

### Internet Gateway

**Important**
Always check [AWS documentation](https://aws.amazon.com/ec2/pricing/on-demand/) for current pricing.
 
**Network costs**

1) Downloads - no cost

2) Uploads - first 100GB/month is free, tiered cost per 1GB transferred after

**Sample Network Cost**

2 Servers will download 100GB and upload 500GB in a month.

	1) Download cost = $0
	2) Upload cost = (100GB = $0) + ($0.09 x 400GB) = $36

	Total Network Cost = $36/month

### NAT Gateway

**Important**
Always check [AWS documentation](https://aws.amazon.com/vpc/pricing/) for current pricing.

**Network Costs**
1) Downloads - $0.045/GB
2) Uploads - $0.045/GB
3) NAT Gatway - 0.045/hr

**Sample Network Cost**

2 Servers will download 100GB and upload 500GB in a month.  The NAT gateway will be on the entire month.

	1) Download cost = $0.045 x 100 = $4.50
	2) Upload cost = $0.045 x 500 = $22.50
	3) NAT Gateway Instance = $0.045 x (24hr x 30day= 720hr) = $32.40

	Total Network Cost = $59.40/month

### CFS Transit Gateway VPN

**Important**
Always check [AWS documentation](https://aws.amazon.com/transit-gateway/pricing/) for current pricing.

**Network Costs**
1) Downloads - $0.02/GB
2) Uploads - $0.02/GB
3) Attachment - $0.05/hr

**Sample Network Cost**

2 Servers will download 100GB and upload 500GB in a month.  The VPC attachment will be on the entire month.

	1) Download cost = $0.02 x 100 = $2
	2) Upload cost = $0.02 x 500 = $10
	3) Attachment cost = $0.05 x (24hr x 30day= 720hr) = $36

	Total Network Cost = $48/month

