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

# С помощью цикла проверить все возможные сочетания реальных типов запроса и значений параметра method
method_data = ["POST", "GET", "PUT", "DELETE"]
method_post = "POST"
method_get = "GET"
method_put = "PUT"
method_delete = "DELETE"
num_test = 0

# GET
for i in range(4):
    num_data = method_data[i]
    num_test += 1
    response_get = requests.get("https://playground.learnqa.ru/api/compare_query_type", params={"method": num_data})
    if response_get.text == '{"success":"!"}':
        print("Test All methods", num_test, "for method", method_get, "is Passed:", "Method in request:", num_data,
              response_get.status_code, response_get.text)
    else:
        print("Test All methods", num_test, "for method", method_get, "is Failed:", "Method in request:", num_data,
              response_get.status_code, response_get.text)
# POST
for i in range(4):
    num_data = method_data[i]
    num_test += 1
    response_get = requests.post("https://playground.learnqa.ru/api/compare_query_type", data={"method": num_data})
    if response_get.text == '{"success":"!"}':
        print("Test All methods", num_test, "for method", method_post, "is Passed:", "Method in request:", num_data,
              response_get.status_code, response_get.text)
    else:
        print("Test All methods", num_test, "for method", method_post, "is Failed:", "Method in request:", num_data,
              response_get.status_code, response_get.text)

# PUT
for i in range(4):
    num_data = method_data[i]
    num_test += 1
    response_get = requests.put("https://playground.learnqa.ru/api/compare_query_type", data={"method": num_data})
    if response_get.text == '{"success":"!"}':
        print("Test All methods", num_test, "for method", method_put, "is Passed:", "Method in request:", num_data,
              response_get.status_code, response_get.text)
    else:
        print("Test All methods", num_test, "for method", method_put, "is Failed:", "Method in request:", num_data,
              response_get.status_code, response_get.text)

# DELETE
for i in range(4):
    num_data = method_data[i]
    num_test += 1
    response_get = requests.delete("https://playground.learnqa.ru/api/compare_query_type", data={"method": num_data})
    if response_get.text == '{"success":"!"}':
        print("Test All methods", num_test, "for method", method_delete, "is Passed:", "Method in request:", num_data,
              response_get.status_code, response_get.text)
    else:
        print("Test All methods", num_test, "for method", method_delete, "is Failed:", "Method in request:", num_data,
              response_get.status_code, response_get.text)
