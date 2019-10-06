from flask import Flask, render_template, url_for, redirect, request
from pymongo import MongoClient
import os
# from flask_compress import Compress
# from flask_cache import Cache

app = Flask(__name__)
FLASK_APP = app  # specifying flask app
'''
# Flask Compress use inspired by
# https://damyanon.net/post/flask-series-optimizations/
COMPRESS_MIMETYPES = ['text/html']
COMPRESS_LEVEL = 6
COMPRESS_MIN_SIZE = 500
Compress(app)

# Flask Cache use inspired by
# https://damyanon.net/post/flask-series-optimizations/
cache = Cache()
CACHE_TYPE = 'simple'
# configure_app(app)
cache.init_app(app)
'''


host = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/Homely')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
offers = db.offers

# list of links for property images
links = [
    "https://photos.zillowstatic.com/cc_ft_960/ISnudtiomyixgn0000000000.jpg",
    "https://photos.zillowstatic.com/cc_ft_960/ISfciedjxtcf841000000000.jpg",
    "https://photos.zillowstatic.com/cc_ft_960/ISatojh6728i6o1000000000.jpg",
    "https://photos.zillowstatic.com/p_e/IS6eqr7il2cjge0000000000.jpg"
]

# MOCK ARRAY of PROPERTY DEALS *USE OF API FOR THIS COMING SOON
properties = [
    {'name': 'Dallas, TX Property',
     'picture': links[0],
     'address': '4432 Bowser Ave, Dallas, TX 75219',
     'value': 1500000,
     'status': 'OPEN',
     'num_units': 11},
    {'name': 'Austin, TX Property',
     'picture': links[1],
     'address': '701 Baylor St, Austin, TX 78703',
     'value': 1700000,
     'status': 'OPEN',
     'num_units': 6},
    {'name': 'Fort Worth, TX Property',
     'picture': links[2],
     'address': '10294 Western Oaks Rd, Fort Worth, TX 76108',
     'value': 2700000,
     'status': 'CLOSED',
     'num_units': 12},
    {'name': 'Houston, TX Property',
     'picture': links[3],
     'address': '3709 Montrose Blvd, Houston, TX 770069',
     'value': 1000000,
     'status': 'CLOSED',
     'num_units': 7},
]


@app.route('/', methods=['GET'])
def properties_index():
    """Show all open and closed investment properties."""
    return render_template('properties_index.html',
                           properties=properties,
                           links=links)


@app.route('/offers_new')
def offers_new():
    '''Render form to enter offer on a property.'''
    return render_template('offers_new.html')


@app.route('/offers_show', methods=['POST'])
def offers_show():
    """User sees all offers made so far on investment properties."""
    # Submit a new offer on a location to make an investment.
    # Make a new JSON form form data
    new_offer = {
        "name": request.form.get('name'),
        "offer": request.form.get('offer'),
        "email": request.form.get('email'),
        "location": request.form.get('location')
    }
    # Insert into PyMongo database
    offers.insert_one(new_offer)

    # display all previous offers
    return render_template('offers_show.html', offers=offers.find())


@app.route('/offers_show', methods=['GET'])
def offers_show_all():
    return render_template('offers_show.html', offers=offers.find())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
