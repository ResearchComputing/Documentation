## AWS - Troubleshooting

Troubleshooting AWS Errors

---

### Failed to create role: not authorized to perform: iam:CreateRole

**Error:**
![](images/create-role.png)

**Solution:**

When creating AWS Roles, you must attach the "Customer_Admin_PermissionBoundary" Permission Boundary.
See [Admin Account Permission Exclusions](../getting-started/customer-permission-boundary.md)

---

### Unable to create user: not authorized to perform: iam:CreateUser

**Error:**
![](images/create-user.png)

**Solution:**

When creating AWS Users, you must attach the "Customer_Admin_PermissionBoundary" Permission Boundary.
See [Admin Account Permission Exclusions](../getting-started/customer-permission-boundary.md)

---