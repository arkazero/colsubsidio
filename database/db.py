import pymysql

db_host = 'database-clase.ca1q2d4cnkkx.us-east-2.rds.amazonaws.com'
db_user = 'admin'
db_password = 'colsubsidio'
db_database = 'clase'

try:
    pymysql.connect(
        host = db_host,
        user = db_user,
        password = db_password,
        database = db_database
    )
    print("Conexion satisfactoria")
except Exception as err:
    print("Error de conexion")