import sqlite3
import pandas as pd


class curd:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """ create table if not exists curdop (

                   id integer praimary key ai, 
                   name text , 
                   age text , 
                   place text 
           ) """
        self.cur.execute(sql)
        self.con.commit()   

    def fetch(self):
        self.cur.execute("select * from curdop")
        val  = self.cur.fetchall()
        return val 
            

    def add(self , name , age , place ):
        self.cur.execute("insert into curdop values(null,?,?,?) " , (name, age , place))
        self.con.commit()

obj = curd("database.db")
values = obj.fetch()
print(values)


