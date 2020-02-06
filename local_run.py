from controllers.read_people_controler import listPeople

peopleEntity = listPeople('0','5')
json = peopleEntity.body.to_json()
print ("{}".format(json))
