import logging

import azure.functions as func
from textblob import TextBlob
import nltk
import os
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
    except ValueError:
        pass

    text = req_body['text']
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity    
    return func.HttpResponse(json.dumps(polarity),mimetype = 'application/json')