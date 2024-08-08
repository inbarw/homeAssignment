import json

from pages.api_base import APIBase


class APIBooking(APIBase):
    def __init__(self, base_url, headers=None):
        super().__init__(base_url, headers)

    def create_new_booking(self, booking_data, headers=None):
        return self.request_api("POST", data=booking_data, headers=headers or self.headers)

    def create_new_booking_and_get_booking_id(self, booking_data, headers=None):
        response = self.create_new_booking(booking_data, headers=headers or self.headers)
        booking_id = response['bookingid']
        return booking_id

    def get_all_bookings_by_ids(self, headers=None):
        return self.request_api("GET", headers=headers or self.headers)

    def update_booking(self, booking_id, booking_data, headers=None):
        return self.request_api("PUT", endpoint=booking_id, data=booking_data, headers=headers or self.headers)




