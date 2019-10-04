from unittest import TestCase, main as unittest_main
from app import app


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

if __name__ == '__main__':
    unittest_main()
