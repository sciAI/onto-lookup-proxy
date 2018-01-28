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
        'httpschema_orgrepository': 'JsonldId',
        'iri': 'str',
        'name': 'str',
        'description': 'str',
        'acronym': 'str',
        'version': 'str',
        'date': 'str'
    }

    attribute_map = {
        'httpschema_orgrepository': 'http://schema.org/repository',
        'iri': 'iri',
        'name': 'name',
        'description': 'description',
        'acronym': 'acronym',
        'version': 'version',
        'date': 'date'
    }

    def __init__(self, httpschema_orgrepository=None, iri=None, name=None, description=None, acronym=None, version=None, date=None):
        """
        Ontology - a model defined in Swagger
        """

        self._httpschema_orgrepository = None
        self._iri = None
        self._name = None
        self._description = None
        self._acronym = None
        self._version = None
        self._date = None

        if httpschema_orgrepository is not None:
          self.httpschema_orgrepository = httpschema_orgrepository
        if iri is not None:
          self.iri = iri
        if name is not None:
          self.name = name
        if description is not None:
          self.description = description
        if acronym is not None:
          self.acronym = acronym
        if version is not None:
          self.version = version
        if date is not None:
          self.date = date

    @property
    def httpschema_orgrepository(self):
        """
        Gets the httpschema_orgrepository of this Ontology.

        :return: The httpschema_orgrepository of this Ontology.
        :rtype: JsonldId
        """
        return self._httpschema_orgrepository

    @httpschema_orgrepository.setter
    def httpschema_orgrepository(self, httpschema_orgrepository):
        """
        Sets the httpschema_orgrepository of this Ontology.

        :param httpschema_orgrepository: The httpschema_orgrepository of this Ontology.
        :type: JsonldId
        """

        self._httpschema_orgrepository = httpschema_orgrepository

    @property
    def iri(self):
        """
        Gets the iri of this Ontology.

        :return: The iri of this Ontology.
        :rtype: str
        """
        return self._iri

    @iri.setter
    def iri(self, iri):
        """
        Sets the iri of this Ontology.

        :param iri: The iri of this Ontology.
        :type: str
        """

        self._iri = iri

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
    def description(self):
        """
        Gets the description of this Ontology.

        :return: The description of this Ontology.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Ontology.

        :param description: The description of this Ontology.
        :type: str
        """

        self._description = description

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
    def version(self):
        """
        Gets the version of this Ontology.

        :return: The version of this Ontology.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this Ontology.

        :param version: The version of this Ontology.
        :type: str
        """

        self._version = version

    @property
    def date(self):
        """
        Gets the date of this Ontology.

        :return: The date of this Ontology.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """
        Sets the date of this Ontology.

        :param date: The date of this Ontology.
        :type: str
        """

        self._date = date

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
