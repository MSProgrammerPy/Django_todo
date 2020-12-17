# Django ToDo
ToDo web application built with Django.

# Installation
#### step 1
Download or clone repository:
```
$ git clone https://github.com/MSProgrammerPy/Django_todo.git
```
Go to cloned repository:
```
$ cd Django_todo
```

#### step 2
Creating a virtual environment:
```
$ python -m venv venv
```

#### step 3
Activate virtual environment:
```
$ .\venv\Scripts\activate
```
If you want to switch projects or otherwise leave your virtual environment, simply run:
```
$ .\venv\Scripts\deactivate
```

#### step 4
Download Django.  
After activating virtual environment, download Django:
```
$ pip install Django==3.1.4
```

#### step 5
run:
```
$ python manage.py makemigrations
```
```
$ python manage.py migrate
```

# Usage
#### step 1
Go to cloned repository:
```
$ cd Django_todo
```

#### step 2
Activate virtual environment:
```
$ .\venv\Scripts\activate
```

#### step 3
Run server:
```
$ python manage.py runserver
```
This command starts a lightweight development Web server on the local machine. By default, the server runs on port 8000 on the IP address 127.0.0.1.  
http://127.0.0.1:8000/  

If you want to run server on custom port, use:
```
$ python manage.py runserver <your_port>
```
Quit the server with CTRL - BREAK.
