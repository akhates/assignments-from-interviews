Simple requests for certain company's API, returns currency ratios and then converts it into xlsx file

didn't got hired because I didn't do well on second part

part of code and was removed for obivious reasons

---

Простой реквест к апи чтобы взять данные валют и сгенерить файл экселя с этими данными.
Не сделал вторую часть адаптивной по этому не взяли.
Часть кода и данных из тз была убрана.


Часть 1: Python
1) Дополните файл test.py комментарием к функции test_function.
2) Напишите функцию, которая будет выгружать список валют из API нашего тестового
проекта. Функция должна содержать в себе алгоритм обновления токенов
аутентификации.
Эндпойнт: https://***
Для доступа к эндпойнту вместе с запросом нужно отправить два хэдера:
Authorization и Client-ID.
Authorization - строка вида "Bearer X", где X равен access токену.
Client-ID - строка с client id.


Тестовые данные:

access_token =
"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNj
I1ODM0NDEyLCJqdGkiOiI4ZmZlNjkwZDJhODI0OWRiODI0ZGNlNzVlZTg1NWI0ZSIsInVzZ
XJfaWQiOjI5fQ.H5BITcFUPrlxEmWdIFs-YSvm7dg5nljUMb_8ReYrKOE"


refresh_token =
"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6
MTYyNTkyMDUxMiwianRpIjoiNGNlYzE0NmQxYzRkNDI2ZmIwZDBiNWNhMmMyNTVlM
mQiLCJ1c2VyX2lkIjoyOX0.IimhvxD0JERnq5KNCBDhEnp7duMoAlG3QfgQyd1UmVs"


client_id =
""


Access токен живет 5 минут, refresh токен - 2 недели. Для получения новой пары
токенов нужно сделать POST запрос на эндпойнт
https://***
В теле запроса должно быть одно поле: "refresh" - строка с refresh токеном.
Для того, чтобы запрос на обновление токенов прошел, достаточно только хэдера с
client id.


3) Напишите функцию, которая будет генерировать .xlsx файл со списоком валют из
предыдущей задачи.


Часть 2: JavaScript + CSS
1) Не меняя исходную структуру html, добавьте JavaScript и CSS к файлу test.html так,
чтобы по умолчанию таблица была скрыта и появлялась при нажатии на заголовок
"Sample catalog".
2) Добавьте стили по своему усмотрению. Страницу должно быть удобно
просматривать с разных устройств.
