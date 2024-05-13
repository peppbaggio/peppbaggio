## Запросы на [создание](#создание-таблиц) и [заполнение](#заполнение-таблиц) таблиц

### Создание таблиц
*   **Создание таблицы *voice***<br>
```sql
CREATE TABLE voice (
voice_id INT PRIMARY KEY AUTO_INCREMENT,
voice_type VARCHAR(100) NOT NULL
);
```

*   **Создание таблицы *rate***<br>
```sql
CREATE TABLE rate (
rate_id INT PRIMARY KEY AUTO_INCREMENT,
rate_per_performance DECIMAL(9, 2) NOT NULL
);
```

*   **Создание таблицы *composer***<br>
```sql
CREATE TABLE composer (
composer_id INT PRIMARY KEY AUTO_INCREMENT,
composer_name VARCHAR(255) NOT NULL
);
```

*   **Создание таблицы *opera***<br>
```sql
CREATE TABLE opera (
opera_id INT PRIMARY KEY AUTO_INCREMENT,
opera_title VARCHAR(255) NOT NULL,
composer_id INT,
cost DECIMAL(9, 2),
is_staged BOOLEAN DEFAULT(0) NOT NULL,
FOREIGN KEY (composer_id) REFERENCES composer(composer_id)
);
```

*   **Создание таблицы *opera_character***<br>
```sql
CREATE TABLE opera_character (
character_id INT PRIMARY KEY AUTO_INCREMENT,
character_name VARCHAR(255) NOT NULL,
opera_id INT NOT NULL,
voice_id INT NOT NULL,
FOREIGN KEY (opera_id) REFERENCES opera(opera_id),
FOREIGN KEY (voice_id) REFERENCES voice(voice_id)
);
```

*   **Создание таблицы *singer***<br>
```sql
CREATE TABLE singer (
singer_id INT PRIMARY KEY AUTO_INCREMENT,
singer_name VARCHAR(255) NOT NULL,
voice_id INT, 
rate_id INT,
FOREIGN KEY (voice_id) REFERENCES voice(voice_id),
FOREIGN KEY (rate_id) REFERENCES rate(rate_id)
);
```

*   **Создание таблицы *role***<br>
```sql
CREATE TABLE role (
role_id INT PRIMARY KEY AUTO_INCREMENT,
singer_id INT,
character_id INT NOT NULL,
FOREIGN KEY (singer_id) REFERENCES singer(singer_id),
FOREIGN KEY (character_id) REFERENCES opera_character(character_id)
);
```

### Заполнение таблиц
*   **Таблица *voice***<br>
```sql
INSERT INTO voice (voice_type) 
VALUES ('бас'), ('баритон'), ('тенор'), ('меццо-сопрано'), ('сопрано'), ('колоратурное сопрано'), ('тенор-альтино');
```
<details>
    <summary>Результат</summary>
    <img scr="https://www.google.com/imgres?q=ghj&imgurl=https%3A%2F%2Flookaside.fbsbx.com%2Flookaside%2Fcrawler%2Fmedia%2F%3Fmedia_id%3D100064023637928&imgrefurl=https%3A%2F%2Fm.facebook.com%2Fghjdesign%2F&docid=HU9EX1YJYt1sxM&tbnid=LeKX6oJ61NrtqM&vet=12ahUKEwiMg5-W2YuGAxX1LRAIHV0CDJMQM3oECBsQAA..i&w=1500&h=1500&hcb=2&ved=2ahUKEwiMg5-W2YuGAxX1LRAIHV0CDJMQM3oECBsQAA">
</details><br>


*   **Таблица *rate***<br>
```sql
INSERT INTO rate (rate_per_performance) 
VALUES (150000.00), (130000.00), (100000.00), (90000.00), (70000.00), (50000.00), (20000.00), (10000.00);
```
<details>
    <summary>Результат</summary>
    
</details><br>

*   **Таблица *composer***<br>
```sql
INSERT INTO composer (composer_name) 
VALUES ('Чайковский П. И.'), ('Верди Дж.'), ('Моцарт В. А.'), ('Римский-Корсаков Н. А.');
```
<details>
    <summary>Результат</summary>
    
</details><br>

*   **Таблица *opera***<br>
```sql
INSERT INTO opera (opera_title, composer_id, cost, is_staged)
VALUES ('Волшебная флейта', 3, 2900000.98, TRUE),
('Евгений Онегин', 1, 1800000.10, TRUE),
('Золотой петушок', 4, NULL, FALSE),
('Отелло', 2, 2300000.00, TRUE),
('Пиковая дама', 1, 1970000, TRUE),
('Травиата', 2, 1355000.00, TRUE),
('Фальстаф', 2, NULL, FALSE),
('Царская невеста', 4, 2100000.00, TRUE);
```
<details>
    <summary>Результат</summary>
    
</details><br>

*   **Таблица *opera_character***<br>
*Указать реальное расположение файла на локальном компьютере; в качестве разделителя столбцов используется значение по умолчанию — Tab*
```sql
LOAD DATA LOCAL INFILE 'opera_character.txt' 
INTO TABLE opera_character;
```
<details>
    <summary>Результат</summary>
    
</details><br>

*   **Таблица *singer***<br>
*Указать реальное расположение файла на локальном компьютере; в качестве разделителя столбцов используется значение по умолчанию — Tab*
```sql
LOAD DATA LOCAL INFILE 'singer.txt' 
INTO TABLE singer;
```
<details>
    <summary>Результат</summary>
    
</details><br>

*   **Таблица *role***<br>
*Указать реальное расположение файла на локальном компьютере; в качестве разделителя столбцов используется значение по умолчанию — Tab*
```sql
LOAD DATA LOCAL INFILE 'role.txt' 
INTO TABLE role;
```
<details>
    <summary>Результат</summary>
    
</details><br>
