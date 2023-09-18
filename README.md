# Проект Foodgram
___

### Проект доступен по адресу: https://cookbook.servebeer.com/
## Описание
Foodgram — сайт, на котором пользователи могут публиковать рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов. Пользователям сайта также будет доступен сервис «Список покупок». Он позволит создавать список продуктов, которые нужно купить для приготовления выбранных блюд. 
Проект запускается в контейнерах Docker. Настроено автоматическое тестирование и развертывание на виртуальном удаленном сервере с ОС Ubuntu с помощью Github Actions. Сайт защищен шифрованием запросов по протоколу HTTPS.
___

## Технологии, использованные при разработке
[![Python](https://img.shields.io/badge/Python-3776AB?style=plastic&logo=python&logoColor=092E20&labelColor=white
)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-092E20?style=plastic&logo=django&logoColor=092E20&labelColor=white
)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django_REST_framework-DC143C?style=plastic
)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=plastic&logo=postgresql&labelColor=white
)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/NGINX-009639?style=plastic&logo=nginx&logoColor=%23009639&labelColor=white
)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/Gunicorn-499848?style=plastic&logo=gunicorn&labelColor=white
)](https://gunicorn.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=plastic&logo=docker&labelColor=white
)](https://www.docker.com/)
[![Docker-compose](https://img.shields.io/badge/Docker_compose-2496ED?style=plastic&logo=docker&labelColor=white
)](https://docs.docker.com/compose/)
[![GitHub%20Actions](https://img.shields.io/badge/GitHub_actions-2088FF?style=plastic&logo=githubactions&labelColor=white
)](https://github.com/features/actions)
___

## Установка
1. Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/tetrapack55/foodgram-project-react
```
```
cd foodgram-project-react/backend/foodgram
```
2. Cоздать файл .env, указываем следующие переменные со своими данными
```
POSTGRES_USER      #имя пользователя в базе PostgreSQL
POSTGRES_PASSWORD  #пароль пользователя в базе PostgreSQL
POSTGRES_DB        #имя базы данных
DB_HOST            #имя контейнера, где запущен сервер БД
DB_PORT            #порт, по которому Django будет обращаться к базе данных

SECRET_KEY         #ваш секретный код из settings.py
DEBUG              #статус режима отладки
ALLOWED_HOSTS      #адреса, по которым будет доступен проект

```
3. Создать Docker образы  (вместо username ваш логин на  DockerHub)
```
cd frontend
docker build -t username/foodgram_frontend .
cd ../backend
docker build -t username/foodgram_backend .
cd ../infra_prod
docker build -t username/foodgram_gateway . 
```
4. Загрузить образы на DockerHub
```
docker push username/foodgram_frontend
docker push username/foodgram_backend
docker push username/foodgram_gateway
```
5. Подключиться к своему удаленному серверу
```
ssh -i путь_до_файла_с_SSH_ключом/название_файла_с_SSH_ключом имя_пользователя@ip_адрес_сервера 
```
6. Установить docker compose на сервер
```
sudo apt update
sudo apt install curl
curl -fSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh
sudo apt-get install docker-compose-plugin
```
7. Создать на сервере папку foodgram и скопировать в нее файлы docker-compose.yml и .env
8. Открыть на сервере конфиг файл Nginx
```
sudo nano /etc/nginx/sites-enabled/default
```
9. Изменить настройки location
```
location / {
    proxy_set_header Host $http_host;
    proxy_pass http://127.0.0.1:8888;
}
```
10. Перезапустить Nginx
```
sudo service nginx reload
```
11. Для адаптации workflow файла добавить свои данные в секреты GitHub Actions
```
DOCKER_USERNAME                # имя пользователя в DockerHub
DOCKER_PASSWORD                # пароль пользователя в DockerHub
HOST                           # ip_address сервера
USER                           # имя пользователя
SSH_KEY                        # приватный ssh-ключ (cat ~/.ssh/id_rsa)
SSH_PASSPHRASE                 # кодовая фраза (пароль) для ssh-ключа
TELEGRAM_TO                    # id телеграм-аккаунта (можно узнать у @userinfobot, команда /start)
TELEGRAM_TOKEN                 # токен бота (получить токен можно у @BotFather, /token, имя бота)
```
12. Сохранить все изменения и запушить в GitHub. При отсутствии ошибок проект развернется автоматически на сервере
13. Наполнить базу данных ингредиентами и тэгами, используя менеджмент комманды
```
sudo docker compose -f docker-compose.yml exec backend python manage.py load_data
sudo docker compose -f docker-compose.yml exec backend python manage.py load_tags
```
___

## Доступность проекта
- Сайт - https://cookbook.servebeer.com/
- Логин суперюзера - admin
- Пароль суперюзера - sxehardcore55
___

## Примеры запросов к API

Получение и удаление токена

```
POST /api/auth/token/login/
POST /api/auth/token/logout/
```

Регистрация нового пользователя: 

```
POST /api/users/
```

Получение данных своей учетной записи:

```
GET /api/users/me/
```

Получение страницы пользователя и списка всех пользователей
```
GET /api/users/:id/
GET /api/users/?page=1&limit=3
```

Подписка на пользователя и отписка

```
POST /api/users/:id/subscribe/?recipes_limit=3
DELETE /api/users/:id/subscribe/
```

Подписки пользователя
```
GET /api/users/subscriptions/
```

Получение рецепта и списка рецептов
```
GET /api/recipes/:id/
GET /api/recipes/
```

Создание, обновление и удаление рецепта
```
POST /api/recipes/
PATCH /api/recipes/:id/
DELETE /api/recipes/:id/
```

Добавление рецепта в избранное и удаление из избранного
```
POST /api/recipes/:id/favorite/
DELETE /api/recipes/:id/favorite/
```

Добавление рецепта в список покупок и удаление из списка покупок
```
POST /api/recipes/:id/shopping_cart/
DELETE /api/recipes/:id/shopping_cart/
```

Скачать список покупок
```
GET /api/recipes/download_shopping_cart/
```

## Автор проекта
Олег Кирьянов
```
https://github.com/tetrapack55
xagatgx@yandex.ru
```