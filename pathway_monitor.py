import random

def check_for_updates():
    """Mock: randomly detect updates."""
    updates = [
        None,
        "New circular: attendance now 70%",
        "Policy updated: notice period changed to 3 weeks"
    ]
    return random.choice(updates)
