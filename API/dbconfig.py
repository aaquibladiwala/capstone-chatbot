from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Enter MYSQL_DATABASE_PASSWORD'
app.config['MYSQL_DATABASE_DB'] = 'JOB_ADVISORY'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)