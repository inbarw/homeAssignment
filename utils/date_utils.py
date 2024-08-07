from datetime import datetime, timedelta

def get_future_date(weeks=0, days=0):
    current_date = datetime.now().date()
    future_date = current_date + timedelta(weeks=weeks, days=days)
    return future_date.strftime("%Y-%m-%d")

def verify_item_in_list_of_dict(value, data):
    return any(value in item.values() for item in data)