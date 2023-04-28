import os
import json
import requests
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
headers = {'X-Api-Key': API_TOKEN}

temp = {"domain": "", "expires": ""}
list = []


with open('domains.json') as f:
	templates = json.load(f)
	for i in templates:
		domain = domain=i["label"]
		api_url = 'https://api.api-ninjas.com/v1/whois?domain={}'.format(domain)
		response = requests.get(api_url, headers=headers)
		res = response.json()
		date = int(res['expiration_date'])
		date = datetime.utcfromtimestamp(date).strftime('%Y-%m-%d')
		result = temp.copy()
		result.update(domain=res['domain_name'], expires=date)
		list.append(result)
		print(result)


with open("output.json", "w")as f:
	f.write(json.dumps(list, indent=2))

