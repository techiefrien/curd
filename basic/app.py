from flask import Flask , render_template , request , url_for 
import sqlite3
from database import curd

db = curd("database.db")


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/confirm" , methods=['POST','GET'])
def confirms():
    if request.method == "POST":
        n =  request.form.get("name")
        a =  request.form.get("age")
        c =  request.form.get("city")
        return render_template("home.html" , name = n , age = a , city = c)    


if __name__ == "__main__":
    app.run(debug=True)



