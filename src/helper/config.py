from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'myrubber_python'
app.config['MYSQL_DATABASE_PASSWORD'] = 'BukasaJ4'
app.config['MYSQL_DATABASE_DB'] = 'myrubber_calculation'
app.config['MYSQL_DATABASE_HOST'] = '103.145.226.120'
mysql.init_app(app)


