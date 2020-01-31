from controllers.read_people_controler import listPeople

peopleEntity = listPeople(0,5)
json = peopleEntity.to_json()
print ("{}".format(json))
