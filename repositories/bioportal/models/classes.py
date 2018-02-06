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


class Classes(object):
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
        'collection': 'list[ModelClass]',
        'page': 'int',
        'page_count': 'int',
        'total_count': 'int',
        'links': 'Links'
    }

    attribute_map = {
        'collection': 'collection',
        'page': 'page',
        'page_count': 'pageCount',
        'total_count': 'totalCount',
        'links': 'links'
    }

    def __init__(self, collection=None, page=None, page_count=None, total_count=None, links=None):
        """
        Classes - a model defined in Swagger
        """

        self._collection = None
        self._page = None
        self._page_count = None
        self._total_count = None
        self._links = None

        if collection is not None:
          self.collection = collection
        if page is not None:
          self.page = page
        if page_count is not None:
          self.page_count = page_count
        if total_count is not None:
          self.total_count = total_count
        if links is not None:
          self.links = links

    @property
    def collection(self):
        """
        Gets the collection of this Classes.

        :return: The collection of this Classes.
        :rtype: list[ModelClass]
        """
        return self._collection

    @collection.setter
    def collection(self, collection):
        """
        Sets the collection of this Classes.

        :param collection: The collection of this Classes.
        :type: list[ModelClass]
        """

        self._collection = collection

    @property
    def page(self):
        """
        Gets the page of this Classes.

        :return: The page of this Classes.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """
        Sets the page of this Classes.

        :param page: The page of this Classes.
        :type: int
        """

        self._page = page

    @property
    def page_count(self):
        """
        Gets the page_count of this Classes.

        :return: The page_count of this Classes.
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """
        Sets the page_count of this Classes.

        :param page_count: The page_count of this Classes.
        :type: int
        """

        self._page_count = page_count

    @property
    def total_count(self):
        """
        Gets the total_count of this Classes.

        :return: The total_count of this Classes.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this Classes.

        :param total_count: The total_count of this Classes.
        :type: int
        """

        self._total_count = total_count

    @property
    def links(self):
        """
        Gets the links of this Classes.

        :return: The links of this Classes.
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this Classes.

        :param links: The links of this Classes.
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
        if not isinstance(other, Classes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other