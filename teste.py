import requests

# url = 'https://services.onetcenter.org/ws/mnm/interestprofiler/questions'
# headers = {'Authorization': 'Basic d2VtYXA6NjYyM2p4cA==',
#            'Accept': 'application/json'}

# response = requests.get(url, headers=headers)

# print(response.status_code)
# print(response.text)
# print(response.json())

url = 'https://services.onetcenter.org/ws/mnm/interestprofiler/results?answers=553421321134342523523523254115342111351145453111231155343444'
headers = {'Authorization': 'Basic d2VtYXA6NjYyM2p4cA==',
           'Accept': 'application/json'}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.text)
# print(response.json())
