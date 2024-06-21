
import mysql.connector
class Database:
    def conec():
        connection =mysql.connector.connect(host='localhost',user='root',password='041199',database='pixeluxApp')
        c= connection.cursor()