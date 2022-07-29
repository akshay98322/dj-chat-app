# dj-chat-app
This is a basic Chat App

pip install -r requirements.txt
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py startapp core

docker run -p 6379:6379 --name redis redis
