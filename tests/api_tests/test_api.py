from utils.booking_data_utils import set_booking_data
from utils.date_utils import verify_item_in_list_of_dict, get_future_date

import pytest

@pytest.mark.parametrize("booking_params", [
    {"first_name": "Test1", "last_name": "User1", "total_price": 150, "deposit_paid": True, "checkin_offset_weeks": 2,"checkin_offset_days": 0, "checkout_offset_weeks": 2,"checkout_offset_days": 2, "additional_needs": "Breakfast"},
])
def test_create_new_booking(api_booking, booking_params):
    booking_data = set_booking_data(**booking_params)
    booking_id = api_booking.create_new_booking_and_get_booking_id(booking_data)
    bookings_ids_list = api_booking.get_all_bookings_by_ids()
    assert verify_item_in_list_of_dict(booking_id, bookings_ids_list)


@pytest.mark.parametrize("booking_params", [
    {"first_name": "Test1", "last_name": "User1", "total_price": 150, "deposit_paid": True, "checkin_offset_weeks": 1,"checkin_offset_days": 0, "checkout_offset_weeks": 1,"checkout_offset_days": 4, "additional_needs": "Breakfast"},
])
def test_update_booking(api_booking, booking_params, put_headers):
    booking_data = set_booking_data(**booking_params)
    booking_id = api_booking.create_new_booking_and_get_booking_id(booking_data)
    check_out_updated_date = get_future_date(weeks=1, days=5)
    booking_data["bookingdates"]["checkout"] = check_out_updated_date
    updated_booking_data = api_booking.update_booking(booking_id, booking_data, headers=put_headers)
    assert updated_booking_data["bookingdates"]["checkin"] == booking_data["bookingdates"]["checkin"]
    assert updated_booking_data["bookingdates"]["checkout"] == booking_data["bookingdates"]["checkout"]





