# API YaTube

## Описание
**API YaTube** - это API-сервис для публикации постов.
Основные возможности проекта: публикация записей, комментирование записей, а так же подписки на авторов.

### Основной функционал проекта:

- Регистрация и работа с пользователями через JWT-токены
- Получение, создание, обновление, удаление публикаций
- Получение, создание, обновление, удаление комментариев к публикациям
- Просмотр групп и детальной информации о них
- Отслеживание подписок на авторов, а также возможность подписки на интересующего автора публикации

## Стек технологий 

![](https://img.shields.io/badge/Python-3.9-black?style=flat&logo=python) 
![](https://img.shields.io/badge/Django-3.2.16-black?style=flat&logo=fastapi)
![](https://img.shields.io/badge/DjangoRestFramework-3.12.4-black?style=flat)

## Порядок действий для запуска проекта

***1. Клонировать репозиторий и перейти в папку c проектом***

```shell
git clonegit@github.com:ItsFreez/API_YaTube.git
```

```shell
cd API_YaTube
```

***2. Cоздать и активировать виртуальное окружение***

*Для Windows*
```shell
python -m venv env
source venv/Scripts/Activate
```
*Для MacOS/Linux*
```shell
python3 -m venv env
source env/bin/activate
```

***3. Обновить менеджер pip и установить зависимости из файла requirements.txt***

```shell
python -m pip install --upgrade pip
```

```shell
pip install -r requirements.txt
```

***4. Применить миграции для создания базы данных***

```shell
cd yatube_api
```

```shell
python manage.py migrate
```

***5. Запустить проект***

```shell
python manage.py runserver
```

***6. Изучить эндпоинты и примеры их использования в документации Redoc***

```shell
http://127.0.0.1:8000/redoc/
```

### Автор проекта

[ItsFreez](https://github.com/ItsFreez)
