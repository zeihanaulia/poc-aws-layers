import json
import requests
from src.postgres.postgres import (Database)
import os

def hello(event, context):

    r = requests.get("https://api.github.com/")

    dbstr = os.environ["db_string"]

    resp = Database(dbstr)
    print(resp)

    body = {
        "github": r.text,
        "connection": resp,
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
