'''
Lesson 138 操作SQLite数据库

'''

import sys
from PyQt5.QtSql import QSqlDatabase,QSqlQuery
def createDB():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('./db/database.db')
    if not db.open():
        print('Not Connected')
        return False
    query = QSqlQuery()
    query.exec('create table people(id int primary key,name varchar(10),address varchar(50))')
    query.exec('insert into people values(1,"Jason","Shenyang")')
    query.exec('insert into people values(2,"Justin","Shanghai")')
    db.close()
    return True

if __name__ == '__main__':
    createDB()
