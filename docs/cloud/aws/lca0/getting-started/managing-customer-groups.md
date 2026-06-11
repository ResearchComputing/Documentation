# Managing User Access

## CU Boulder Users
CU Boulder user groups are managed through grouper.

> **Note:** Users must be logged in to the CU Boulder VPN to access Grouper.

### Adding Users

AWS customers can add team members as Administrators to their AWS account.
This is done using [CU's Grouper Tool](https://mygroups.colorado.edu/).
Note that changes can take up to 15 minutes to take effect.

1. Navigate to the Grouper Group for your AWS Account using one of the following methods:

   Method 1: Use the direct link that was sent to you in your welcome email to go directly to the group you wish to administer, and login using your [CU IdentiKey](https://oit.colorado.edu/services/identity-access-management/identikey).

   Method 2: Go to the [My Grouper Groups](https://mygroups.colorado.edu/grouper/grouperUi/app/UiV2Main.index?operation=UiV2MyGroups.myGroups) view in Grouper.
   Login using your [CU IdentiKey](https://oit.colorado.edu/services/identity-access-management/identikey).
   Filter for 'AWS' (if you can't find your group easily).
   You will see a list of groups that you can administer.
   Select the Group for your AWS Account.

   ```{image} images/managing-grouper-groups/my-grouper-groups.png
   :alt: The Grouper "My groups" page with the AWS filter applied
   ```

3. In the 'Members' tab view, click the "Add members" button.

   ```{image} images/managing-grouper-groups/add-members-button.png
   :alt: The Grouper "Add members" button
   ```

4. In the 'Member name or ID' field, enter the user's [CU IdentiKey](https://oit.colorado.edu/services/identity-access-management/identikey) and select the matching entry.

   ```{image} images/managing-grouper-groups/enter-identikey.png
   :alt: The Grouper dropdown box for selecting members to add to a group
   ```

5. Click the 'Add' button.

   ```{image} images/managing-grouper-groups/add-user.png
   :alt: The Grouper "Add" button for adding the selected member to a group
   ```

6. Verify the new user show up in the table.

   ```{image} images/managing-grouper-groups/verify-user.png
   :alt: The Grouper group membership page with a sample user circled in red
   ```

### Removing Users

Users can be removed from accessing the AWS account by removing them from the Grouper Group.

1. Login to the Grouper Group, as described above, using your [CU IdentiKey](https://oit.colorado.edu/services/identity-access-management/identikey).
2. In the 'Members' tab view, place a 'check' next to the user(s), and click the 'Remove selected members' button.

   ```{image} images/managing-grouper-groups/remove-user.png
   :alt: The Grouper group membership page with a sample user checked for removal
   ```

3. Verify the user(s) no longer appear in the table.

## Non CU Boulder Users
Non CU Boulder user groups are managed through [Microsoft Entra groups](https://portal.azure.com/#view/Microsoft_AAD_IAM/GroupsManagementMenuBlade/~/Overview).

### Your Group Name
The Entra group name to manage access to your AWS account is in the form '\<account-alias\>-CustomerAdmin'.
To find your account alias view the top right corner of the screen when logged into the AWS console.
   ```{image} images/managing-grouper-groups/alias.png
   :alt: AWS console top right corner showing the account alias identifier highlighted within a red square in the navigation bar
   ```


### Adding Users

AWS customers can add team members as Administrators to their AWS account.
This is done using AWS Entra Groups.
Note that changes can take up to 15 minutes to take effect.

The technical contact person is added as Owner of the Entra group and they will have access to add members to the group.

Refer to [Microsoft's Documentation](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-manage-groups#add-members-or-owners-of-a-group) to add members to groups.


### Removing Users
Users can be removed from accessing the AWS account by removing them from the Entra Group.

Refer to [Microsoft's Documentation](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-manage-groups#remove-members-or-owners-of-a-group) to remove members from groups.
