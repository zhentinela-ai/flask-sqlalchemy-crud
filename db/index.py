from dotenv import load_dotenv
load_dotenv()
import os
import MySQLdb
connection = MySQLdb.connect(
  host= os.environ["MYSQL_HOST"],
  user=os.environ["MYSQL_USER"],
  passwd= os.environ["MYSQL_PASSWORD"],
  db= os.environ["MYSQL_DB"],
  ssl_mode = "VERIFY_IDENTITY",
  ssl      = {
    "ca": "/etc/ssl/cert.pem"
  }
)