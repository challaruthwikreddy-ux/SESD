def get_latest_status(status_updates):
    """Return the most recent parcel status, if one exists."""
    if not status_updates:
        return "No updates available"
    return status_updates[-1]
