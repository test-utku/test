import requests

url = "http://212.132.64.73:4446/"
response = requests.get(url)

print(response.status_code)
print(response.text)
