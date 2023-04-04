# Приложение для показа задач в билде, отсортированных по зависимостям

Написано на Python с использованием библиотек: 
- FastAPI
- uvicorn
- dependency-injector
- pydantic

Клонируйте репозиторий
```
git clone https://github.com/fractalical/saber_test.git
cd saber_test
```

Создайте и заполните файл .env по примеру .env.example

## Для запуска в контейнере
```
docker-compose up --build
```

## Для запуска локально

Создайте и запустите виртуальное окружение
```
(windows/linux/macOS)
poetry init
poetry shell

```
Установите зависимости
```
poetry install
```
Запустите приложение
```
uvicorn app:create_app --host 127.0.0.1 --port 8000
```
Тестирование приложения возможно из браузера по ссылке
```
http://HOST:PORT/docs
```
Либо при отправке запросов
```
request.post(url=http://HOST:PORT/build/get_tasks, headers={'X_API_TOKEN': ...}, json={'build': 'name'})
```