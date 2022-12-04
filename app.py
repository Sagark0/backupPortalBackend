from flask import Flask, redirect, url_for, request
import psycopg2
import json
app = Flask(__name__)

@app.route("/")
def hello():
    return "backend is running properly"

@app.route("/getData")
def data():
    conn,curr=connect()
    query="SELECT * FROM backupportal.dim_test where id>4"
    curr.execute(query)
    returnObj=''
    output=curr.fetchall()
    print(output)
    if(output is not None):
        returnObj=output
    else:
        returnObj="Nothing Found"
    conn.commit()
    conn.close()
    return json.dumps(returnObj)

@app.route("/uploadData",methods=["POST"])
def upload():
    if(request.method=="POST"):
        item=request.form["item"]
        conn,curr=connect()
        query="Insert into backupportal.dim_test (\"name\") values('{}')"
        curr.execute(query.format(item))
        conn.commit()
        conn.close()
        return "Item Added: %s" % item

def connect():
    conn=psycopg2.connect(dbname="postgres", user="postgres", password="root", host="localhost")
    curr=conn.cursor()

    return conn,curr

if __name__=="__main__":
    app.run(debug=True)