# Movie drf project

## Запуск приложения
### Запуск БД в docker
```shell
docker run --name postgres -p 5432:5432 -e POSTGRES_USER=postgres \
-e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres \
-v /custom/mount:/var/lib/postgresql/data -d postgres:15
```
### Склонировать проект
```shell
git clone https://github.com/zxdmimfort/drf-movie.git
cd 
pip install -r requirements.txt
```
### Выполняем миграции и запускаем приложение
```shell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Приложение доступно по адресу http://localhost:8000
На http://localhost:8000/admin находится админка
Фильмы http://localhost:8000/api/movies/
```json
{
    "list": [
        {
            "id": 2,
            "title": "movie 1",
            "year": 2023,
            "length": "01:01:00",
            "rating": 9,
            "director": 1
        },
        {
            "id": 3,
            "title": "movie 2",
            "year": 2020,
            "length": "01:01:00",
            "rating": 7,
            "director": 2
        },
        {
            "id": 4,
            "title": "movie 3",
            "year": 2020,
            "length": "01:01:00",
            "rating": 7,
            "director": 2
        },
        {
            "id": 5,
            "title": "movie 4",
            "year": 2020,
            "length": "01:01:00",
            "rating": 7,
            "director": 3
        }
    ]
}
```
Режиссеры http://localhost:8000/api/directors/
```json
{
    "list": [
        {
            "id": 1,
            "fio": "director 1"
        },
        {
            "id": 2,
            "fio": "director 2"
        },
        {
            "id": 3,
            "fio": "director 3"
        }
    ]
}
```
Доступны методы GET, POST, PATCH, DELETE, PUT
Можно выбрать конкретную запись по id http://localhost:8000/api/movies/2, http://localhost:8000/api/directors/1
