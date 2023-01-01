import requests, os

#model_id = os.environ.get('be7269f8-7687-4c6d-b008-5524b09f1696')
#api_key = os.environ.get('m-eSBQW6IQYI2bZ1-TqMdTrsSgHbl-N1')

model_id = 'adf8fefc-6155-4b87-9e11-d10c8f93cc96'
api_key ='m-eSBQW6IQYI2bZ1-TqMdTrsSgHbl-N1'

url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/' + model_id + '/Train/'

querystring = {'modelId': model_id}

response = requests.request('POST', url, auth=requests.auth.HTTPBasicAuth(api_key, ''), params=querystring)

print(response.text)

print("\n\nNEXT RUN: python ./code/model-state.py")