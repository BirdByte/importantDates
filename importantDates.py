# This script sends reminder texts for important dates, like anniversaries
# or birthdays, to your phone using Amazon Web Services.
# 
# This script sends a monthly reminder on the first day of the month with 
# all events for that month.  It sends daily reminders on the day of event.
#
# Uses Amazon SNS without topics, AWS Lambda, Cloudwatch Events, and Python.
#
# Created By: Amy B. / BirdByte
# Created On: September 9, 2019

import boto3        # AWS SDK for Python
import logging      # Detailed logging for CloudWatch
import datetime     # Module to create and manipulate date objects
import os           # Allows use of environment variable

# Initialize logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize SNS client
session = boto3.Session(
    region_name="us-east-1"     #---- EDIT HERE, if necessary ------
)
sns_client = session.client('sns')

# Python Dictionary {"key": "value"}
# Note: Best practice would be to store data in a file inside S3 or database.
# Date Format: YYYY-MM-DD -- note: year only for formatting purposes
# Event name / key must be unique.
importantDates = {
    # --- EDIT HERE - ADD YOUR IMPORTANT DATES -----
    "Amy's Birthday": "1900-06-01",
    # --- END EDIT -----
}

today = datetime.date.today()
eventList = []
eventListMonthly = []
alertMsg = ""

def lambda_handler(event, context):
    
    # ---- MONTHLY REMINDERS ---------------
    # Loop through dictionary of events
    # Convert string date to a datetime object
    # Compare dictionary date to today's date
    # Executes on the first day of the month
    if today.day == 18:
        print('EXECUTING MONTHLY REMINDERS')
        for eventName, eventDate in importantDates.items():
            eventDateConverted = datetime.datetime.strptime(eventDate, "%Y-%m-%d")   
            if eventDateConverted.month == today.month:
                eventListMonthly.append(eventName + " on " + datetime.datetime.strftime(eventDateConverted, "%m-%d"))
    
    # ---- DAILY REMINDERS -----------------
    for eventName, eventDate in importantDates.items():
        eventDateConverted = datetime.datetime.strptime(eventDate, "%Y-%m-%d")   
        if eventDateConverted.day == today.day and eventDateConverted.month == today.month:
            eventList.append(eventName)
    
    # ---- CREATE MESSAGE -------
    
    # Monthly Message
    if eventListMonthly:
        alertMsg = datetime.datetime.strftime(today, '%B') + " Events: " +  ', '.join(eventListMonthly) + ". "
 
    # Daily Message; combine daily and monthly messages, if necessary
    if eventList:
        if eventListMonthly:
            alertMsg = alertMsg + "Today\'s Events: " + ', '.join(eventList)
        else:
            alertMsg = "Today\'s Events: " + ', '.join(eventList)
    
    # ---- SEND MESSAGE -----
    if alertMsg:

        response = sns_client.publish(
            
            PhoneNumber = os.environ["PHONE_NUM"],
            Message = alertMsg,
            
            # Note: By default, messages set as "Promotional", which are
            # non-critical and meant to be lowest cost. Set message attributes 
            # to "Transactional" for critical tasks and high reliability.
            
        )
        
    logger.info(response)

    return {
        'statusCode': 200,
    }
