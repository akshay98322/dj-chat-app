# dj-chat-app
This is a basic Chat App using Websocket and AsyncWebsocket.

## Installation

Install Python 3.9.0

```bash
  pip install virtualenvwrapper-win==1.2.7
  mkvirtualenv <your_virtual_env_name>  
```

## Run Locally

Clone the project

```bash
  git clone https://github.com/akshay98322/dj-chat-app-with-generic-consumer.git
```

Go to the project directory

```bash
  cd dj-chat-app-with-generic-consumer
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Create DB and Tables

```bash
  python manage.py makemigrations
  python manage.py migrate
```

Create admin/super user

```bash
  python manage.py createsuperuser
```

Download and run docker desktop in your pc.

Start the redis service in a new terminal
```bash
  docker run -p 6379:6379 --name redis redis
```

Start the server

```bash
  python manage.py runserver
```



