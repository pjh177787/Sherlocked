import json
import requests

vision_api_key = '35c31f59e05b4879b12821be073d04f9'
vision_api_url = 'https://westus.api.cognitive.microsoft.com/vision/v1.0/analyze'

def WhatDoYouSee(body):
    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': vision_api_key,
    }
     
    params = {
        'visualFeatures': 'Description, Faces',
        'details': '',
        'language': 'en',
    }

    try:
        api_url = vision_api_url 
        response = requests.post(api_url, headers=headers, data=body, params=params)
        print ('Respose:')
        parsed = json.loads(response.text)
        if len(parsed) == 0:
            parsedText = 'I see nothing'
        parsedText = 'I see %s' % (parsed['description']['captions'][0]['text'])
        print (json.dumps(parsed, sort_keys=True, indent=2))
    except Exception as e:
        print('Error:')
        print(e)
        parsedText = e

    return parsedText
