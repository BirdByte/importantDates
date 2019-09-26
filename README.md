# Important Dates SMS Reminder

This is a serverless application using Amazon Web Services (AWS).  A time-based CloudWatch event triggers the Lambda Function to run once a day.  On the first day of every month an SMS is sent with all important dates for the month; a daily SMS is sent for any important events on that date.

Whether you have any knowledge of AWS or coding, this documentation written with the intention to provide everything you need to implement this application.

>**Level:** Beginner

>**Cost:** Free Tier

*Disclaimer:* I do not claim to be an expert. This is my first AWS project and my first time using Python.

<p align="center">
  <img src="/images/diagram.PNG"/>
</p>


## --------------- Tutorial in progress --------------------

### Step 1 - Create an AWS Account, if necessary
While this project stays within the free tier account provided by AWS, you will still need to enter **credit card** information to complete the account sign-up.

1. Visit https://aws.amazon.com/
2. Click **Create an AWS Account**
3. Fill out information and select **Continue**
4. Select **Personal** as Account Type and fill in remaining details
5. Click **Create Account and Continue**
6. Add a payment method
7. Complete Confirm your Identity through SMS or Voice call
8. Select **Free** support plan
9. **Sign in** to the console

### Step 2 - Create IAM Role
1. In the **Find Services** input box, type “IAM” and press Enter
2. Select **Roles** on the left
3. Select **Create role** button
4. Ensure **AWS service** box is selected
5. Under choose the service that wilol use this role, select **Lambda**
6. Select **Next:Permissions**
7. In the **Filter Policies** input, type “AWSLambdaBasic”.
8. Select the AWS Managed Policy **AWSLambdaBasicExecutionRole**. This gives permission for Lambda to write log files to CloudWatch.
9. Select **Next: Tags**
10. Select **Next: Review**
11. Input a **Role Name** and select **Create Role**
12. Select the newly created role from the list.
13. Select **Attach policies**
14. Select **JSON** tab.
15. Open the role.txt in GitHub. Copy and paste the contents into the JSON text area. This gives your Lambda function permission to publish to SNS, this following the rule of least permissions.
16. Select **Review Policy**
17. .... in progress


### Step 3 - Create Lambda Function

### Step 4 - Test Lambda Function

### Step 5 - Create Cloudwatch Event

