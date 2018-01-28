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


class Concept(object):
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
        'httpschema_orgontology': 'JsonldId',
        'iri': 'str',
        'label': 'str',
        'description': 'object',
        'short': 'str',
        'synonyms': 'object'
    }

    attribute_map = {
        'httpschema_orgrepository': 'http://schema.org/repository',
        'httpschema_orgontology': 'http://schema.org/ontology',
        'iri': 'iri',
        'label': 'label',
        'description': 'description',
        'short': 'short',
        'synonyms': 'synonyms'
    }

    def __init__(self, httpschema_orgrepository=None, httpschema_orgontology=None, iri=None, label=None, description=None, short=None, synonyms=None):
        """
        Concept - a model defined in Swagger
        """

        self._httpschema_orgrepository = None
        self._httpschema_orgontology = None
        self._iri = None
        self._label = None
        self._description = None
        self._short = None
        self._synonyms = None

        if httpschema_orgrepository is not None:
          self.httpschema_orgrepository = httpschema_orgrepository
        if httpschema_orgontology is not None:
          self.httpschema_orgontology = httpschema_orgontology
        if iri is not None:
          self.iri = iri
        if label is not None:
          self.label = label
        if description is not None:
          self.description = description
        if short is not None:
          self.short = short
        if synonyms is not None:
          self.synonyms = synonyms

    @property
    def httpschema_orgrepository(self):
        """
        Gets the httpschema_orgrepository of this Concept.

        :return: The httpschema_orgrepository of this Concept.
        :rtype: JsonldId
        """
        return self._httpschema_orgrepository

    @httpschema_orgrepository.setter
    def httpschema_orgrepository(self, httpschema_orgrepository):
        """
        Sets the httpschema_orgrepository of this Concept.

        :param httpschema_orgrepository: The httpschema_orgrepository of this Concept.
        :type: JsonldId
        """

        self._httpschema_orgrepository = httpschema_orgrepository

    @property
    def httpschema_orgontology(self):
        """
        Gets the httpschema_orgontology of this Concept.

        :return: The httpschema_orgontology of this Concept.
        :rtype: JsonldId
        """
        return self._httpschema_orgontology

    @httpschema_orgontology.setter
    def httpschema_orgontology(self, httpschema_orgontology):
        """
        Sets the httpschema_orgontology of this Concept.

        :param httpschema_orgontology: The httpschema_orgontology of this Concept.
        :type: JsonldId
        """

        self._httpschema_orgontology = httpschema_orgontology

    @property
    def iri(self):
        """
        Gets the iri of this Concept.

        :return: The iri of this Concept.
        :rtype: str
        """
        return self._iri

    @iri.setter
    def iri(self, iri):
        """
        Sets the iri of this Concept.

        :param iri: The iri of this Concept.
        :type: str
        """

        self._iri = iri

    @property
    def label(self):
        """
        Gets the label of this Concept.

        :return: The label of this Concept.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this Concept.

        :param label: The label of this Concept.
        :type: str
        """

        self._label = label

    @property
    def description(self):
        """
        Gets the description of this Concept.

        :return: The description of this Concept.
        :rtype: object
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Concept.

        :param description: The description of this Concept.
        :type: object
        """

        self._description = description

    @property
    def short(self):
        """
        Gets the short of this Concept.

        :return: The short of this Concept.
        :rtype: str
        """
        return self._short

    @short.setter
    def short(self, short):
        """
        Sets the short of this Concept.

        :param short: The short of this Concept.
        :type: str
        """

        self._short = short

    @property
    def synonyms(self):
        """
        Gets the synonyms of this Concept.

        :return: The synonyms of this Concept.
        :rtype: object
        """
        return self._synonyms

    @synonyms.setter
    def synonyms(self, synonyms):
        """
        Sets the synonyms of this Concept.

        :param synonyms: The synonyms of this Concept.
        :type: object
        """

        self._synonyms = synonyms

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
        if not isinstance(other, Concept):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other