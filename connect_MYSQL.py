# Write Python code to connect to your MySQL database. 
import sys
from DataBase.BD_connect_MYSQL import Database

class conn_Database:
    def __init__(self):
        self.db = Database()

if __name__ == "__main__":
    conn_Database()        