import json
import pandas as pd
import requests
import numpy as np


def lambda_handler(event, context):
    # TODO implement

    base_site ='https://www.microsoft.com/en-us/trainingdays'
    r = requests.get(base_site)

    table = pd.read_html(r.text,match = 'Security')

    df = table[0]

    output_date = list(df['Date'])

    output_name = list(df['Event Name'])


    responsehttp = {}

    responsehttp = output_name,output_date





    return {
        'statusCode': 200,
        'body': json.dumps(responsehttp)
    }
