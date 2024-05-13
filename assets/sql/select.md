# Выборки из таблиц
*   *Вывести список певцов, в чьем репертуаре есть партия Гремина, сортировать по убыванию гонорара.*
```sql
SELECT character_name, singer_name, rate_per_performance FROM singer
JOIN rate USING(rate_id)
JOIN role USING(singer_id)
JOIN opera_character USING(character_id)
WHERE character_name = 'Гремин'
ORDER BY rate_per_performance DESC, singer_name ASC;
```
<details>
    <summary>Результат</summary>
</details><br>

*   *Вывести список опер, которые не могут быть поставлены силами театра (opera.is_staged = 0), список партий из этих опер, которых нет в репертуаре певцев с указанием типа голоса, и список певцов труппы с подходящими голосами (или прочерк, если таких пецов нет)*
```sql
WITH 
    not_staged AS 
    (SELECT opera_title, opera_id FROM opera WHERE is_staged = 0),
    no_singers AS 
    (SELECT opera_title, character_id, character_name, voice_id, voice_type FROM opera_character 
    JOIN not_staged USING(opera_id) 
    JOIN voice USING(voice_id) 
    WHERE character_id NOT IN (SELECT character_id FROM role) 
    ORDER BY opera_title)
SELECT opera_title, character_name, voice_type, 
CASE 
WHEN voice_id IN (SELECT voice_id FROM singer) THEN singer_name 
ELSE '—' 
END AS singer_name 
FROM no_singers LEFT JOIN singer USING(voice_id) 
ORDER BY opera_title, character_name, singer_name;
```
<details>
    <summary>Результат</summary>
</details><br>

*   *Увольняется Й. Марини. Вывести оперы, которые теперь невозможно исполнять, вместе с партиями для соответствующего голоса. Здесь два запроса: вывести партии, для которых Марини — единственный исполнитель; вычислить количество певиц с ее типом голоса в труппе и вывести оперы, в которых требуют участия сразу всех певицы с этим типом голоса*
```sql
WITH 
/* id певца и голоса певицы "Марини Й." */
marini AS (
    SELECT singer_id, voice_id FROM singer WHERE singer_name = 'Марини Й.'), 
/* оперы с этим типом голоса */
mezzo_opera AS ( 
    SELECT DISTINCT character_id, opera_id FROM opera_character WHERE voice_id = (SELECT voice_id FROM marini)),
/* количество певцов с этим типом голоса в труппе */
mezzo_count AS (
    SELECT COUNT(singer_id) AS singer_count FROM singer WHERE voice_id = (SELECT voice_id FROM marini)),
/* количество занятых меццо-сопрано по операм; оконная функция нужна, чтобы сохранить названия всех партий */
some_mezzo AS (
    SELECT character_id, opera_id, COUNT(character_id) OVER (PARTITION BY opera_id) AS character_count FROM opera_character WHERE voice_id = (SELECT voice_id FROM marini))
/* Основной запрос: партии меццо, которые исполняет только один певец и это — Марини */
SELECT opera_title, character_name FROM mezzo_opera
    JOIN role USING(character_id)
    JOIN opera_character USING(character_id)
    JOIN opera ON mezzo_opera.opera_id = opera.opera_id
    WHERE character_id IN (SELECT character_id FROM role GROUP BY character_id HAVING COUNT(role_id) = 1) AND singer_id = (SELECT singer_id FROM marini)
UNION
/* Основной запрос: оперы, требую участия всех меццо в труппе */
SELECT opera_title, character_name FROM some_mezzo
    JOIN opera_character USING(character_id)
    JOIN opera ON some_mezzo.opera_id = opera.opera_id
    WHERE character_count = (SELECT singer_count FROM mezzo_count)
ORDER BY opera_title, character_name;
```
<details>
    <summary>Результат</summary>
</details><br>