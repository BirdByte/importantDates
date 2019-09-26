# Important Dates SMS Reminder

This is a serverless application using Amazon Web Services (AWS).  A time-based CloudWatch event triggers the Lambda Function to run once a day.  On the first day of every month an SMS is sent with all important dates for the month; a daily SMS is sent for any important events on that date.

Whether you have any knowledge of AWS or coding, this documentation written with the intention to provide everything you need to implement this application.

>**Level:** Beginner

>**Cost:** Free Tier.

*Disclaimer:* I do not claim to be an expert. This is my first AWS project and my first time using Python.

<p align="center">
  <img src="/images/diagram.PNG"/>
</p>

## Pricing
While this project alone is unlikely to exceed free tier you should know your boundaries, and the cost to you if you exceeded those limits.

> Lambda - https://aws.amazon.com/lambda/pricing/

> SNS - https://aws.amazon.com/sns/pricing/

> CloudWatch - https://aws.amazon.com/cloudwatch/pricing/


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
AWS requires that we grant services permission to talk to each other.  You are creating a role that will allow Lambda to interact with CloudWatch and SNS. We will follow the rule of least privilage by only giving SNS publishing permissions.

1. In the **Find Services** input box, type “IAM” and press Enter
2. Select **Roles** on the left
3. Select **Create role** button
4. Ensure **AWS service** box is selected
5. Under Choose the service that will use this role, select **Lambda**
6. Select **Next:Permissions**
7. In the **Filter Policies** input, type “AWSLambdaBasic”.
8. Select the AWS Managed Policy **AWSLambdaBasicExecutionRole**. This gives permission for Lambda to write log files to CloudWatch.
9. Select **Next: Tags**
10. Select **Next: Review**
11. Input a **Role Name**, such as "myLambdaSNSRole" and select **Create Role**
12. Select the newly created role from the list by clicking on the role name
13. Select **Add inline policy**
14. Select **JSON** tab and **delete** all contents.
15. Open the **role.txt** in GitHub. Copy and paste the contents into the JSON text area. This gives your Lambda function permission to publish to SNS.
16. Select **Review Policy**
17. Enter a **Name**, such as "mySNSPublishOnlyPolicy"
18. Select **Create policy**

### Step 3 - Create Lambda Function
1. Select the **Services** dropdown in the navigation bar
2. In the **Find Services** input box, type “Lambda” and press Enter
3. Click the **Create Function** button
4. Ensure that **Author from scratch** is selected on the Create Function page
5. Input a **function name**, such as “importantDates”
6. In the **Runtime** dropdown, select “Python 3.7”.
7. Click **Choose or create an execution role** to expand
8. Select **Use an existing role**
9. In the **existing role** enter your **IAM role name**, such as "myLambdaSNSRole"
10. Click **Create function**. This may take some time to complete.
11. Scroll down to the code editor.  Delete the contents.  Copy and paste the contents from the **importantDates.py** file in Github into the editor
12. Click **Save**

### Step 4 - Update the Lambda Function
1. Code line 23, update region, if necessary. If in the US changing this is not necessary. https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html

```python
region_name="us-east-1"     #---- EDIT HERE, if necessary ------
```

2. Code line 33, add your important dates by editing and copy and pasting the example. The event name, such as "Amy's Birthday" must be **unique**.  The year is irrelevant.

```python
    # --- EDIT HERE - ADD YOUR IMPORTANT DATES -----
    "May the Fourth be with you!": "1900-05-04",
    "Don't forget to get Amy an amazing gift": "1900-05-25",
    "Amy's Birthday": "1900-06-01",
    "Time to take over the world!": "1900-07-07",
    # --- END EDIT -----
```


### Step 5 - Test Lambda Function

### Step 6 - Create Cloudwatch Event

