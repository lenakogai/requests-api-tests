import requests

payload = {"name": "Tester"}
response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
print(response.text)