## Configuring a budget action

You can attach budget actions to an alert for either a cost budget or a usage budget. To configure a budget action on a new budget, first follow the steps for <a href="https://docs.aws.amazon.com/cost-management/latest/userguide/create-cost-budget.html" target="_blank">Creating a cost budget</a>

---

### Creating a budget

1.	Sign in to the AWS Management Console and open the AWS Cost Management console at <a href="https://docs.aws.amazon.com/cost-management/latest/userguide/create-cost-budget.html" target="_blank">https://console.aws.amazon.com/cost-management/home</a>

2.	In the navigation pane, choose **Budgets**. (You may directly search for ‘budgets’ in top search bar)

3.	Click on ‘create budget’, choose Budget setup as ‘Customize(advanced)’ and Budget type as ‘Cost budget’
    ![](https://raw.githubusercontent.com/ResearchComputing/Documentation/master/docs/cloud/aws/budget-actions/images/1.png)

4.	Choose ‘Budget name’ of choice and ‘set budget amount’ to monthly with ‘Budget renewal type’ as ‘Recurring budget’. Choose ‘Start month’ and ‘Budgeting method’ as ‘Fixed’. And finally ‘Enter your budgeted amount’.
    ![](https://raw.githubusercontent.com/ResearchComputing/Documentation/master/docs/cloud/aws/budget-actions/images/2.png)

5.	Choose ‘Budget scope’ and select the services you would like in scope. For this example we will choose 'All AWS Services' and choose ‘Next’
    ![](https://raw.githubusercontent.com/ResearchComputing/Documentation/master/docs/cloud/aws/budget-actions/images/3.png)

To configure a budget action on an existing cost or usage budget, first follow the steps for <a href="https://docs.aws.amazon.com/cost-management/latest/userguide/create-cost-budget.html" target="_blank">Editing a budget.</a> Then, after you reach the **Configure alerts** step of creating or editing the budget, use the following procedure.


### To configure a budget action

1.	To configure a budget action on a new alert, choose **Add an alert threshold**. To configure a budget action on an existing alert, skip to step 7.
    ![](https://raw.githubusercontent.com/ResearchComputing/Documentation/master/docs/cloud/aws/budget-actions/images/4.png)

2.	Under Set **alert threshold**, for Threshold, enter the amount that needs to be reached for you to be notified. This can be either an absolute value or a percentage(choose using drop down). For example, say you have a budget of $200. To be notiﬁed at $160 (80% of your budget), enter 160 for an absolute budget or 80 for a percentage budget.

    Next to the amount, choose **Absolute value** to be notiﬁed when your costs exceed the threshold amount. Or, choose **% of budgeted amount** to be notiﬁed when your costs exceed the threshold percentage.

    Next to the threshold, choose **Actual** to create an alert for actual spend ‘Trigger’. Or, choose **Forecasted** to create an alert for forecasted spend.
    ![](https://raw.githubusercontent.com/ResearchComputing/Documentation/master/docs/cloud/aws/budget-actions/images/5.png)

3.	(Optional) Under **Notification preferences - Optional**, for **Email recipients**, enter the email addresses that you want the alert to notify. Separate multiple email addresses with commas. A notification can have up to 10 email addresses.

4.	(Optional) Under **Notification preferences - Optional**, for **Amazon SNS Alerts**, enter the Amazon Resource Name (ARN) for your Amazon SNS topic. For instructions on how to create a topic, see <a href="https://docs.aws.amazon.com/cost-management/latest/userguide/create-cost-budget.html" target="_blank">Creating an Amazon SNS topic for budget notifications.</a>

5.	  (Optional) Under **Notification preferences - Optional**, for **AWS Chatbot Alerts**, you can configure AWS Chatbot to send budget alerts to an Amazon Chime or Slack chat room. You configure these alerts through the AWS Chatbot console.

6.	 You may choose to add more alert thresholds for various actual amounts or various % of budgeted amounts. For instance, one alert for 80% and another for 100% of budgeted amount. Once configured, Choose Next.

7.	  For **Attach actions - Optional**, choose **Add Action.**
![](https://raw.githubusercontent.com/ResearchComputing/Documentation/master/docs/cloud/aws/budget-actions/images/6.png)
* For **Select IAM role**, choose an IAM role to allow AWS Budgets to perform an action on your behalf. It is recommended to use ‘Budget-role’ which has a Managed policy: AWSBudgetsActions_RolePolicyForResourceAdministrationWithSSM attached to it. 

* This managed policy is focused on specific actions that AWS Budgets takes on your behalf when completing a specific action. This policy gives permission to control AWS resources. For example, starts and stops Amazon EC2 or Amazon RDS instances by running AWS Systems Manager (SSM) scripts.

* For **Which action type should be applied when the budget threshold has been exceeded**, select the action that you want AWS Budgets to take on your behalf.You can choose from applying an IAM policy, attaching a service control policy (SCP), or targeting speciﬁc Amazon EC2 or Amazon RDS instances. You can apply multiple budget actions to a single alert. Only a management account can apply SCPs.

* If you want to choose ‘Automate instance to stop for EC2 or RDS’, choose related fields to select ‘region’ and ‘instances’ that you intend to stop.

* For **Do you want to automatically run this action when this threshold is exceeded**, choose **Yes** or **No**. If you choose No, then you run the action manually on the **Alert details page**. For instructions, see Reviewing and approving your budget action.

* For **How do you want to be alerted when this action is run, choose Use the same alert settings when you defined this threshold** or **Use different alert settings**. To use different alert settings, complete the **Notification preferences** specific to this action.
![](https://raw.githubusercontent.com/ResearchComputing/Documentation/master/docs/cloud/aws/budget-actions/images/7.png)



8.	Choose **Next**.

9.	Review your budget settings, and then choose **Create budget**.
    ![](https://raw.githubusercontent.com/ResearchComputing/Documentation/master/docs/cloud/aws/budget-actions/images/8.png)

    After you create an action, you can view its status from the AWS Budgets page on the **Actions** column. This column shows your configured actions count, actions waiting for your approval (**Requires approval**), and your successfully completed actions.
        ![](https://raw.githubusercontent.com/ResearchComputing/Documentation/master/docs/cloud/aws/budget-actions/images/9.png)

    Once a budget action is taken place, you get alerts based on the chosen notification preference. Below is a snippet of an email notification.
        ![](https://raw.githubusercontent.com/ResearchComputing/Documentation/master/docs/cloud/aws/budget-actions/images/10.png)
