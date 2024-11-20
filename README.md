# api_final_yatube

## Описание
**api_final_yatube** — это проект, позволяющий пользователям публиковать личные посты. Он включает в себя функционал для чтения, создания, удаления и редактирования постов и комментариев к ним. Также предусмотрена возможность подписки на других пользователей и получение JWT токена для авторизации.

## Установка и запуск

Чтобы развернуть проект на локальной машине для Windows, выполните следующие шаги:

1. Клонировать репозиторий:
   ```bash
   git clone https://github.com/SenoStar/api_final_yatube.git
   ```
2. Перейти в папку проекта:
   ```bash
   cd api_final_yatube
   ```
3. Создать и активировать виртуальное окружение:
   ```bash
   python -m venv venv
   ```
   ```bash
   source venv/Script/activate
   ```
4. Установить зависимости:
   ```bash
   pip install -r requirements.txt
   ```
5. Выполнить миграции:
   ```bash
   python api_yatube/manage.py migrate
   ```
Запустить сервер:

bash

Copy
python3 api_yatube/manage.py runserver
