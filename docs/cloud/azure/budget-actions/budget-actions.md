# Budget Actions

Cost control is a critical component to maximizing the value of your investment in the cloud. To configure a Budget and Budget actions in Azure, you'll complete the following actions by using the steps provided in each section. This document specifically outlines an example of how to setup a budget action to shutdown virtual machine when it meets the configured alert condition.

These actions included in this tutorial allow you to:

    1. Create an Azure Automation Account, Import relevant Runbook, which will use webhooks to stop VMs.
    2. If needed, Add role assignment to provide relevant access to the Automation account to perform operations on virtual machines.
    3. If haven't already,Create the budget with the wanted thresholds and wire it to the action group.
    4. Azure Monitor Action Group will be configured to trigger the Webhook when the budget threshold is met. This behaviour can be tested using 'Test action group'.

## Creating Azure Automation Account

1.	Sign in to the [Azure Management Console](https://portal.azure.com/#home) and search for **Automation accounts** on the top search bar. Click **Create** and choose the subscription that you intent to manage, A Resource Group to place the Automation account, Name and Region to host Automation account.

![Azure portal Create an Automation Account Basics tab with Subscription, Resource group, Automation account name, and Region fields.](images/1.png)

2.	Leave all other parameters to default. You may optionally choose to configure **Tags** as per your compliance standards. Click **Review+Create** and then click on **Create**.

![Azure portal Review + Create tab showing a Validation passed banner and a summary of Automation account settings.](images/2.png)

After the deployment finishes, open the new Automation account. The Overview page shows resource details such as resource group, location, subscription, and status.

![Azure portal Overview page for a newly created Automation account showing Essentials details and job statistics.](images/3.png)

3.	Once you are in your Automation Account, Click on **Runbooks** and click on **Browse Gallery** from the top pane.

![Azure Automation Runbooks page with Create a runbook, Import a runbook, and Browse gallery buttons.](images/4.png)

4.	Search for **Stop Azure V2 VMs** from the search bar. Make sure to choose **source** as **Github**. Click on Stop Azure V2 VMs graphical runbook.

![Azure Automation Browse Gallery search results for Stop Azure V2 VMs, showing a Graphical Runbook and a PowerShell Runbook.](images/5.png)

5.	Review the graphical flow to understand how this runbook will excute to stop all VMs at subscription or resource group level and then click on **Select** at the bottom.

![Azure Automation import page for the Stop Azure V2 VMs graphical runbook, including a flowchart of Connect AzAccount, Get VMs, Merge VMs, Stop VM, and notification steps.](images/6.png)

6. Name the runbook (for example, `Stop-VMs`) and select **Import**.

![Azure portal Import a runbook form with a runbook name field and an Import button.](images/7.png)

7. In the **Edit graphical runbook** pane, select **Publish**, then confirm by selecting **Yes**.

![Azure portal Edit graphical runbook pane with a Publish button in the toolbar.](images/8.png)

![Azure portal confirmation dialog asking whether to publish the runbook, with Yes and No buttons.](images/9.png)

## Add VM Contributor Role Assignment

1.	To check access level of the Automation account that you created, go to **Subscription** using top search bar and click on your subscription name. Then click on **Access control (IAM)** >> choose **check access** from top pane >> click on **check access**

![Azure portal Access control (IAM) Check access tab for a subscription, with View my access, Check access, and Add role assignment buttons.](images/9.1.png)

2.	Choose **Managed Identity** and choose your **subscription**. Under 'Managed Indentity' choose **Automation Accounts** and select your automation account. This will show you manually or auto assigned Role assignments for this automation account (if any). 

![Azure portal Check access pane with Managed Identity selected and filters for subscription and Automation Accounts.](images/9.2.png)

![Azure portal role assignments list for the selected Automation account managed identity.](images/9.3.png)

3.	In case you don't see any Role assignments, Click on **Add** in **Access Control (IAM)** blade of your subscription and choose **Add role assignment**.
In **Role** >> **Job function roles** >> search for **virtual machine contributor** and click on it. Then click **Next** to assign this role to our automation account.

![Azure portal Add role assignment page with the Role tab selected.](images/9.4.png)

![Azure portal Job function roles list with Virtual Machine Contributor selected.](images/9.5.png)


4.	Choose **Managed Identity** radio button, click on **select members** to select your automation account. Once your clicked on **select**, click on **Review+Assign**.

![Azure portal Add role assignment Members tab with Managed identity selected and a Select members button.](images/9.6.png)

## Create Budget and Action Group

1. Open your subscription and, under **Cost Management**, select **Budgets**. Select **Add** to create a new budget.

![Azure portal Budgets page for a subscription, with an Add button and an empty budgets table.](images/10.png)

2. Enter a budget name and choose a **Reset period** (this example uses monthly). You can leave the creation and expiration dates at their defaults. Enter the total budget **Amount**, then select **Next**.

![Azure portal Create a budget form with name, reset period, date range, and amount fields.](images/11.png)

3. In **Set alerts** tab, click on **Manage action group**. Click **Create** to create a new action group.

![Azure portal Set alerts tab with a Manage action group link.](images/12.png)

![Azure portal Action groups page with a Create button for a new action group.](images/13.png)

4. On the **Basics** tab, choose the subscription and resource group, set **Region** to **Global**, and enter an action group name and a display name (the display name is limited to 12 characters). Select **Next: Notifications**.

![Azure portal Create action group Basics tab with subscription, resource group, region, action group name, and display name fields.](images/14.png)

5. Under **Notification type**, select **Email/SMS message/Push/Voice**, choose the notification method you want (this example uses email), enter the recipient address, then select **OK**. Name the notification, then select **Next: Actions**.

![Azure portal Create action group Notifications tab with Email, SMS, Push, and Voice notification options.](images/15.png)

![Azure portal Notifications tab after an email notification has been named.](images/16.png)

6. Under **Actions**, set **Action type** to **Automation Runbook**. Configure the runbook as follows:

   - **Run runbook:** Enabled
   - **Runbook source:** User
   - **Subscription:** the subscription you are managing
   - **Automation account:** the Automation account you created
   - **Runbook:** the imported Stop VMs runbook

   Select **Configure parameters**. **Subscription** is the only required parameter. Leave resource group blank to apply the action at subscription scope, or enter a resource group name to limit the action to that group. Select **OK** as needed, name the action, then select **Review + create** and **Create**.


![Azure portal Create action group Actions tab with Automation Runbook selected and a Configure Runbook pane listing subscription, Automation account, and runbook.](images/17.png)

![Azure portal Configure parameters form for the Automation runbook webhook.](images/18.png)

![Azure portal runbook parameters with Subscription filled in as the required field.](images/19.png)

![Azure portal Actions tab with the Automation Runbook action named.](images/20.png)

![Azure portal Create action group Review + create tab summarizing basics, notifications, and actions.](images/21.png)

7. Once you are back on **Action Groups** page, give it 10-20 seconds for the new Action group to show up. Click on **Refresh** if needed. Once you see your Action group, carefully click on Red **X** at the top right corner, only Once, to come back to **Create Budget** pane.

![Azure portal Action groups list showing the newly created action group, with a close control in the upper-right corner.](images/24.png)

8. After the action group is created, Azure sends a confirmation email to the notification recipient. The message is from `azure-noreply@microsoft.com` and states that the recipient has been added to the action group. It includes the resource group name and action group name.

```{note}
Add `azure-noreply@microsoft.com` to your email allow list so budget and action-group messages are not delivered to spam.
```

![Email from Microsoft Azure stating the recipient has been added to an Azure Monitor action group, including resource group and action group names.](images/22.png)

9. On **Create Budget** pane, configure **alert conditions** as needed, I chose to not perform any action for 80% and enforce budget action when my budget hits 100% utilization, in this example. Make sure to select the action group which you have created in previous step. Click **Create** in the bottom, once you have filled all relevant fields as per below screenshot. In the next section, we will test this action group if it really works.

![Azure portal Create budget Set alerts tab with 80 percent and 100 percent actual-spend thresholds and an action group selected at 100 percent.](images/25.png)

## Test Azure Monitor Action Group

```{warning}
Testing an action group that is configured to stop VMs will stop those VMs. Use a test resource group, and make sure the runbook webhook is scoped to that resource group if you do not want subscription-wide impact.
```

1. Search for **Monitor** in the top search bar. Open **Monitor**, select **Alerts**, then select **Action groups** in the toolbar.

![Azure Monitor Alerts page with the Action groups option selected in the toolbar.](images/26.png)

2. In the Action groups list, select the checkbox next to the action group you created, then select **Test action group**.

![Azure portal Action groups list with one action group selected and a Test action group button.](images/27.png)

3. Leave the default notification and action tests selected. For **Select sample type**, choose **Cost budget alert**. This sends a test email and fires the webhook to stop VMs in the configured subscription or resource group.

![Azure portal Test action group pane with Cost budget alert selected as the sample type.](images/28.png)

4. When the test finishes, the portal shows a success or failure status. Open **Virtual machines** to confirm that the test VMs are in a deallocated state.

![Azure portal test result showing whether the action group notification and action tests succeeded or failed.](images/29.png)

5. If the email notification test succeeds, you receive a message confirming that a test alert was sent for the action group.

![Email from Microsoft Azure confirming a successful test of an Azure Monitor action group notification.](images/30.png)
