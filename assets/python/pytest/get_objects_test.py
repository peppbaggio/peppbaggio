import get_object_requests

#Проверка ответа на запрос GET https://api.restful-api.dev/objects
#на получение всех объектов каталога

response_all = get_object_requests.get_all_objects()
json_data_all = response_all.json()


# Проверка кода ответа
def test_get_all_objects_statuscode():
    assert response_all.status_code == 200, ("Ошибка: ожидался код 200, "
                                         "пришел код ") + str(response_all.status_code)

# Проверка типа данных в теле ответа (список)
def test_get_all_objects_body_structure():
    assert type(json_data_all) == list, ("Ошибка: ожидался тип list")

# Проверка выборочных элементов (первого и последнего)
# на тип (словарь)
def test_get_all_objects_elements_type():
    assert type(json_data_all[0]) == dict, "У первого элемента ожидался тип dict"
    assert type(json_data_all[len(json_data_all)-1]) == dict, "У последнего элемента ожидался тип dict"

# Проверка наличия обязательных ключей (id, name, data)
# в первом и последнем элементах
def test_get_all_objects_elements_keys():
    assert "id" in json_data_all[0], "В первом элементе нет ключа id"
    assert "name" in json_data_all[0], "В первом элементе нет ключа name"
    assert "data" in json_data_all[0], "В первом элементе нет ключа data"
    assert "id" in json_data_all[len(json_data_all)-1], "В первом элементе нет ключа id"
    assert "name" in json_data_all[len(json_data_all)-1], "В первом элементе нет ключа name"
    assert "data" in json_data_all[len(json_data_all)-1], "В первом элементе нет ключа data"

