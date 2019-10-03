from flask import Flask, render_template, url_for, redirect, request
from pymongo import MongoClient

app = Flask(__name__)
FLASK_APP = app  # specifying flask app

client = MongoClient()
db = client.Homely
offers = db.offers

# list of links for property images
links = [
    "https://photos.zillowstatic.com/cc_ft_960/ISnudtiomyixgn0000000000.jpg",
    "https://photos.zillowstatic.com/cc_ft_960/ISfciedjxtcf841000000000.jpg",
    "https://photos.zillowstatic.com/cc_ft_960/ISatojh6728i6o1000000000.jpg",
    "https://photos.zillowstatic.com/p_e/IS6eqr7il2cjge0000000000.jpg"
]

# MOCK ARRAY of INVESTMENT DEALS *USE OF API FOR THIS COMING SOON
investments = [
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


@app.route('/')
def investments_index():
    """Show all open and closed investment properties."""
    return render_template('investments_index.html',
                           investments=investments,
                           links=links)


@app.route('/investments/new')
def investments_new_form():
    '''Render form to enter offer on a property.'''
    return render_template('investments_new.html')


@app.route('/investments/new', methods=['GET', 'POST'])
def investments_new():
    """Submit a new offer on a location to make an investment."""
    # Make a new JSON form form data
    new_offer = {
        "name": request.form.get('name'),
        "offer": request.form.get('offering')
    }
    # Insert into PyMongo database
    offers.insert_one(new_offer)


@app.route('/investments/show', methods=['POST'])
def investments_show():
    """Show user all offers made so far."""
    pass


if __name__ == '__main__':
    app.run(debug=True)
