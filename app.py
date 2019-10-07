from flask import Flask, render_template, url_for, redirect, request
from pymongo import MongoClient
import os
from bson.objectid import ObjectId

app = Flask(__name__)
FLASK_APP = app  # specifying flask app

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
    {"name": "Dallas, TX Property",
     'picture': links[0],
     'address': '4432 Bowser Ave, Dallas, TX 75219',
     'value': 1500000,
     'status': 'OPEN',
     'num_units': 11},
    {"name": "Austin, TX Property",
     'picture': links[1],
     'address': '701 Baylor St, Austin, TX 78703',
     'value': 1700000,
     'status': 'OPEN',
     'num_units': 6},
    {"name": "Fort Worth, TX Property",
     'picture': links[2],
     'address': '10294 Western Oaks Rd, Fort Worth, TX 76108',
     'value': 2700000,
     'status': 'CLOSED',
     'num_units': 12},
    {"name": "Houston, TX Property",
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
    return render_template('offers_new.html', properties=properties)


'''
@app.route('/offers_new', methods=['GET', 'POST'])
def offers_show():
    """Submit a new offer on a location to make an investment.
       User sees all offers made so far on investment properties.
    """
    # Make a new JSON from form data
    new_offer = {
        "name": request.form.get('name'),
        "offer": request.form.get('offer'),
        "email": request.form.get('email'),
        "location": request.form.get('location')
    }
    # Insert into PyMongo database
    offer_id = offers.insert_one(new_offer).inserted_id

    # redirect to page showing new offer only
    return render_template('offers_show.html', offer_id=offer_id)
'''


@app.route('/offers_show', methods=['GET'])
def offers_show_every():
    """Submit a new offer on a location to make an investment.
       Users sees all previously made offers on a property from other users.
    """
    return render_template('offers_show.html', offers=offers.find())


@app.route('/offers_show', methods=['POST'])
def offers_show_all():
    """Submit a new offer on a location to make an investment.
       Users sees all previously made offers on a property from other users.
    """
    # Make a new JSON from form data
    new_offer = {
        "name": request.form.get('name'),
        "offer": request.form.get('offer'),
        "email": request.form.get('email'),
        "location": request.form.get('location')
    }
    # Insert into PyMongo database
    offer_id = offers.insert_one(new_offer).inserted_id
    return render_template('offers_show.html', offers=offers.find())

# New routes below 10/6/19


@app.route('/offers/<offer_id>')
def offers_show_single(offer_id):
    """Show a single offer."""
    offer = offers.find_one({'_id': ObjectId(offer_id)})
    return render_template('offer_show.html', offer=offer)


@app.route('/offers/<offer_id>/edit')
def offers_edit(offer_id):
    """Show the edit form for an offer."""
    offer = offers.find_one({'_id': ObjectId(offer_id)})
    return render_template('offers_edit.html', offer=offer,
                           properties=properties)


@app.route('/offers/<offer_id>', methods=['POST'])
def offers_update(offer_id):
    """Submit an edited offer."""
    updated_offer = {
        'name': request.form.get('name'),
        'offer': request.form.get('offer'),
        'email': request.form.get('email'),
        'location': request.form.get('location')
    }
    offers.update_one(
        {'_id': ObjectId(offer_id)},
        {'$set': updated_offer})
    return redirect(url_for('offers_show_single', offer_id=offer_id,
                    offers=offers.find()))


@app.route('/offers/<offer_id>/delete', methods=['POST'])
def offers_delete(offer_id):
    """Delete one offer."""
    offers.delete_one({'_id': ObjectId(offer_id)})
    return redirect(url_for('offers_show_all'))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
