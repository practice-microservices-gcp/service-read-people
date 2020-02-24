from entities.metadata_entity import MetadataEntity
from entities.people_entity import PeopleEntity
from entities.people_page_entity import PeoplePageEntity
from entities.response_entity import ResponseEntity
from facades.pagination_facade import paginationFacade

import traceback

from responses import responses
from people_repository.people_repository import peopleRepository


def listPeople(offset, limit):

    try:
        pagDic = paginationFacade.offsetLimitValidation(offset, limit)
        if (not pagDic):
            raise responses.WrongRequest
        
        peopleDB = peopleRepository.listPeople(**pagDic)
        metadata = MetadataEntity(limit, offset, peopleDB['total'])
        peopleList = list()

        for tupla in peopleDB['data']:
            peopleList.append(PeopleEntity(tupla[0], tupla[1], tupla[2]))

        return ResponseEntity(200, PeoplePageEntity(metadata, peopleList))
    
    except responses.WrongRequest:
        return ResponseEntity(responses.http_responses['WrongRequest']['code'], responses.http_responses['WrongRequest']['message'])
    except Exception:
        print(traceback.format_exc())
        return ResponseEntity(responses.http_responses['UnexpectedError']['code'], responses.http_responses['UnexpectedError']['message'])
    
