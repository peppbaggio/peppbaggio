## База "Theater"
[На Главную](../../README.md)

![diagram](Theater.drawio.svg)<br>
## Запросы
*   [Создание и заполнение таблиц](create.md)
*   [Выборки](select.md)

##   Описание базы
### Таблица *composer*<br>
Содержит список композиторов — авторов опер<br>
*   *Первичный ключ* **composer_id:** содержит id композитора
*   **composer_name:** фамилия и имя композитора

### Таблица *opera*<br>
Содержит список опер<br>
*   *Первичный ключ* **opera_id:** id оперы
*   **opera_title:** название оперы
*   *Внешний ключ* **composer_id:** id композитора
*   **cost:** стоимость постановки одного спектакля, без учета гонорара певцам
*   **is_staged:** идет ли в репертуаре театра (значения «0» или «1»)

### Таблица *opera_character*<br>
Содержит список оперных персонажей (партий). Заполняется из внешнего файла
*   *Первичный ключ* **character_id:** id оперного персонажа (партии)
*   **character_name:** имя персонажа
*   *Внешний ключ* **opera_id:** id оперы, к которой относится партия
*   *Внешний ключ* **voice_id:** id типа голоса, исполняющего партию

### Таблица *singer*<br>
Содержит список певцов в труппе театра. Заполняется из внешнего файла
*   *Первичный ключ* **singer_id:** id певца
*   **singer_name:** фамилия и инициалы певца
*   *Внешний ключ* **voice_id:** id типа голоса певца
*   *Внешний ключ* **rate_id:** id ставки гонорара за выход

### Таблица *voice*<br>
Содержит типы певческих голосов
*   *Первичный ключ* **voice_id:** id певческого голоса
*   **voice_type:** тип певческого голоса

### Таблица *rate*<br>
Содержит ставки гонораров за выход
*   *Первичный ключ* **rate_id:** id ставки гонорара
*   **rate_per_performance:** сумма за выход

### Таблица *role*<br>
Содержит список ролей в репертуаре певцов театра. Заполняется из внешнего файла
*   *Первичный ключ* **role_id:** id роли
*   *Внешний ключ* **singer_id:** id певца
*   *Внешний ключ* **character_id:** id оперной партии 

