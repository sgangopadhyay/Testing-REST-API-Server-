"""
test_RESTAPI.py


The Python UnitTest file for testing REST API Server

Command : python -m unittest -v testRestAPI.py
"""

import unittest

from RestAPI import SumanAPIServer



class TestRESTAPIServer(unittest.TestCase):

    def setUp(self):
        self.url = "https://62513902977373573f4567fb.mockapi.io/pizza/suman"
        self.rest_api_server = SumanAPIServer(self.url)

    # Test Case : REST API Status Code
    def test_api_status_code(self):
        result = self.rest_api_server.api_status_code()
        self.assertEqual(result, 200)

    # Test Case : Insert Data
    def test_insert_data(self):
        data = {"name": "anil", "email": "anil@example.com", "city": "delhi", "country": "india"}
        result = self.rest_api_server.insert_data(data)
        self.assertEqual(result, False)

    # Test Case : Delete Data
    def test_delete_data(self):
        id = 5
        result = self.rest_api_server.delete_data(id)
        self.assertEqual(result, True)


if __name__ == "__main__":
    unittest.main()
