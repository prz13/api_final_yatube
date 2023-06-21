## Финальный проект по API
[![Python](https://img.shields.io/badge/-Python-464641?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-464646?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![Pytest](https://img.shields.io/badge/Pytest-464646?style=flat-square&logo=pytest)](https://docs.pytest.org/en/6.2.x/)
[![Postman](https://img.shields.io/badge/Postman-464646?style=flat-square&logo=postman)](https://www.postman.com/)

## Описание: 
#### Смысл проекта проекта в том, что можно пользоваться функционалом приложения не посещая сайт.
##### Реализованы следующие функцмм:
* Можно создавать, читать, редактировать, удалять посты.
* Можно читать и создавать новые группы.
* Можно отвечать на коментарии и редактировать свои комментарии.
* Можно подписываться на  интересующих Вас пользователей. 
* Есть возможность применять фильтры по полям поиска.


### Документация к приложению (API) поступна по адресу: `http://localhost:8000/redoc/`

## Инструкция по усмтановки:

* Клонируем репозиторий на локальную машину:

```
git clone https://github.com/yandex-praktikum/kittygram_backend.git
```
* Переходим в нужную папку:
```
cd kittygram_backend
```
* Создаем и активируем виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

* Установливаем зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

* Выполняем миграции:

```
python3 manage.py migrate
```

* Запускаем проект:

```
python3 manage.py runserver
```

## ПО для тестирования приложения API (Postman)
https://www.postman.com/

## Примеры запросов к приложению API:

Получить список всех постов (GET):
```
http://127.0.0.1:8000/api/v1/posts/
```

Получить конкретный пост (GET):
```
http://127.0.0.1:8000/api/v1/posts/1/
```

Получить коментарии конкретного поста (GET):
```
http://127.0.0.1:8000/api/v1/posts/1/comments/
```

Получить список всех групп (GET):
```
http://127.0.0.1:8000/api/v1/groups/
```

Создать новый пост (POST):

(Только для зарегистрированных пользователей!)
```
http://127.0.0.1:8000/api/v1/posts/
```