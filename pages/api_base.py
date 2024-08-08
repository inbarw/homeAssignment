import requests as requests


class APIBase():
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers

    def request_api(self, method, endpoint='', data=None, params=None, headers=None):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.request(method, url, json=data, headers=headers, params=params)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return "Error: " + str(e)
        return response.json()


