from entity_decorator.entity_decorator import serializable

@serializable
class PeoplePageEntity():

    def __init__(self, metadata, people):
        self.metadata = metadata
        self.data = people
