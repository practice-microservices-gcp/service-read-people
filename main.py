from controllers.read_people_controler import listPeople
from response_decorator.response_decorator import http_response

@http_response
def read_people(request):
    offset = None
    limit = None

    request_args = request.args

    if request_args and 'offset' in request_args:
        offset = request_args['offset']
    
    if request_args and 'limit' in request_args:
        limit = request_args['limit']

    return listPeople(offset, limit)