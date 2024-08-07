from utils.date_utils import get_future_date


def set_booking_data(first_name="Test", last_name="User", total_price=140, deposit_paid=True,
                          checkin_offset_weeks=0, checkin_offset_days=0,checkout_offset_weeks=0, checkout_offset_days=0,
                          additional_needs="Breakfast"):
    check_in_date = get_future_date(weeks=checkin_offset_weeks, days=checkin_offset_days)
    check_out_date = get_future_date(weeks=checkout_offset_weeks, days=checkout_offset_days)
    return {
        "firstname": first_name,
        "lastname": last_name,
        "totalprice": total_price,
        "depositpaid": deposit_paid,
        "bookingdates": {
            "checkin": check_in_date,
            "checkout": check_out_date
        },
        "additionalneeds": additional_needs
    }