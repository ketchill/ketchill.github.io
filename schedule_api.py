import json
import time
import requests

class ScheduleApiError(Exception):
    '''
    Raised if there is an error with the schedule API.
    '''
    pass

# The base API endpoint
base_url = 'http://ketchill.github.io'

# the amount of time to wait for the schedule API
timeout_duration = 25