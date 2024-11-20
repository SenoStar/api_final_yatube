# api_final_yatube

## Описание
**api_final_yatube** — это проект, позволяющий пользователям публиковать личные посты. Он включает в себя функционал для чтения, создания, удаления и редактирования постов и комментариев к ним. Также предусмотрена возможность подписки на других пользователей и получение JWT токена для авторизации.

## Установка и запуск

Чтобы развернуть проект на локальной машине, выполните следующие шаги:

1. Клонировать репозиторий:
   ```bash
   git clone <https or SSH URL>
Перейти в папку проекта:

bash

Copy
cd api_final_yatube
Создать и активировать виртуальное окружение:

bash

Copy
python3 -m venv venv
source venv/bin/activate
Обновить pip:

bash

Copy
python3 -m pip install --upgrade pip
Установить зависимости:

bash

Copy
pip install -r requirements.txt
Выполнить миграции:

bash

Copy
python3 api_yatube/manage.py migrate
Запустить сервер:

bash

Copy
python3 api_yatube/manage.py runserver
