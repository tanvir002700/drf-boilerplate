# drf-boilerplate

This is a django rest framework project boilerplate.

## Initial Auth Endpoints
 - User Signup
 - User Login
 - User Logout
 - User Account Activation
 - User Account Activation Resend Email
 - User Password Reset Eamil
 - User Password Confirmation
 - User Set Password
 - User Set Email

## Initial Others Endpoints
 - Api Docs
 - Api Schema
 
## Local Development Setup
 - First Create python virtual env
 ```
  $ virtualenv -p python .venv
 ```
 - Install Requirements
 ```
  $ pip install -r api/requiremts.txt
 ```
 - Copy .env-example to .env and set config
 ```
  $ copy .env-example .env
 ```
 - Create postgres database
 ```
  $ sudo su postgres
  $ psql
  postgres=# CREATE USER django WITH PASSWORD 'password';
  postgres=# ALTER ROLE django SET client_encoding TO 'utf8';
  postgres=# ALTER ROLE django SET default_transaction_isolation TO 'read committed';
  postgres=# ALTER ROLE django SET timezone TO 'UTC';
  postgres=# CREATE DATABASE drf;
  postgres=# GRANT ALL PRIVILEGES ON DATABASE drf TO django;
  postgres=# \q
  $ exit
 ```
 - Run Server
 ```
  $ python api/manage.py runserver
 ```
## Docker Development Setup
 - Set database name and password in .docker-env file
 - Copy .docker-env.example to .env and set config
 ```
  $ cp .docker-env.example .env
 ```
 - Build app
 ```
  $ docker-compose build
 ```
 - run application and services
 ```
  $ docker-compose up
 ```
 - run migration while running container
 ```
  $ docker-compose run app python api/manage.py migrate
 ```
