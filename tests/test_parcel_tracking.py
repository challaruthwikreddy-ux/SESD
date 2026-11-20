from parcel_tracking import get_latest_status


def test_returns_latest_status():
    updates = ["Parcel received", "In transit", "Out for delivery"]
    assert get_latest_status(updates) == "Out for delivery"


def test_returns_message_when_no_updates():
    assert get_latest_status([]) == "No updates available"
