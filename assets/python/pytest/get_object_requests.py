import requests
import configuration


# Запрос на получение всех объектов каталога
def get_all_objects():
    return requests.get(configuration.URL_SERVICE)

# ID существующего объекта
json_data = get_all_objects().json()
first_id = json_data[0].get('id')

# Запрос на получение объекта по ID

def get_object_with_id():
    # Передаем его в параметрах пути GET-запроса
    return requests.get(configuration.URL_SERVICE, params=first_id)




