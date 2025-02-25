from flask import Flask, render_template
from pymongo import MongoClient
import base64

app=Flask(__name__)

# client=MongoClient('localhost',27017) #creating client
# db=client.touchwoodgraphics # creating database
# service=db.services #creating collection
# service.insert_one({'name':'tshirt printing','price':'200'})

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/apparels')
def apparels():
    return render_template('apparels.html', title="Apparels")

@app.route('/businessEssentials')
def businessEss():
    return render_template('bussinessEss.html',title='Business Essentials')

@app.route('/customiseGifts')
def customGifts():
    return render_template('customGift.html',title='Customise Gifts')

@app.route('/designingServices')
def designServices():
    return render_template('designServ.html',title='Designing Services')

@app.route('/singages')
def singages():
    return render_template('singages.html',title='Singages')

if __name__ == "__main__":
    app.run(debug=True)