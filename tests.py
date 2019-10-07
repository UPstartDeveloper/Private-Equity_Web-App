from unittest import TestCase, main as unittest_main, mock
from app import app
from bson.objectid import ObjectId

'''
dummy data to use in testing create, update, and delete routes
(U and D not yet made)
Inspiration taken from Playlister tutorial.
'''
sample_offer_id = ObjectId('5d55cffc4a3d4031f42827a3')
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

    def test_show_offers(self):
        """Test showing offers on a property."""
        result = self.client.get('/offers_show')
        self.assertEqual(result.status, '200 OK')

    def test_offers_new(self):
        """Test the new offer creation page."""
        result = self.client.get('/offers_new')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Make an Offer', result.data)

    @mock.patch('pymongo.collection.Collection.insert_one')
    def test_submit_offer(self, mock_insert):
        """Test submitting a new offer."""
        result = self.client.post('offers_show', data=sample_form_data)

        # After submitting, should redirect to the offers_show page.
        self.assertEqual(result.status, '200 OK')
        mock_insert.assert_called_with(sample_offer)

    @mock.patch('pymongo.collection.Collection.find_one')
    def test_edit_offer(self, mock_find):
        """Test editing a single offer."""
        mock_find.return_value = sample_offer

        result = self.client.get(f'/offers/{sample_offer_id}/edit')
        self.assertEqual(result.status, '200 OK')
        self.assertIn('Make an Offer', result.data)


if __name__ == '__main__':
    unittest_main()
