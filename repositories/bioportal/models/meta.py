# coding: utf-8

"""
    NCBO BioPortal API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Meta(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'ontology_xpath': 'str',
        'ontology': 'MetaOntology',
        'concept_xpath': 'str',
        'concept': 'MetaConcept',
        'search_xpath': 'str',
        'search': 'MetaConcept',
        'pages': 'MetaPages'
    }

    attribute_map = {
        'ontology_xpath': 'ontology_xpath',
        'ontology': 'ontology',
        'concept_xpath': 'concept_xpath',
        'concept': 'concept',
        'search_xpath': 'search_xpath',
        'search': 'search',
        'pages': 'pages'
    }

    def __init__(self, ontology_xpath='', ontology=None, concept_xpath='collection', concept=None, search_xpath='collection', search=None, pages=None):
        """
        Meta - a model defined in Swagger
        """

        self._ontology_xpath = None
        self._ontology = None
        self._concept_xpath = None
        self._concept = None
        self._search_xpath = None
        self._search = None
        self._pages = None

        if ontology_xpath is not None:
          self.ontology_xpath = ontology_xpath
        if ontology is not None:
          self.ontology = ontology
        if concept_xpath is not None:
          self.concept_xpath = concept_xpath
        if concept is not None:
          self.concept = concept
        if search_xpath is not None:
          self.search_xpath = search_xpath
        if search is not None:
          self.search = search
        if pages is not None:
          self.pages = pages

    @property
    def ontology_xpath(self):
        """
        Gets the ontology_xpath of this Meta.

        :return: The ontology_xpath of this Meta.
        :rtype: str
        """
        return self._ontology_xpath

    @ontology_xpath.setter
    def ontology_xpath(self, ontology_xpath):
        """
        Sets the ontology_xpath of this Meta.

        :param ontology_xpath: The ontology_xpath of this Meta.
        :type: str
        """

        self._ontology_xpath = ontology_xpath

    @property
    def ontology(self):
        """
        Gets the ontology of this Meta.

        :return: The ontology of this Meta.
        :rtype: MetaOntology
        """
        return self._ontology

    @ontology.setter
    def ontology(self, ontology):
        """
        Sets the ontology of this Meta.

        :param ontology: The ontology of this Meta.
        :type: MetaOntology
        """

        self._ontology = ontology

    @property
    def concept_xpath(self):
        """
        Gets the concept_xpath of this Meta.

        :return: The concept_xpath of this Meta.
        :rtype: str
        """
        return self._concept_xpath

    @concept_xpath.setter
    def concept_xpath(self, concept_xpath):
        """
        Sets the concept_xpath of this Meta.

        :param concept_xpath: The concept_xpath of this Meta.
        :type: str
        """

        self._concept_xpath = concept_xpath

    @property
    def concept(self):
        """
        Gets the concept of this Meta.

        :return: The concept of this Meta.
        :rtype: MetaConcept
        """
        return self._concept

    @concept.setter
    def concept(self, concept):
        """
        Sets the concept of this Meta.

        :param concept: The concept of this Meta.
        :type: MetaConcept
        """

        self._concept = concept

    @property
    def search_xpath(self):
        """
        Gets the search_xpath of this Meta.

        :return: The search_xpath of this Meta.
        :rtype: str
        """
        return self._search_xpath

    @search_xpath.setter
    def search_xpath(self, search_xpath):
        """
        Sets the search_xpath of this Meta.

        :param search_xpath: The search_xpath of this Meta.
        :type: str
        """

        self._search_xpath = search_xpath

    @property
    def search(self):
        """
        Gets the search of this Meta.

        :return: The search of this Meta.
        :rtype: MetaConcept
        """
        return self._search

    @search.setter
    def search(self, search):
        """
        Sets the search of this Meta.

        :param search: The search of this Meta.
        :type: MetaConcept
        """

        self._search = search

    @property
    def pages(self):
        """
        Gets the pages of this Meta.

        :return: The pages of this Meta.
        :rtype: MetaPages
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """
        Sets the pages of this Meta.

        :param pages: The pages of this Meta.
        :type: MetaPages
        """

        self._pages = pages

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Meta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
