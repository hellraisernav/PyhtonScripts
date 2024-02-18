from datetime import datetime

""" A simple module that returns the current date time"""

def get_current_time():
    """Returns current time"""
    c_time=datetime.now().strftime('%H%M%S_%y%b%d')
    return c_time