import datetime
import logging
import boto3
import requests
import os
import json
from datetime import date

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def run(event, context):
    logger.info("Starting to collect AWS Cost data")
    client = boto3.client('ce')
    haurl = os.getenv('HASS_WEBHOOK_URL')
    response = client.get_cost_and_usage(
        TimePeriod={
            'Start': str(date.today().replace(day=1)),
            'End': str(date.today())
        },
        Granularity='MONTHLY',
        Metrics=[
            'AmortizedCost'
        ],
        Filter = { 
                'Not': { 
                    'Dimensions': {
                        'Key': "RECORD_TYPE",
                        'Values': ["Refund", "Credit"]
                    }
                },
            },
    )

    totalCost = response["ResultsByTime"][0]["Total"]["AmortizedCost"]
    headers = {'Content-type': 'application/json'}

    r = requests.put(haurl, json=totalCost)
    logger.debug("Got data : " + json.dumps(totalCost))
    logger.info("Function done")
