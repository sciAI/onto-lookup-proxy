# coding: utf-8

"""
    IBC AgroPortal API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Ontology(object):
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
        'id': 'str',
        'type': 'str',
        'acronym': 'str',
        'name': 'str',
        'ontology_type': 'str',
        'links': 'Links'
    }

    attribute_map = {
        'id': '@id',
        'type': '@type',
        'acronym': 'acronym',
        'name': 'name',
        'ontology_type': 'ontologyType',
        'links': 'links'
    }

    def __init__(self, id=None, type=None, acronym=None, name=None, ontology_type=None, links=None):
        """
        Ontology - a model defined in Swagger
        """

        self._id = None
        self._type = None
        self._acronym = None
        self._name = None
        self._ontology_type = None
        self._links = None

        if id is not None:
          self.id = id
        if type is not None:
          self.type = type
        if acronym is not None:
          self.acronym = acronym
        if name is not None:
          self.name = name
        if ontology_type is not None:
          self.ontology_type = ontology_type
        if links is not None:
          self.links = links

    @property
    def id(self):
        """
        Gets the id of this Ontology.

        :return: The id of this Ontology.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Ontology.

        :param id: The id of this Ontology.
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """
        Gets the type of this Ontology.

        :return: The type of this Ontology.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Ontology.

        :param type: The type of this Ontology.
        :type: str
        """

        self._type = type

    @property
    def acronym(self):
        """
        Gets the acronym of this Ontology.

        :return: The acronym of this Ontology.
        :rtype: str
        """
        return self._acronym

    @acronym.setter
    def acronym(self, acronym):
        """
        Sets the acronym of this Ontology.

        :param acronym: The acronym of this Ontology.
        :type: str
        """

        self._acronym = acronym

    @property
    def name(self):
        """
        Gets the name of this Ontology.

        :return: The name of this Ontology.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Ontology.

        :param name: The name of this Ontology.
        :type: str
        """

        self._name = name

    @property
    def ontology_type(self):
        """
        Gets the ontology_type of this Ontology.

        :return: The ontology_type of this Ontology.
        :rtype: str
        """
        return self._ontology_type

    @ontology_type.setter
    def ontology_type(self, ontology_type):
        """
        Sets the ontology_type of this Ontology.

        :param ontology_type: The ontology_type of this Ontology.
        :type: str
        """

        self._ontology_type = ontology_type

    @property
    def links(self):
        """
        Gets the links of this Ontology.

        :return: The links of this Ontology.
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this Ontology.

        :param links: The links of this Ontology.
        :type: Links
        """

        self._links = links

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
        if not isinstance(other, Ontology):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
