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


class SearchResponse(object):
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
        'num_found': 'int',
        'start': 'int',
        'docs': 'list[ModelClass]'
    }

    attribute_map = {
        'num_found': 'numFound',
        'start': 'start',
        'docs': 'docs'
    }

    def __init__(self, num_found=None, start=None, docs=None):
        """
        SearchResponse - a model defined in Swagger
        """

        self._num_found = None
        self._start = None
        self._docs = None

        if num_found is not None:
          self.num_found = num_found
        if start is not None:
          self.start = start
        if docs is not None:
          self.docs = docs

    @property
    def num_found(self):
        """
        Gets the num_found of this SearchResponse.

        :return: The num_found of this SearchResponse.
        :rtype: int
        """
        return self._num_found

    @num_found.setter
    def num_found(self, num_found):
        """
        Sets the num_found of this SearchResponse.

        :param num_found: The num_found of this SearchResponse.
        :type: int
        """

        self._num_found = num_found

    @property
    def start(self):
        """
        Gets the start of this SearchResponse.

        :return: The start of this SearchResponse.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """
        Sets the start of this SearchResponse.

        :param start: The start of this SearchResponse.
        :type: int
        """

        self._start = start

    @property
    def docs(self):
        """
        Gets the docs of this SearchResponse.

        :return: The docs of this SearchResponse.
        :rtype: list[ModelClass]
        """
        return self._docs

    @docs.setter
    def docs(self, docs):
        """
        Sets the docs of this SearchResponse.

        :param docs: The docs of this SearchResponse.
        :type: list[ModelClass]
        """

        self._docs = docs

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
        if not isinstance(other, SearchResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
