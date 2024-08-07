import requests as requests


class APIBase():
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers

    def request_api(self, method, endpoint='', data=None, params=None, headers=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.request(method, url, json=data, headers=headers, params=params)
        return response

    # def _post(self, endpoint, data=None):
    #     url = f"{self.base_url}/{endpoint}"
    #     response = requests.post(url, json=data, headers=headers or self.headers)
    #     return response
    #
    # def _get(self, endpoint, params=None):
    #     url = f"{self.base_url}/{endpoint}"
    #     response = requests.get(url, params=params)
    #     return response
    #
    # def _put(self, endpoint, data=None):
    #     url = f"{self.base_url}/{endpoint}"
    #     response = requests.put(url, json=data, headers=self.headers)
    #     return response

