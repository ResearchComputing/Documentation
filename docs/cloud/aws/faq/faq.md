## AWS - FAQs

Frequently Asked Questions

---

### What is the URL for the Single Sign-On Console?
**Answer:**
Login using your <a href="https://oit.colorado.edu/services/identity-access-management/identikey" target="_blank">CU IdentiKey</a> here: <a href="http://bit.ly/OIT-AWS" target="_blank">http://bit.ly/OIT-AWS </a>.

---

### Why can't I see the AWS resources I created?
**Answer:**
Be sure that you have selected the correct AWS region.
Many AWS services are region specific.
Also make sure you are logged in to the correct AWS account with the correct Role.

---

### Failed to create role: not authorized to perform: iam:CreateRole

**Answer:**
When creating AWS Roles, you must attach the "Customer_Admin_PermissionBoundary" Permission Boundary.
See [Admin Account Permission Exclusions](../getting-started/customer-permission-boundary.md)

---

### Unable to create user: not authorized to perform: iam:CreateUser

**Answer:**
When creating AWS Users, you must attach the "Customer_Admin_PermissionBoundary" Permission Boundary.
See [Admin Account Permission Exclusions](../getting-started/customer-permission-boundary.md)

---

### What region has the lowest latency from CU Campus?
**Answer:**
The **us-west-2** AWS region has the lowest latency from Colorado's Front Range region (CU Campuses).

---

### Can I use the root user?
**Answer:**
No.
The root user is owned by the CU Cloud Team.
You must use your Customer-Admin role.

---

### Are MTurk users supported?
**Answer:**
MTurk users are only supported for programmatic access (AWS CLI).
Console users are not supported because it requires root user access.

---
