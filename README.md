# Проект API_FINAL_YATUBE

## Версии языка и используемых библиотек

- Python - 3.9.10

- Django - 3.2.16

- DjangoRestFramework - 3.12.4 

- DjangoRestFramework-SimpleJWT - 4.7.2 

## Описание проекта

Проект API_FINAL_YATUBE представляет собой готовый бэкенд для создания сервиса публикации постов.

Основные составляющие:
1. Система авторизации через токены JWT
2. Система публикации и комментирования постов
   
   2.1 Публикация и комментирование только для зарегистрированных пользователей
   
   2.2 Редактирование и удаление ограничено только для авторов публикаций и комментариев
   
   2.3 Чтение доступно всем пользователям
   
3. Система объединения публикаций в группы
   
   3.1 Создание групп доступно только для администраторов проекта
   
   3.2 Добавление публикации в определенную группу доступно только ее автору
   
4. Система подписок для зарегистрированных пользователей

### Основные эндпоинты и примеры их использования представлены в документации проекта - [Redoc](http://127.0.0.1:8000/redoc/)

## Установка проекта:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/ItsFreez/api_final_yatube.git
```

```
cd kittygram
```

Cоздать и активировать виртуальное окружение:

Для Windows
```
python -m venv env
source venv/Scripts/Activate
```
Для MacOS/Linux
```
python3 -m venv env
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### ***Автор проекта - [ItsFreez](https://github.com/ItsFreez)***
