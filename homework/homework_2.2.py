import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
# Необходимо узнать сколько редиректов происходит от изначальной точки назначения до итоговой. И какой URL итоговый

first_url = response.history[0]
second_url = response.history[1]

print("All redirects:", response.history)
print("First redirect:", first_url.status_code, first_url.url)
print("Second redirect:", second_url.status_code, second_url.url)
print("Final URL:", response.url)
