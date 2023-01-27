import mysql.connector




class RepositorioConsulta:
    def __init__(self,database):
        self.database = database
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="299Gorillaz@"
        )
        self.mydb.connect()
        cursor = self.mydb.cursor()
        cursor.execute(f"""CREATE DATABASE IF NOT EXISTS {self.database} """)
        cursor.close()