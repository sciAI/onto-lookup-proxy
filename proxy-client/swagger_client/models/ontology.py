# coding: utf-8

"""
    PROXY OLS API

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
        'schemaincluded_in_data_catalog': 'str',
        'id': 'str',
        'type': 'str',
        'dcttitle': 'str',
        'dctdescription': 'str',
        'omvacronym': 'str',
        'owlversion_info': 'str',
        'dctmodified': 'str'
    }

    attribute_map = {
        'schemaincluded_in_data_catalog': 'schema:includedInDataCatalog',
        'id': '@id',
        'type': '@type',
        'dcttitle': 'dct:title',
        'dctdescription': 'dct:description',
        'omvacronym': 'omv:acronym',
        'owlversion_info': 'owl:versionInfo',
        'dctmodified': 'dct:modified'
    }

    def __init__(self, schemaincluded_in_data_catalog=None, id=None, type='http://www.w3.org/2002/07/owl#Ontology', dcttitle=None, dctdescription=None, omvacronym=None, owlversion_info=None, dctmodified=None):
        """
        Ontology - a model defined in Swagger
        """

        self._schemaincluded_in_data_catalog = None
        self._id = None
        self._type = None
        self._dcttitle = None
        self._dctdescription = None
        self._omvacronym = None
        self._owlversion_info = None
        self._dctmodified = None

        if schemaincluded_in_data_catalog is not None:
          self.schemaincluded_in_data_catalog = schemaincluded_in_data_catalog
        if id is not None:
          self.id = id
        if type is not None:
          self.type = type
        if dcttitle is not None:
          self.dcttitle = dcttitle
        if dctdescription is not None:
          self.dctdescription = dctdescription
        if omvacronym is not None:
          self.omvacronym = omvacronym
        if owlversion_info is not None:
          self.owlversion_info = owlversion_info
        if dctmodified is not None:
          self.dctmodified = dctmodified

    @property
    def schemaincluded_in_data_catalog(self):
        """
        Gets the schemaincluded_in_data_catalog of this Ontology.

        :return: The schemaincluded_in_data_catalog of this Ontology.
        :rtype: str
        """
        return self._schemaincluded_in_data_catalog

    @schemaincluded_in_data_catalog.setter
    def schemaincluded_in_data_catalog(self, schemaincluded_in_data_catalog):
        """
        Sets the schemaincluded_in_data_catalog of this Ontology.

        :param schemaincluded_in_data_catalog: The schemaincluded_in_data_catalog of this Ontology.
        :type: str
        """

        self._schemaincluded_in_data_catalog = schemaincluded_in_data_catalog

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
    def dcttitle(self):
        """
        Gets the dcttitle of this Ontology.

        :return: The dcttitle of this Ontology.
        :rtype: str
        """
        return self._dcttitle

    @dcttitle.setter
    def dcttitle(self, dcttitle):
        """
        Sets the dcttitle of this Ontology.

        :param dcttitle: The dcttitle of this Ontology.
        :type: str
        """

        self._dcttitle = dcttitle

    @property
    def dctdescription(self):
        """
        Gets the dctdescription of this Ontology.

        :return: The dctdescription of this Ontology.
        :rtype: str
        """
        return self._dctdescription

    @dctdescription.setter
    def dctdescription(self, dctdescription):
        """
        Sets the dctdescription of this Ontology.

        :param dctdescription: The dctdescription of this Ontology.
        :type: str
        """

        self._dctdescription = dctdescription

    @property
    def omvacronym(self):
        """
        Gets the omvacronym of this Ontology.

        :return: The omvacronym of this Ontology.
        :rtype: str
        """
        return self._omvacronym

    @omvacronym.setter
    def omvacronym(self, omvacronym):
        """
        Sets the omvacronym of this Ontology.

        :param omvacronym: The omvacronym of this Ontology.
        :type: str
        """

        self._omvacronym = omvacronym

    @property
    def owlversion_info(self):
        """
        Gets the owlversion_info of this Ontology.

        :return: The owlversion_info of this Ontology.
        :rtype: str
        """
        return self._owlversion_info

    @owlversion_info.setter
    def owlversion_info(self, owlversion_info):
        """
        Sets the owlversion_info of this Ontology.

        :param owlversion_info: The owlversion_info of this Ontology.
        :type: str
        """

        self._owlversion_info = owlversion_info

    @property
    def dctmodified(self):
        """
        Gets the dctmodified of this Ontology.

        :return: The dctmodified of this Ontology.
        :rtype: str
        """
        return self._dctmodified

    @dctmodified.setter
    def dctmodified(self, dctmodified):
        """
        Sets the dctmodified of this Ontology.

        :param dctmodified: The dctmodified of this Ontology.
        :type: str
        """

        self._dctmodified = dctmodified

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
