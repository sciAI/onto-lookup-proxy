# coding: utf-8

"""
    EBI OLS API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class OntologyConfig(object):
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
        'title': 'str',
        'namespace': 'str',
        'description': 'str',
        'version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'namespace': 'namespace',
        'description': 'description',
        'version': 'version'
    }

    def __init__(self, id=None, title=None, namespace=None, description=None, version=None):
        """
        OntologyConfig - a model defined in Swagger
        """

        self._id = None
        self._title = None
        self._namespace = None
        self._description = None
        self._version = None

        if id is not None:
          self.id = id
        if title is not None:
          self.title = title
        if namespace is not None:
          self.namespace = namespace
        if description is not None:
          self.description = description
        if version is not None:
          self.version = version

    @property
    def id(self):
        """
        Gets the id of this OntologyConfig.

        :return: The id of this OntologyConfig.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OntologyConfig.

        :param id: The id of this OntologyConfig.
        :type: str
        """

        self._id = id

    @property
    def title(self):
        """
        Gets the title of this OntologyConfig.

        :return: The title of this OntologyConfig.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this OntologyConfig.

        :param title: The title of this OntologyConfig.
        :type: str
        """

        self._title = title

    @property
    def namespace(self):
        """
        Gets the namespace of this OntologyConfig.

        :return: The namespace of this OntologyConfig.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this OntologyConfig.

        :param namespace: The namespace of this OntologyConfig.
        :type: str
        """

        self._namespace = namespace

    @property
    def description(self):
        """
        Gets the description of this OntologyConfig.

        :return: The description of this OntologyConfig.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this OntologyConfig.

        :param description: The description of this OntologyConfig.
        :type: str
        """

        self._description = description

    @property
    def version(self):
        """
        Gets the version of this OntologyConfig.

        :return: The version of this OntologyConfig.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this OntologyConfig.

        :param version: The version of this OntologyConfig.
        :type: str
        """

        self._version = version

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
        if not isinstance(other, OntologyConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
