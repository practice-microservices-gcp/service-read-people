http_responses = {
    'WrongRequest': {
        'message': 'Wrong offset and limit parameters',
        'code': '400'
    },
    'UnexpectedError': {
        'message': 'There is a problem with the data base. Please try later',
        'code': '500'
    }
}

class WrongRequest(Exception):
    pass