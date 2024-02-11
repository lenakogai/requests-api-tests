import requests

# С помощью цикла проверить все возможные сочетания реальных типов запроса и значений параметра method
method = {"POST", "GET", "PUT", "DELETE"}

# Method GET
for i in method:
    response_get = requests.get("https://playground.learnqa.ru/api/compare_query_type", params={"method": method})
    if response_get.text == '{"success":"!"}':
        print("Test4 for method GET is Passed:", "Method in request:", method, response_get.status_code, response_get.text)
    else:
        print("Test4 for method GET is Failed:", "Method in request:", method, response_get.request, response_get.status_code, response_get.text)

# Method POST
for i in method:
    response_post = requests.post("https://playground.learnqa.ru/api/compare_query_type", data={"method": method})
    if response_post.text == '{"success":"!"}':
        print("Test4 for method POST is Passed:", "Method in request:", method, response_post.status_code, response_post.text)
    else:
        print("Test4 for method POST is Failed:", "Method in request:", method, response_post.request, response_post.status_code, response_post.text)

# Method PUT
for i in method:
    response_put = requests.put("https://playground.learnqa.ru/api/compare_query_type", data={"method": method})
    if response_put.text == '{"success":"!"}':
        print("Test4 for method PUT is Passed:", "Method in request:", method, response_put.status_code, response_put.text)
    else:
        print("Test4 for method PUT is Failed:", "Method in request:", method, response_put.request, response_put.status_code, response_put.text)