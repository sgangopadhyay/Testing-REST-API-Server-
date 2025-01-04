"""
RESTAPI.py


Library files to communicate with REST API server
"""

import requests


class SumanAPIServer:

    def __init__(self, url):
        self.url = url

    # Fetch Status code
    def api_status_code(self):
        response = requests.get(self.url)
        return response.status_code

    # Fetch the REST API server Headers
    def fetch_headers(self):
        if self.api_status_code() == 200:
            response = requests.get(self.url)
            return response.headers
        else:
            return 404

    # GET method - Fetch data from API server
    def fetch_api_data(self):
        if self.api_status_code() == 200:
            response = requests.get(self.url)
            return response.json()
            # GET method - Fetch the data by its ID

    def fetch_by_id(self, id):
        if self.api_status_code() == 200:
            id = str(id)
            for data in self.fetch_api_data():
                if data['id'] == id:
                    print(data['id'])
                    print(data['name'])
                    print(data['email'])
                    print(data['city'])
                    print(data['country'])

    # POST method - Insert data
    def insert_data(self, data):
        if self.api_status_code() == 200:
            response = requests.post(self.url, json=data)
            if response:
                return True
            else:
                return False

    # DELETE method - Delete data
    def delete_data(self, id):
        if self.api_status_code() == 200:
            id = str(id)
            url = self.url + "/" + id
            response = requests.delete(url)
            if response.status_code == 200:
                return True
            else:
                return False

    # PATCH method - Updated data
    def update_data(self, id, data):
        if self.api_status_code() == 200:
            id = str(id)
            url = self.url + "/" + id
            response = requests.patch(url, json=data)
            if response.status_code == 200:
                return True
            else:
                return False
