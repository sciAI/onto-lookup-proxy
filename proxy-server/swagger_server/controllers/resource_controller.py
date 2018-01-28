import connexion
from swagger_server.models.concept import Concept
from swagger_server.models.concepts import Concepts
from swagger_server.models.error import Error
from swagger_server.models.jsonld_id import JsonldId
from swagger_server.models.ontologies import Ontologies
from swagger_server.models.ontology import Ontology
from swagger_server.models.repositories import Repositories
from swagger_server.models.repository import Repository
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

import json
import os
import imp
import operator
import time


dir_path = os.path.dirname(os.path.realpath(__file__))
rep_path = os.path.join(dir_path, 'repositories')
modules = {}

for item in os.listdir(rep_path):
    path = os.path.join(rep_path, item)
    fp, pathname, description = imp.find_module(path);
    module = imp.load_module(item, fp, pathname, description);
    modules.setdefault(module.__name__, module)


def concepts(repository, ontology, plain=None):
    """
    
    
    :param repository: 
    :type repository: str
    :param ontology: 
    :type ontology: str
    :param plain: 
    :type plain: bool

    :rtype: Concepts
    """
    # return 'do some magic!'

    module = modules.get(repository)
    obj = []

    if not module:
        return Error(error='No repository', status='404')

    _start = time.time()

    try:
        module_api = module.ResourcesApi()
        response = module_api.concepts(ontology)

        path = module.Meta().concept_xpath
        get_objects = operator.attrgetter(path)

        concepts = get_objects(response)

        if response.page and response.page.total_pages:
            next_page = response.page.number + 1
            total_pages = response.page.total_pages
            # test
            if total_pages > 100:
                return []
            for page in range(next_page, total_pages):
                _next = module_api.concepts(ontology, page=page)
                concepts.extend(get_objects(_next))
                print('> ', page, '/', total_pages, 'in', time.time() - _start)

        meta = module.MetaConcept()

        for item in concepts:
            # resp = Concept(repository=repository, ontology=ontology)
            # for attr in resp.attribute_map:
            #     path = getattr(meta, attr, False)
            #     if not path:
            #         continue
            #     get_value = operator.attrgetter(path)
            #     setattr(resp, attr, get_value(item))
            resp = Concept()
            for attr, _obj in resp.swagger_types.items():
                path = getattr(meta, attr, False)
                if not path:
                    continue
                get_value = operator.attrgetter(path)
                setattr(resp, attr, get_value(item))
                # 
                resp.httpschema_orgrepository = JsonldId(id=repository)
                resp.httpschema_orgontology = JsonldId(id=ontology)
            obj.append(resp)

    except AttributeError as e:
        print("Exception when parsing API: %s\n" % e)
    except module.rest.ApiException as e:
        print("Exception when calling API: %s\n" % e)

    print('request process time:', time.time() - _start)

    return obj


def ontologies(repository, plain=None):
    """
    
    
    :param repository: 
    :type repository: str
    :param plain: 
    :type plain: bool

    :rtype: Ontologies
    """
    # return 'do some magic!'

    module = modules.get(repository)
    obj = []

    if not module:
        return Error(error='No repository', status='404')

    _start = time.time()

    try:
        module_api = module.ResourcesApi()
        response = module_api.ontologies()

        path = module.Meta().ontology_xpath
        get_ontologies = operator.attrgetter(path)

        ontologies = get_ontologies(response)

        if response.page and response.page.total_pages:
            next_page = response.page.number + 1
            total_pages = response.page.total_pages
            for page in range(next_page, total_pages):
                _next = module_api.ontologies(page=page)
                ontologies.extend(get_ontologies(_next))

        meta = module.MetaOntology()

        for item in ontologies:
            resp = Ontology()
            for attr in resp.attribute_map:
                path = getattr(meta, attr, False)
                if not path:
                    continue
                get_value = operator.attrgetter(path)
                setattr(resp, attr, get_value(item))
                # 
                resp.httpschema_orgrepository = JsonldId(id=repository)
            obj.append(resp)

    except AttributeError as e:
        print("Exception when parsing API: %s\n" % e)
    except module.rest.ApiException as e:
        print("Exception when calling API: %s\n" % e)

    print('request process time:', time.time() - _start)

    return obj


def repositories():
    """
    
    

    :rtype: Repositories
    """
    # return 'do some magic!'
    obj = []

    for item, module in iteritems(modules):
        resp = Repository(name=item, url=module.configuration.host)
        obj.append(resp)

    return obj