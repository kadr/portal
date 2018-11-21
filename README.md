# Case Portal
Проект использует Python версии 3.7

### Разворачиваем проект
##### Все дальнейшие действия совершать в папке с проектом
 - Все  зависимости находяться в файле **requirements.txt**. Для того что бы установить зависимости нужно выполнить в консоле, команду: **pip3 install -r requirements.txt**
 - Установить сервер базы данных, если нет
 - Доступы к базе нужно прописыват в файле **my.cnf**, переименовав файл **my_exampe.cnf** и туда забить свои доступы к базе
 - После настройки базы, нужно запустить миграции, для создания структуры таблиц в базе. Для это выполняем команду: **python3 manage.py migrate**
 - Для запуска локального сервера, выполняем: **python3 manage.py runserver 127.0.1.1:8000**
 - Если не возникло никаких ошибок и север запустился, в браузере по адресу **http://localhost:8000/admin** появиться форма авторизации
 - Для того что бы попасть в админку, надо создать суперпользователя, выполняем команду: **python3 manage.py createsuperuser**, далее следуем инструкциям мастера.

### Code Style
В проекте используется пакет Flake8 для проверки форматирования кода и приведения его к одному стилю.
Установка производиться вместе с установкой всех пакетов из файла requirements.txt. Далее нужно настроить взаимодействие с гитом, что бы не пропускать коммиты с невалидным форматированием:
 - Установить хук для Git: **flake8 --install-hook git**
 - И настроить сам гит, чтобы учитывать правила Flake8: **git config --bool flake8.strict true**

Пост с объяснением работы Flake8:  *https://habr.com/company/dataart/blog/318776/*

### Консольные команды
