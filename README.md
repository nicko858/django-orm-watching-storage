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

- Fill your database params in the `project/settings.py`

    ```bash
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': '',
        'PORT': '',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        }
      }
    ```
- Run the program


## How to run

  ```bash
      $ python main.py
  ```

## Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
