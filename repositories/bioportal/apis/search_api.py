# coding: utf-8

"""
    NCBO BioPortal API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class SearchApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def search(self, q, **kwargs):
        """
        
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.search(q, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str q:  (required)
        :param list[str] ontologies: 
        :param str type: 
        :param list[str] field_list: 
        :param list[str] include: 
        :param bool require_exact_match: 
        :param bool require_definitions: 
        :param bool also_search_properties: 
        :param bool also_search_obsolete: 
        :param int page: 
        :return: Classes
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.search_with_http_info(q, **kwargs)
        else:
            (data) = self.search_with_http_info(q, **kwargs)
            return data

    def search_with_http_info(self, q, **kwargs):
        """
        
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.search_with_http_info(q, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str q:  (required)
        :param list[str] ontologies: 
        :param str type: 
        :param list[str] field_list: 
        :param list[str] include: 
        :param bool require_exact_match: 
        :param bool require_definitions: 
        :param bool also_search_properties: 
        :param bool also_search_obsolete: 
        :param int page: 
        :return: Classes
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['q', 'ontologies', 'type', 'field_list', 'include', 'require_exact_match', 'require_definitions', 'also_search_properties', 'also_search_obsolete', 'page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'q' is set
        if ('q' not in params) or (params['q'] is None):
            raise ValueError("Missing the required parameter `q` when calling `search`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'q' in params:
            query_params.append(('q', params['q']))
        if 'ontologies' in params:
            query_params.append(('ontologies', params['ontologies']))
            collection_formats['ontologies'] = 'multi'
        if 'type' in params:
            query_params.append(('type', params['type']))
        if 'field_list' in params:
            query_params.append(('fieldList', params['field_list']))
            collection_formats['fieldList'] = 'multi'
        if 'include' in params:
            query_params.append(('include', params['include']))
            collection_formats['include'] = 'multi'
        if 'require_exact_match' in params:
            query_params.append(('require_exact_match', params['require_exact_match']))
        if 'require_definitions' in params:
            query_params.append(('require_definitions', params['require_definitions']))
        if 'also_search_properties' in params:
            query_params.append(('also_search_properties', params['also_search_properties']))
        if 'also_search_obsolete' in params:
            query_params.append(('also_search_obsolete', params['also_search_obsolete']))
        if 'page' in params:
            query_params.append(('page', params['page']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apikey']

        return self.api_client.call_api('/search', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Classes',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
