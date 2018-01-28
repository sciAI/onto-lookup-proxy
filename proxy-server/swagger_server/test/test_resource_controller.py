# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.concept import Concept
from swagger_server.models.error import Error
from swagger_server.models.ontology import Ontology
from swagger_server.models.repository import Repository
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestResourceController(BaseTestCase):
    """ ResourceController integration test stubs """

    def test_concepts(self):
        """
        Test case for concepts

        
        """
        query_string = [('plain', true)]
        response = self.client.open('//repository/{repository}/ontology/{ontology}/concepts'.format(repository='repository_example', ontology='ontology_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_ontologies(self):
        """
        Test case for ontologies

        
        """
        query_string = [('plain', true)]
        response = self.client.open('//repository/{repository}/ontology'.format(repository='repository_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_repositories(self):
        """
        Test case for repositories

        
        """
        response = self.client.open('//repository',
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
