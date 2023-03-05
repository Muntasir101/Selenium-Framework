import configparser

config = configparser.ConfigParser()

config.read("config.ini")

database_host = config.get('database', 'host')
database_port = config.get('database', 'port')
database_username = config.get('database', 'username')
database_password = config.get('database', 'password')
print(database_port)
