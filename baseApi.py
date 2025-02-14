import requests

class BaseApi:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def __init__(self):
        self.session = requests.Session()

    def get(self, endpoint, params=None):
        return self.session.get(f"{self.BASE_URL}/{endpoint}", params=params)

    def post(self, endpoint, data=None):
        return self.session.post(f"{self.BASE_URL}/{endpoint}", json=data)

    def put(self, endpoint, data=None):
        return self.session.put(f"{self.BASE_URL}/{endpoint}", json=data)

    def patch(self, endpoint, data=None):
        return self.session.patch(f"{self.BASE_URL}/{endpoint}", json=data)

    def delete(self, endpoint):
        return self.session.delete(f"{self.BASE_URL}/{endpoint}")

    def print_response(self, response):
        print(f"Status Code: {response.status_code}")
        print(f"Response JSON: {response.json()}")
        print("-" * 50)
