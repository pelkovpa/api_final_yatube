**YATUBE**

Проект API для социальной сети, в которой есть возможность публиковать и читать посты, подписываться на других авторов, а также комментировать их записи.

**Как запустить проект:**

Клонировать репозиторий и перейти в него в командной строке:

`git clone https://github.com/pelkovpa/api_final_yatube.git`

`cd api_final_yatube`

Cоздать и активировать виртуальное окружение:

`python -m venv venv`

`source venv/bin/activate`

Установить зависимости из файла requirements.txt:

`python -m pip install --upgrade pip`

`pip install -r requirements.txt`

Выполнить миграции:

`python manage.py migrate`

Запустить проект:

`python manage.py runserver`
