import requests

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
        print("Test All methods", num_test, "for method", method_get, "is Passed:", "Method in request:", num_data, response_get.status_code, response_get.text)
    else:
        print("Test All methods", num_test, "or method", method_get, "is Failed:", "Method in request:", num_data, response_get.status_code, response_get.text)
# POST
for i in range(4):
    num_data = method_data[i]
    num_test += 1
    response_get = requests.post("https://playground.learnqa.ru/api/compare_query_type", data={"method": num_data})
    if response_get.text == '{"success":"!"}':
        print("Test", num_test, "for method", method_post, "is Passed:", "Method in request:", num_data, response_get.status_code, response_get.text)
    else:
        print("Test", num_test, "or method", method_post, "is Failed:", "Method in request:", num_data, response_get.status_code, response_get.text)

# PUT
for i in range(4):
    num_data = method_data[i]
    num_test += 1
    response_get = requests.put("https://playground.learnqa.ru/api/compare_query_type", data={"method": num_data})
    if response_get.text == '{"success":"!"}':
        print("Test", num_test, "for method", method_put, "is Passed:", "Method in request:", num_data, response_get.status_code, response_get.text)
    else:
        print("Test", num_test, "or method", method_put, "is Failed:", "Method in request:", num_data, response_get.status_code, response_get.text)

# DELETE
for i in range(4):
    num_data = method_data[i]
    num_test += 1
    response_get = requests.delete("https://playground.learnqa.ru/api/compare_query_type", data={"method": num_data})
    if response_get.text == '{"success":"!"}':
        print("Test", num_test, "for method", method_delete, "is Passed:", "Method in request:", num_data, response_get.status_code, response_get.text)
    else:
        print("Test", num_test, "or method", method_delete, "is Failed:", "Method in request:", num_data, response_get.status_code, response_get.text)