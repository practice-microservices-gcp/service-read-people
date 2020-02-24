from entity_decorator.entity_decorator import serializable

@serializable
class MetadataEntity():

    def __init__(self, limit, offset, total):
        self.limit = limit
        self.offset = offset
        self.total = total