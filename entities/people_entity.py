from entity_decorator.entity_decorator import serializable

@serializable
class PeopleEntity():

    def __init__(self, id, name, surname, email):
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email
