from entity_decorator.entity_decorator import serializable

@serializable
class PeopleEntity():

    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email
