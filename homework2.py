import requests

url = 'https://api.chucknorris.io/jokes/categories'

desired_category = input('Алекс, введи желаемую категорию шутки про Чака Норриса: ') #1.Запросить у пользователя категорию, на которую он хочет получить шутку (не сами сохранить в переменную, а через input() и ввести в терминале

list_categories = requests.get(url).json() #2.Отправить запрос для получения всех категорий

check_status_code = requests.get(url).status_code
assert  check_status_code == 200, 'пришел ответ, отличный от 200, необходимо дебажить' #проверка статус-кода

print(list_categories)  '''печать всех категорий шуток'''

assert desired_category in list_categories, 'Желаемой категории в списке нет' #3.убедиться что данная категория (из пункта 1) есть в ответе запроса (отправленного в пункте 2)
desired_joke = requests.get(f'https://api.chucknorris.io/jokes/random?category={desired_category}').json()['value']  #4.Отправить запрос для получения шутки, которую запросил пользователь

print(desired_joke) #печать шутки для пользователя