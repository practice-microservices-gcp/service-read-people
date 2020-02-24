from entity_decorator.entity_decorator import serializable

@serializable
class ResponseEntity():

    def __init__(self,code, body):
        self.code = code
        self.body = body
