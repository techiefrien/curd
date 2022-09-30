import sqlite3
from flask import Flask , render_template , request

global msg , msg1 

msg = ""
msg1 = ""
con = sqlite3.connect("students.db")
con.execute("create table if not exists students ( id integer primary key autoincrement , name text , age text , city text )")
con.close()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add")
def add():
    return render_template("add.html")    

@app.route("/savedetails" , methods=['POST','GET'])
def save():
    try:

        if request.method == "POST":
            n = request.form.get("name")
            a = request.form.get("age")
            c = request.form.get("city")

            with sqlite3.connect("students.db") as con:
                cur = con.cursor()
                cur.execute("insert into students(name , age , city) values(?,?,?)",(n , a , c))
                con.commit()
                
                msg= "recorded added successfully"
    except:
        con.rollback()
        msg = "we cannot add the record"

    finally:
        return render_template("save.html" , msg = msg)    

@app.route("/view")
def view():
    con = sqlite3.connect("students.db")   
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from students")
    data = cur.fetchall()
    return render_template("view.html" , data = data)



@app.route("/remove")
def remove():
    return render_template("remove.html")

@app.route("/rem" , methods=['POST','GET'])
def rem():
    try:
        if request.method == "POST":
            id = request.form.get("id")
            con = sqlite3.connect("students.db")  
            cur = con.cursor()
            cur.execute("delete  from students where id=?",(id,))
            con.commit()
            

    except:
        con.rollback()
        #msg1 = 'failed'
    
    finally:
        return render_template("rem.html")


if __name__ == "__main__":
    app.run(debug=True)

