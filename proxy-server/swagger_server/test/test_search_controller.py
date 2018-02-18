# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.error import Error
from swagger_server.models.search import Search
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestSearchController(BaseTestCase):
    """ SearchController integration test stubs """

    def test_search(self):
        """
        Test case for search

        
        """
        query_string = [('query', 'query_example')]
        response = self.client.open('//search',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
