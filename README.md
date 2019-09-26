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

### Step 4 - Update the Region
1. Code line 23, update region, if necessary. If in the US changing this is not necessary. https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html
2. Click **Save**

```python
region_name="us-east-1"     #---- EDIT HERE, if necessary ------
```

### Step 5 - Add your important dates

1. Add your important dates by editing and copy and pasting the example. The event name, such as "Amy's Birthday" must be **unique**.  The year is irrelevant. They do not have to be in chronological order, but it sure helps for maintaining your list.

```python
    # --- EDIT HERE - ADD YOUR IMPORTANT DATES -----
    "May the Fourth be with you!": "1900-05-04",
    "Don't forget to get Amy an amazing gift": "1900-05-25",
    "Amy's Birthday": "1900-06-01",
    "Time to take over the world!": "1900-07-07",
    # --- END EDIT -----
```
2. Click **Save**

### Step 5 - Add your environment variable / phone number
1. In the **Key** input under Environment variables, type **PHONE_NUM**. Must be exact.
2. In the **Value** input enter your phone number.  For example, a U.S. phone number would appear as **+1XXX5550100**
3. Click **Save**

### Step 5 - Test Lambda Function
1. Click the **Test** button
2. Enter an **Event name**, such as "doNotFailMe". Template should be "Hello World".
2. Click **Create**.
3. Add a temporary event with today's date to test daily reminders.

```python
    # --- EDIT HERE - ADD YOUR IMPORTANT DATES -----
    "It works?": "1900-09-26",
    # --- END EDIT -----
```
4. Click **Save**
5. Click **Test**.  Execution Results at the bottom of screen should display **"statusCode": 200**. You should also have received your SMS message on the phone number provided.
6. Remove your temporary date and **Save**

#### Optional - Test monthly alerts
1. Locate the section of code for **MONTHLY REMINDERS** inside the lambda_handler function.

```python
def lambda_handler(event, context):
    
    # ---- MONTHLY REMINDERS ---------------
    # Loop through dictionary of events
    # Convert string date to a datetime object
    # Compare dictionary date to today's date
    # Executes on the first day of the month
    if today.day == 1:      # EDIT HERE TO TEST
```

2. Change the **1** to today's day of the month. For me, today is the 26th.

```python
if today.day == 26:   
```
3. Make sure you have 2 or more events taking place in the current month.  For me, it is September.

```python
    # --- EDIT HERE - ADD YOUR IMPORTANT DATES -----
    "Deadline for Evil Master Plan 2.4": "1900-09-10",
    "League of Villians Annual Meeting": "1900-09-26",
    "Cheat day: do something heroic!": "1900-09-29",
    # --- END EDIT -----
```

3. Click **Save**
4. Click **Test**. Execution Results at the bottom of screen should display **"statusCode": 200**. You should also have received your SMS message on the phone number provided.
5. Revert code to original value and **save**

```python
if today.day == 1:   
```

### Step 6 - Create Cloudwatch Event
1. In the Designer at the top of the top, click the **+ Add trigger** button
2. Click the dropdown and type **CloudWatch**. Select **CloudWatch Events**
3. In the Rule dropdown, select **Create a new rule**
4. Enter a **rule name**, such as "dailyMorningTrigger"
5. Ensure that **Schedule expression** is selected
6. In the **schedule expression** input your Cron expression. Copy and paste mine below or create your own. Mine triggers around 6:00 am for me, so take timezones into account. Adjust to your needs. cron(minute hour day-of-month month day-of-week year)

> cron(0 11 * * ? *)

##### Breakdown:
* 0 minutes
* 11 hour
* \* every day
* \* every month
* ? no specific day of the week
* \* every year

7. Click **Add**

