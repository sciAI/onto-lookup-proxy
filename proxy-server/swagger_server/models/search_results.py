# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.concept import Concept
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class SearchResults(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, repository: str=None, concept: Concept=None, children: List[Concept]=None, parents: List[Concept]=None):
        """
        SearchResults - a model defined in Swagger

        :param repository: The repository of this SearchResults.
        :type repository: str
        :param concept: The concept of this SearchResults.
        :type concept: Concept
        :param children: The children of this SearchResults.
        :type children: List[Concept]
        :param parents: The parents of this SearchResults.
        :type parents: List[Concept]
        """
        self.swagger_types = {
            'repository': str,
            'concept': Concept,
            'children': List[Concept],
            'parents': List[Concept]
        }

        self.attribute_map = {
            'repository': 'repository',
            'concept': 'concept',
            'children': 'children',
            'parents': 'parents'
        }

        self._repository = repository
        self._concept = concept
        self._children = children
        self._parents = parents

    @classmethod
    def from_dict(cls, dikt) -> 'SearchResults':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The search_results of this SearchResults.
        :rtype: SearchResults
        """
        return deserialize_model(dikt, cls)

    @property
    def repository(self) -> str:
        """
        Gets the repository of this SearchResults.

        :return: The repository of this SearchResults.
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository: str):
        """
        Sets the repository of this SearchResults.

        :param repository: The repository of this SearchResults.
        :type repository: str
        """

        self._repository = repository

    @property
    def concept(self) -> Concept:
        """
        Gets the concept of this SearchResults.

        :return: The concept of this SearchResults.
        :rtype: Concept
        """
        return self._concept

    @concept.setter
    def concept(self, concept: Concept):
        """
        Sets the concept of this SearchResults.

        :param concept: The concept of this SearchResults.
        :type concept: Concept
        """

        self._concept = concept

    @property
    def children(self) -> List[Concept]:
        """
        Gets the children of this SearchResults.

        :return: The children of this SearchResults.
        :rtype: List[Concept]
        """
        return self._children

    @children.setter
    def children(self, children: List[Concept]):
        """
        Sets the children of this SearchResults.

        :param children: The children of this SearchResults.
        :type children: List[Concept]
        """

        self._children = children

    @property
    def parents(self) -> List[Concept]:
        """
        Gets the parents of this SearchResults.

        :return: The parents of this SearchResults.
        :rtype: List[Concept]
        """
        return self._parents

    @parents.setter
    def parents(self, parents: List[Concept]):
        """
        Sets the parents of this SearchResults.

        :param parents: The parents of this SearchResults.
        :type parents: List[Concept]
        """

        self._parents = parents
