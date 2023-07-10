import requests

'''создание класса получения всех категорий шуток'''
class TestHumor:
    def test_humor(self):
        url = 'https://api.chucknorris.io/jokes/categories'
        check_status_code = requests.get(url).status_code #проверка статус-кода ответа на запрос получения всех категорий шуток
        categories = requests.get(url).json() #1.Отправить запрос для получения всех категорий
        print(check_status_code)
        assert  check_status_code == 200 #3.Добавить в код комментарии, аннотации, print, проверки на статус код для лучшей читаемости кода

        return categories


categories = TestHumor() #создание экземпляра класса
print(categories.test_humor()) #вывод всех категорий в массиве для проверки


def get_jokes_every_category():  #4.У вас не должно быть "портянки" - то есть длинного кода с 17 запросами, минимизируйте количество строк (не в ущерб 3 пункту)
    for i in categories.test_humor():
        print(requests.get(f'https://api.chucknorris.io/jokes/random?category={i}').json()['value'])

get_jokes_every_category() #2.Получить 1 шутку по каждой из категорий (16 шт) - всего 16 шуток
