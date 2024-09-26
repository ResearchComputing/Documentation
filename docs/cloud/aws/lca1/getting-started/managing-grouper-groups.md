# Managing User Access with Grouper

## Group Layout

Access to AWS LCA1 is driven by [CU's Grouper Tool](https://oit.colorado.edu/services/identity-access-management/enterprise-access-management). Each account and role combination is allocated a Grouper group. Members of that group will be allowed to log into AWS as that role.

Group names use the `<AWS account alias>-<Role>` format. For example, the group `awsucob0myaccount-MyRole` would allow members of that group to log into the `awsucob0myaccount` AWS account as the `MyRole` role.

The necessary groups will be created for you as part of your AWS onboarding, and you will be given the ability to add and remove users in your account. **It is your ongoing responsibility to ensure membership in this group accurately reflects the people who should have access to your AWS account.**

All access groups live in `Root -> Services -> Cloud Broker -> AWSLZA -> customer-access-groups`.

## Adding Users

AWS customers can add team members as Administrators to their AWS account. This is done using [CU's Grouper Tool](https://oit.colorado.edu/services/identity-access-management/enterprise-access-management). Note that changes can take up to 15 minutes to take effect.

1. Navigate to the Grouper Group for your AWS Account using one of the following methods:

   **Method 1:** Use the direct link that was sent to you in your welcome email to go directly to the group you wish to administer, and login using your [CU IdentiKey](https://oit.colorado.edu/services/identity-access-management/identikey).

   **Method 2:** Go to the [My Grouper Groups](https://mygroups.colorado.edu/grouper/grouperUi/app/UiV2Main.index?operation=UiV2MyGroups.myGroups) view in Grouper.
   Login using your [CU IdentiKey](https://oit.colorado.edu/services/identity-access-management/identikey). Filter for `AWS` (if you can't find your group easily). You will see a list of groups that you can administer. Select the Group for your AWS Account.

      ```{image} images/managing-grouper-groups/my-grouper-groups.png
      :alt: The Grouper "My groups" page with the AWS filter applied
      ```

3. In the "Members" tab view, click the "Add members" button.

   ```{image} images/managing-grouper-groups/add-members-button.png
   :alt: The Grouper "Add members" button
   ```

4. In the "Member name or ID" field, enter the user's [CU IdentiKey](https://oit.colorado.edu/services/identity-access-management/identikey) and select the matching entry.

   ```{image} images/managing-grouper-groups/enter-identikey.png
   :alt: The Grouper dropdown box for selecting members to add to a group
   ```

5. Click the "Add" button.

   ```{image} images/managing-grouper-groups/add-user.png
   :alt: The Grouper "Add" button for adding the selected member to a group
   ```

6. Verify the new user show up in the table.

   ```{image} images/managing-grouper-groups/verify-user.png
   :alt: The Grouper group membership page with a sample user circled in red
   ```

## Removing Users

Users can be removed from accessing the AWS account by removing them from the Grouper Group.

1. Login to the [Grouper Group](https://mygroups.colorado.edu/grouper/grouperUi/app/UiV2Main.index?operation=UiV2MyGroups.myGroups), as described above, using your [CU IdentiKey](https://oit.colorado.edu/services/identity-access-management/identikey).
2. In the "Members" tab view, place a check next to the user(s), and click the "Remove selected members" button.

   ```{image} images/managing-grouper-groups/remove-user.png
   :alt: The Grouper group membership page with a sample user checked for removal
   ```

3. Verify the user(s) no longer appear in the table.
