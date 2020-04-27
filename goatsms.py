from twilio.rest import Client
import os
from random import randint
import boto3

# Your Account Sid and Auth Token from twilio.com/console
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

def change_time():
    value = randint(17,24)
    schedule = 'cron(0 ' + str(value) + ' * * ? *)'
    sched = boto3.client('events')
    sched.put_rule(
        Name='goattime',
        ScheduleExpression=schedule,
    )
    return schedule

def lambda_handler(event, context):
    ret = ''
    numbers = ["****","****","****"]
    for number in numbers:
        message = client.messages \
            .create(
                body="\n-\n- \n \nA goat!!! \n\n- From your friendly, neighborhood Savvy",
                from_="+11111111111",
                media_url=["https://placegoat.com/200/200"],
                to=number
            )
        ret += message.sid + ' '
    return change_time()
