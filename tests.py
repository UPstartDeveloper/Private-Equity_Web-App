from unittest import TestCase, main as unittest_main, mock
from app import app
from bson.objectid import ObjectId

'''
dummy data to use in testing create, update, and delete routes
(U and D not yet made)
Inspiration taken from Playlister tutorial.
'''
sample_offer_id = ObjectId('5349b4ddd2781d08c09890f4')
sample_offer = {
    'name': 'Muhammad Ali',
    'offer': '4500',
    'email': 'bogus@yahoo.com',
    'location': 'Fort Worth, TX'
}
sample_form_data = {
    'name': sample_offer['name'],
    'offer': sample_offer['offer'],
    'email': sample_offer['email'],
    'location': sample_offer['location']
}


class HomelyTests(TestCase):
    """Flask tests."""

    def setUp(self):
        """Get Flask test client."""
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

    def test_properties_index(self):
        """Test the properties homepage."""
        result = self.client.get('/')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Welcome', result.data)

    def test_offers_new(self):
        """Test the new offer creation page."""
        result = self.client.get('/offers_new')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Make an Offer', result.data)

    def test_offers_show_every(self):
        """Test showing the page of all offers."""
        result = self.client.get('/offers_show_every')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Offers', result.data)

    @mock.patch('pymongo.collection.Collection.insert_one')
    def test_submit_offer(self, mock_insert):
        """Test submitting a new offer. Entry point for route
            is called offers_show_all.
        """
        result = self.client.post('offers_show', data=sample_form_data)

        # After submitting, should redirect to the offers_show page.
        self.assertEqual(result.status, '302 FOUND')
        mock_insert.assert_called_with(sample_offer)

    @mock.patch('pymongo.collection.Collection.find_one')
    def test_show_offer(self, mock_find):
        """Test showing a single offer."""
        mock_find.return_value = sample_offer

        result = self.client.get(f'/offers/{sample_offer_id}')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Description', result.data)

    @mock.patch('pymongo.collection.Collection.find_one')
    def test_offers_edit(self, mock_find):
        """Test rendering of the edit offer form."""
        mock_find.return_value = sample_offer

        result = self.client.get(f'/offers/{sample_offer_id}/edit')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Edit This Offer', result.data)

    @mock.patch('pymongo.collection.Collection.find_one')
    def test_edit_offer(self, mock_find):
        """Test submitted an edited offer."""
        mock_find.return_value = sample_offer

        result = self.client.get(f'/offers/{sample_offer_id}')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Description', result.data)

    @mock.patch('pymongo.collection.Collection.delete_one')
    def test_offers_delete(self, mock_delete):
        """Test deletion of an offer."""
        form_data = {'_method': 'DELETE'}
        result = self.client.post(f'/offers/{sample_offer_id}/delete',
                                  data=form_data)
        self.assertEqual(result.status, '302 FOUND')
        mock_delete.assert_called_with({'_id': sample_offer_id})


if __name__ == '__main__':
    unittest_main()
