import get_object_requests

response_id_correct = get_object_requests.get_object_with_id()
json_data_id_correct = response_id_correct.json()


# Проверяем код ответа
def test_get_object_with_id_correct_status_code():
    assert response_id_correct.status_code == 200, ("Ошибка: Ожидался код 200, "
                                                    "пришел код: " + str(response_id_correct.status_code))


# Проверяем структуру тела ответа (список)
def test_get_object_with_id_correct_structure():
    assert type(json_data_id_correct) == list, ("Ошибка: Ожидался тип список, "
                                                "пришел тип: " + str(type(json_data_id_correct)))


# Проверяем тип элемента (словарь)
def test_get_object_with_id_correct_element_type():
    assert type(json_data_id_correct[0]) == dict, ("Ошибка: Ожидался тип словарь, "
                                                "пришел тип: " + str(type(json_data_id_correct)))


# Проверяем, что у объекта есть обязательные ключи (id, name, data)
def test_get_object_with_id_correct_element_keys():
    assert "id" in json_data_id_correct[0], "В элементе нет ключа id"
    assert "name" in json_data_id_correct[0], "В элементе нет ключа name"
    assert "data" in json_data_id_correct[0], "В элементе нет ключа data"


# Проверяем, что ID объекта соответствует ID в параметрах запроса
def test_get_object_with_id_correct_element_id():
    assert json_data_id_correct[0].get("id") == get_object_requests.first_id, ("Ошибка: ID объекта"
                                                                               "не соответствует ID в параметрах GET-запроса")

