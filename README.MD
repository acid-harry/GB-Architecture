# Архитектура ПО (семинары)

![ClinicAPI](imgs/AutoShopAPI.png)

-----

## Урок 12. Принципы тестирования приложений
### Поработать с тестированием контроллеров нашего WEB-сервиса, добавить проект с автотестами (Unit-тесты).
### Добавить несколько тестов для методов добавления/удаления/редактирования объектов системы по примеру с нашего семинара.
### Если вам тяжело работать в рамках языка C#, вы можете поработать с вашим собственном проектом в контексте любого языка программирования.

### В проект добавлен пакет  [**tests**](tests "Ссылка на пакет"), в котором протестирован контроллер [**client.py**](controllers/client.py "Ссылка на файл") на CRUD-запросы. Во время запуска каждого теста создается временная база данных, а по окончании теста она удаляется. Это сделано с помощью фикстуры в модуле [**conftest.py**](tests/conftest.py "Ссылка на файл")
### Вывод тестов сохранен в директорию [**tests/сonsole_templates**](tests/console_templates/ "Ссылка на пакет")

-----

### Для проекта потребовались библиотеки, перечисленные в [**requirements.txt**](requirements.txt "Ссылка на файл"). Для быстрой установки необходимо выполнить команду:
    pip install -r requirements.txt  