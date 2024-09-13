import requests
import configuration


# Запрос на получение всех объектов каталога
def get_all_objects():
    return requests.get(configuration.URL_SERVICE)


