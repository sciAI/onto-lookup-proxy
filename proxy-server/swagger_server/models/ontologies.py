# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.ontology import Ontology
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Ontologies(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Ontologies - a model defined in Swagger

        """
        self.swagger_types = {
            
        }

        self.attribute_map = {
            
        }


    @classmethod
    def from_dict(cls, dikt) -> 'Ontologies':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ontologies of this Ontologies.
        :rtype: Ontologies
        """
        return deserialize_model(dikt, cls)