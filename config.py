from dotenv import load_dotenv
import os

load_dotenv()

password = os.environ['MYSQL_PASSWORD']
user = os.environ['MYSQL_USER']
database = os.environ['MYSQL_DB']
host = os.environ['MYSQL_HOST']

DATABASE_CONNECTION_URIL = f'mysql://{user}:{password}@{host}/{database}'
print(DATABASE_CONNECTION_URIL)