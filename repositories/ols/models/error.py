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


class Error(object):
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
        'error': 'str',
        'message': 'str',
        'path': 'str',
        'status': 'int',
        'timestamp': 'int'
    }

    attribute_map = {
        'error': 'error',
        'message': 'message',
        'path': 'path',
        'status': 'status',
        'timestamp': 'timestamp'
    }

    def __init__(self, error=None, message=None, path=None, status=None, timestamp=None):
        """
        Error - a model defined in Swagger
        """

        self._error = None
        self._message = None
        self._path = None
        self._status = None
        self._timestamp = None

        if error is not None:
          self.error = error
        if message is not None:
          self.message = message
        if path is not None:
          self.path = path
        if status is not None:
          self.status = status
        if timestamp is not None:
          self.timestamp = timestamp

    @property
    def error(self):
        """
        Gets the error of this Error.

        :return: The error of this Error.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this Error.

        :param error: The error of this Error.
        :type: str
        """

        self._error = error

    @property
    def message(self):
        """
        Gets the message of this Error.

        :return: The message of this Error.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this Error.

        :param message: The message of this Error.
        :type: str
        """

        self._message = message

    @property
    def path(self):
        """
        Gets the path of this Error.

        :return: The path of this Error.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this Error.

        :param path: The path of this Error.
        :type: str
        """

        self._path = path

    @property
    def status(self):
        """
        Gets the status of this Error.

        :return: The status of this Error.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Error.

        :param status: The status of this Error.
        :type: int
        """

        self._status = status

    @property
    def timestamp(self):
        """
        Gets the timestamp of this Error.

        :return: The timestamp of this Error.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this Error.

        :param timestamp: The timestamp of this Error.
        :type: int
        """

        self._timestamp = timestamp

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
        if not isinstance(other, Error):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
