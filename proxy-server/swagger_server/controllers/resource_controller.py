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

from . import harvester

import json
import os
import imp
import operator
import time
import threading
import queue


dir_path = os.path.dirname(os.path.realpath(__file__))
rep_path = os.path.join(dir_path, 'repositories')

modules = {}
threads = {}
queues = {}


for item in os.listdir(rep_path):
    path = os.path.join(rep_path, item)
    fp, pathname, description = imp.find_module(path);

    module = imp.load_module(item, fp, pathname, description);
    modules.setdefault(module.__name__, module)
    queues.setdefault(module.__name__, queue.Queue())


def __concepts(module):
    """
    
    
    :param module: 
    """
    _queue = queues.get(module.__name__)

    while True:
        remote, ontology = _queue.get()
        remote = 'http://' + remote + ''

        try:
            module_api = module.ResourcesApi()
            client_api = harvester.ResourceApi(
                harvester.ApiClient(host=remote))

            path = module.Meta().concept_xpath
            meta = module.MetaConcept()

            get_objects = operator.attrgetter(path)

            pages = list(range(0, 1))

            for page in pages:
                if not page:
                    _next = module_api.concepts(ontology)
                    _page_count = getattr(_next, 'page_count', 0)

                    if _page_count:
                        pages.extend(list(range(2, _page_count + 1)))
                    else:
                        _page = getattr(_next, 'page', False)
                        _total_pages = getattr(_page, 'total_pages', 0)
                        pages.extend(list(range(1, _total_pages)))
                else:
                    _next = module_api.concepts(ontology, page=page)

                concepts = get_objects(_next) if path else _next

                for item in concepts:
                    resp = Concept()
                    for attr, _obj in resp.swagger_types.items():
                        path = getattr(meta, attr, False)
                        if not path:
                            continue
                        get_value = operator.attrgetter(path)
                        setattr(resp, attr, get_value(item))

                    client_api.insert(resp)

        except AttributeError as e:
            print("Exception when parsing API: %s\n" % e)
        except module.rest.ApiException as e:
            print("Exception when calling API: %s\n" % e)

        print(module.__name__, ontology)
        _queue.task_done()


for _name, module in modules.items():
    thread = threading.Thread(target=__concepts, args=(module, ))
    thread.start()
    threads.setdefault(_name, [thread])

def concepts(repository, ontology):
    """
    
    
    :param repository: 
    :type repository: str
    :param ontology: 
    :type ontology: str

    :rtype: List[Concept]
    """
    # return 'do some magic!'

    module = modules.get(repository)
    obj = []

    if not module:
        return Error(error='No repository', status='404')

    _start = time.time()

    if 'Swagger-Codegen' in connexion.request.environ['HTTP_USER_AGENT']:
        # thread = threading.Thread(target=__concepts,
        #                           args=(connexion.request.environ,
        #                                 module,
        #                                 ontology))
        # thread.start()
        _queue = queues.get(repository)
        _queue.put((connexion.request.environ['REMOTE_ADDR'], ontology))
        return 'OK', 200

    try:
        module_api = module.ResourcesApi()
        response = module_api.concepts(ontology)

        path = module.Meta().concept_xpath
        get_objects = operator.attrgetter(path)

        concepts = get_objects(response) if path else response

        page = getattr(response, 'page', False)
        if page:
            next_page = getattr(page, 'number', response.page) + 1
            total_pages = getattr(page, 'total_pages',
                getattr(response, 'page_count', 0))
            # limit for PoC only!
            if total_pages > 100:
                return Error(error='PoC Limit Exceeded: there are %s pages \
                    in %s ontology' % (total_pages, ontology), status=500)
            for page in range(next_page, total_pages):
                _next = module_api.concepts(ontology, page=page)
                concepts.extend(get_objects(_next))

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
            obj.append(resp)

    except AttributeError as e:
        print("Exception when parsing API: %s\n" % e)
    except module.rest.ApiException as e:
        print("Exception when calling API: %s\n" % e)

    print('request process time:', time.time() - _start)

    return obj


def ontologies(repository):
    """
    
    
    :param repository: 
    :type repository: str

    :rtype: List[Ontology]
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

        ontologies = get_ontologies(response) if path else response

        page = getattr(response, 'page', False)
        if page:
            next_page = getattr(page, 'number', response.page) + 1
            total_pages = getattr(page, 'total_pages',
                getattr(response, 'page_count', 0))
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
                resp.schemaincluded_in_data_catalog = repository
            obj.append(resp)

    except AttributeError as e:
        print("Exception when parsing API: %s\n" % e)
    except module.rest.ApiException as e:
        print("Exception when calling API: %s\n" % e)

    print('request process time:', time.time() - _start)

    return obj


def repositories():
    """
    
    

    :rtype: List[Repository]
    """
    # return 'do some magic!'
    obj = []

    for item, module in iteritems(modules):
        resp = Repository(id=item, dcttitle=item,
            dcatlanding_page=module.configuration.host)
        obj.append(resp)

    return obj


def metadata(repository, ontology):
    """
    
    
    :param repository: 
    :type repository: str
    :param ontology: 
    :type ontology: str

    :rtype: object
    """
    # return 'do some magic!'

    module = modules.get(repository)

    if not module:
        return Error(error='No repository', status='404')

    try:
        module_api = module.ResourcesApi()
        response = module_api.ontology(ontology)

    except module.rest.ApiException as e:
        print("Exception when calling API: %s\n" % e)

    return response.to_dict()
