import connexion
from swagger_server.models.concept import Concept
from swagger_server.models.concepts import Concepts
from swagger_server.models.error import Error
from swagger_server.models.search import Search
from swagger_server.models.search_results import SearchResults
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

import os
import imp
import operator
import time
import urllib


dir_path = os.path.dirname(os.path.realpath(__file__))
rep_path = os.path.join(dir_path, 'repositories')

modules = {}


for item in os.listdir(rep_path):
    path = os.path.join(rep_path, item)
    fp, pathname, description = imp.find_module(path);

    module = imp.load_module(item, fp, pathname, description);
    modules.setdefault(module.__name__, module)


def search(query):
    """
    
    
    :param query: 
    :type query: str

    :rtype: List[Search]
    """
    # return 'do some magic!'
    obj = []

    for item, module in iteritems(modules):

        try:
            module_api = module.SearchApi()
            response = module_api.search(query)

            path = module.Meta().search_xpath
            get_objects = operator.attrgetter(path)

            concepts = get_objects(response) if path else response

            page = getattr(response, 'page', False)
            if page:
                next_page = getattr(page, 'number', response.page) + 1
                total_pages = getattr(page, 'total_pages',
                    getattr(response, 'page_count', 0))
                for page in range(next_page, total_pages):
                    _next = module_api.search(query, page=page)
                    concepts.extend(get_objects(_next))
            else:
                # OLS PoC, to be refactored
                head = getattr(response, 'response_header', False)
                step = int(head.get('params').get('rows')) if head else 10
                rows = response
                for name in ['response', 'num_found']:
                    rows = getattr(rows, name)
                for page in range(step, rows, step):
                    _next = module_api.search(query, start=page)
                    concepts.extend(get_objects(_next))

            meta = module.MetaConcept()

            for item in concepts:
                resp = Concept()
                for attr, _obj in resp.swagger_types.items():
                    path = getattr(meta, attr, False)
                    if not path:
                        continue
                    get_value = operator.attrgetter(path)
                    try:
                        setattr(resp, attr, get_value(item))
                    except:
                        pass
                obj.append(SearchResults(
                    repository=module.__name__,
                    concept=resp,
                ))

        except AttributeError as e:
            print("Exception when parsing API: %s\n" % e)
        except module.rest.ApiException as e:
            print("Exception when calling API: %s\n" % e)

    return Search(query=query, results=obj)


def select(ontology, iri, fields=[]):
    """
    
    
    :param ontology: 
    :type ontology: str
    :param iri: 
    :type iri: str
    :param fields: 
    :type fields: List[str]

    :rtype: List[Search]
    """
    # return 'do some magic!'
    obj = []

    for item, module in iteritems(modules):

        try:
            module_api = module.ResourcesApi()

            # OLS PoC, to be refactored
            if 'ols' == module.__name__:
                qri = urllib.parse.quote(iri, safe='')
            else:
                qri = iri

            response = module_api.concept(ontology, qri)

            meta = module.MetaConcept()

            resp = Concept()
            for attr, _obj in resp.swagger_types.items():
                path = getattr(meta, attr, False)
                if not path:
                    continue
                get_value = operator.attrgetter(path)
                try:
                    setattr(resp, attr, get_value(response))
                except:
                    pass
            children = select_children(module, ontology, iri) \
                if 'children' in fields else []
            parents = select_parents(module, ontology, iri) \
                if 'parents' in fields else []

            obj.append(SearchResults(
                repository=module.__name__,
                concept=resp,
                children=children,
                parents=parents,
            ))

        except AttributeError as e:
            print("Exception when parsing API: %s\n" % e)
        except module.rest.ApiException as e:
            print("Exception when calling API: %s\n" % e)

    return Search(query=iri, results=obj)


def select_children(module, ontology, iri):
    """
    
    
    :param query: 
    :type query: str

    :rtype: List[Search]
    """
    # return 'do some magic!'
    obj = []

    try:
        module_api = module.ResourcesApi()

        if not getattr(module_api, 'children', None):
            return obj

        # OLS PoC, to be refactored
        if 'ols' == module.__name__:
            qri = urllib.parse.quote(iri, safe='')
        else:
            qri = iri

        path = module.Meta().concept_xpath
        meta = module.MetaConcept()

        get_objects = operator.attrgetter(path)

        pages = list(range(0, 1))

        for page in pages:
            if not page:
                _next = module_api.children(ontology, qri)
                _page_count = getattr(_next, 'page_count', 0)

                if _page_count:
                    pages.extend(list(range(2, _page_count + 1)))
                else:
                    _page = getattr(_next, 'page', False)
                    _total_pages = getattr(_page, 'total_pages', 0)
                    pages.extend(list(range(1, _total_pages)))
            else:
                _next = module_api.children(ontology, qri, page=page)

            concepts = get_objects(_next) if path else _next

            for item in concepts:
                resp = Concept()
                for attr, _obj in resp.swagger_types.items():
                    path = getattr(meta, attr, False)
                    if not path:
                        continue
                    get_value = operator.attrgetter(path)
                    try:
                        setattr(resp, attr, get_value(item))
                    except:
                        pass
                obj.append(resp)

    except AttributeError as e:
        print("Exception when parsing API: %s\n" % e)
    except module.rest.ApiException as e:
        print("Exception when calling API: %s\n" % e)

    return obj


def select_parents(module, ontology, iri):
    """
    
    
    :param query: 
    :type query: str

    :rtype: List[Search]
    """
    # return 'do some magic!'
    obj = []

    try:
        module_api = module.ResourcesApi()

        if not getattr(module_api, 'parents', None):
            return obj

        # OLS PoC, to be refactored
        if 'ols' == module.__name__:
            qri = urllib.parse.quote(iri, safe='')
        else:
            qri = iri

        response = module_api.parents(ontology, qri)

        # OLS PoC, to be refactored
        if 'ols' == module.__name__:
            path = module.Meta().concept_xpath
            get_objects = operator.attrgetter(path)
            response = get_objects(response)
        else:
            response = response

        meta = module.MetaConcept()

        for item in response:
            resp = Concept()
            for attr, _obj in resp.swagger_types.items():
                path = getattr(meta, attr, False)
                if not path:
                    continue
                get_value = operator.attrgetter(path)
                try:
                    setattr(resp, attr, get_value(item))
                except:
                    pass
            obj.append(resp)

    except AttributeError as e:
        print("Exception when parsing API: %s\n" % e)
    except module.rest.ApiException as e:
        print("Exception when calling API: %s\n" % e)

    return obj
