# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class JsonldId(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id: str=None):
        """
        JsonldId - a model defined in Swagger

        :param id: The id of this JsonldId.
        :type id: str
        """
        self.swagger_types = {
            'id': str
        }

        self.attribute_map = {
            'id': '@id'
        }

        self._id = id

    @classmethod
    def from_dict(cls, dikt) -> 'JsonldId':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The jsonld_id of this JsonldId.
        :rtype: JsonldId
        """
        return deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """
        Gets the id of this JsonldId.

        :return: The id of this JsonldId.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """
        Sets the id of this JsonldId.

        :param id: The id of this JsonldId.
        :type id: str
        """

        self._id = id
