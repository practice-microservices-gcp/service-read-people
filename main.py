import flask
import sys
from controllers.read_people_controler import listPeople

def read_people(request):
    offset = None
    limit = None

    request_args = request.args

    if request_args and 'offset' in request_args:
        offset = request_args['offset']
    
    if request_args and 'limit' in request_args:
        limit = request_args['limit']

    response = listPeople(offset, limit)
    web_response = flask.Response(
        response.body.to_json(),
        status=response.code
    )
    web_response.headers['Content-Type'] = 'application/json'

    return web_response