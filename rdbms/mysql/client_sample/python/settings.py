import os

class Settings:
    DB_HOST = '127.0.0.1'
    DB_PORT = int(os.environ['DB_PORT'])
    DB_USERNAME = os.environ['MYSQL_USER']
    DB_PASSWORD = os.environ['MYSQL_PASSWORD']
    DB_NAME = os.environ['MYSQL_DATABASE']
