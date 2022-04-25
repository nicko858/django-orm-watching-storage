# django-orm-watching-storage
This is a simple web site, written on django for educational purposes. 

## Prerequisites

Python3 should be already installed.

## How to install and configure

- ```bash
  $ git clone https://github.com/nicko858/watching-storage
  $ cd watching-storage
  $ pip install -r requirements.txt
  $ python3 -m venv ./venv
  $ . ./venv/bin/activate
  ```
- Create and fill `.env`-file in the project root directory:  
```bash
   DB_HOST=checkpoint.devman.org
   DB_PORT=<database port>
   DB_NAME=<database name>
   DB_USER=<database user>
   DB_PASSWORD=<database password>
   DEBUG=false
```

## How to run

  ```bash
      $ python manage.py runserver
  ```

## Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
