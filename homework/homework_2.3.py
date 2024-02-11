import requests

# Сделать http-запрос любого типа без параметра method, описать, что будет выводиться в этом случае
response1 = requests.get("https://playground.learnqa.ru/api/compare_query_type")
# Вернет "Wrong method provided"
if response1.text == "Wrong method provided":
    print("Test1 is Passed:", response1.status_code, response1.text)
else:
    print("Test1 is Failed", response1.status_code, response1.text)

# Сделать http-запрос не из списка. Например, HEAD. Описать, что будет выводиться в этом случае
response2 = requests.options("https://playground.learnqa.ru/api/compare_query_type", data={"method": "POST"})
# Вернет "Wrong HTTP method"
if response2.text == "Wrong HTTP method":
    print("Test2 is Passed:", response2.status_code, response2.text)
else:
    print("Test2 is Failed", response2.status_code, response2.text)

# Сделать запрос с правильным значением method. Описать, что будет выводиться в этом случае
response3 = requests.put("https://playground.learnqa.ru/api/compare_query_type", data={"method": "PUT"})
# Вернет {"success":"!"}
if response3.text == '{"success":"!"}':
    print("Test3 is Passed:", response3.status_code, response3.text)
else:
    print("Test3 is Failed", response3.status_code, response3.text)