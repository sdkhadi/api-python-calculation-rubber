from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'myrubber_admin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Rubber2020'
app.config['MYSQL_DATABASE_DB'] = 'myrubber_calculation'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
