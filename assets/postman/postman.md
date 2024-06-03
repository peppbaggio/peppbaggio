## Тестирование API-запросов сервера [RESTFULL-API](https://restful-api.dev/)
[На Главную](../../README.md)

Требования и ограничения полей отсутствуют<br>
При работе приняты следующие ограничения:<br>
*   Обязательный ключ name (строковый или числовой)
*   Обязательный ключ data (объект)
*   Автоназначаемый сервером ключ id (строковый тип; допускает буквы, цифры, дефис)

**Файлы**<br>
*   [Postman-коллекция запросов](Restful-API.postman_collection.json)
*   **Data-файлы для автотестов:**<br>
*   *   [get_incorrect_list_id](get_incorrect_list_id.csv)
*   *   [get_single_object_incorrect_id](get_single_object_incorrect_id.csv)
*   *   [add_new_object_incorrect_name](add_new_object_incorrect_name.csv)
*   *   [add_new_object_incorrect_data](add_new_object_incorrect_data.csv)