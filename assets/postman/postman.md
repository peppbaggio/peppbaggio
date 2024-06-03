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
*   *   [get_icorrect_list_id](get_incorrect_list_id.csv)
*   *   [get_incorrect_id](get_incorrect_id.csv)
*   *   [add_name_incorrect](add_name_incorrect.csv)
*   *   [add_data_incorrect](add_data_incorrect.csv)