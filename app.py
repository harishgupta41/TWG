from flask import Flask, render_template
from pymongo import MongoClient
import base64

app=Flask(__name__)

client=MongoClient('localhost',27017) #creating client
db=client.touchwoodgraphics # creating database
service=db.services #creating collection
service.insert_one({'name':'tshirt printing','price':'200'})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)