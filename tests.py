from unittest import TestCase, main as unittest_main
from app import app


class HomelyTests(TestCase):
    """Flask tests."""

    def setUp(self):
        """Get Flask test client."""
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True


if __name__ == '__main__':
    unittest_main()
