from repositories.people_repository import peopleRepository
from entities.metadata_entity import MetadataEntity
from entities.people_entity import PeopleEntity
from entities.people_page_entity import PeoplePageEntity
from entities.response_entity import ResponseEntity
from facades.pagination_facade import paginationFacade


def listPeople(offset, limit):

    if (not paginationFacade.offsetLimitValidation(offset, limit)):
        raise Exception
    
    peopleDB = peopleRepository.listPeople(offset,limit)
    metadata = MetadataEntity(limit, offset, peopleDB['total'])
    peopleList = list()
    
    for tupla in peopleDB['data']:
        peopleList.append(PeopleEntity(tupla[0], tupla[1], tupla[2]))

    return ResponseEntity(200, PeoplePageEntity(metadata, peopleList))

    
