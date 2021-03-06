# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Repository(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id: str=None, type: str='http://www.w3.org/ns/dcat#Dataset', dcatlanding_page: str=None, dcttitle: str=None):
        """
        Repository - a model defined in Swagger

        :param id: The id of this Repository.
        :type id: str
        :param type: The type of this Repository.
        :type type: str
        :param dcatlanding_page: The dcatlanding_page of this Repository.
        :type dcatlanding_page: str
        :param dcttitle: The dcttitle of this Repository.
        :type dcttitle: str
        """
        self.swagger_types = {
            'id': str,
            'type': str,
            'dcatlanding_page': str,
            'dcttitle': str
        }

        self.attribute_map = {
            'id': '@id',
            'type': '@type',
            'dcatlanding_page': 'http://www.w3.org/ns/dcat#landingPage',
            'dcttitle': 'http://purl.org/dc/terms/title'
        }

        self._id = id
        self._type = type
        self._dcatlanding_page = dcatlanding_page
        self._dcttitle = dcttitle

    @classmethod
    def from_dict(cls, dikt) -> 'Repository':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The repository of this Repository.
        :rtype: Repository
        """
        return deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """
        Gets the id of this Repository.

        :return: The id of this Repository.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """
        Sets the id of this Repository.

        :param id: The id of this Repository.
        :type id: str
        """

        self._id = id

    @property
    def type(self) -> str:
        """
        Gets the type of this Repository.

        :return: The type of this Repository.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """
        Sets the type of this Repository.

        :param type: The type of this Repository.
        :type type: str
        """

        self._type = type

    @property
    def dcatlanding_page(self) -> str:
        """
        Gets the dcatlanding_page of this Repository.

        :return: The dcatlanding_page of this Repository.
        :rtype: str
        """
        return self._dcatlanding_page

    @dcatlanding_page.setter
    def dcatlanding_page(self, dcatlanding_page: str):
        """
        Sets the dcatlanding_page of this Repository.

        :param dcatlanding_page: The dcatlanding_page of this Repository.
        :type dcatlanding_page: str
        """

        self._dcatlanding_page = dcatlanding_page

    @property
    def dcttitle(self) -> str:
        """
        Gets the dcttitle of this Repository.

        :return: The dcttitle of this Repository.
        :rtype: str
        """
        return self._dcttitle

    @dcttitle.setter
    def dcttitle(self, dcttitle: str):
        """
        Sets the dcttitle of this Repository.

        :param dcttitle: The dcttitle of this Repository.
        :type dcttitle: str
        """

        self._dcttitle = dcttitle

