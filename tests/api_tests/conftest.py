import pytest

from pages.api_booking import APIBooking


@pytest.fixture
def base_url():
    return 'https://restful-booker.herokuapp.com/booking'

@pytest.fixture
def headers():
    return {
        "Content-Type": "application/json",
    }

@pytest.fixture
def put_headers():
    return {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='
    }

@pytest.fixture
def api_booking(base_url, headers):
    return APIBooking(base_url, headers)