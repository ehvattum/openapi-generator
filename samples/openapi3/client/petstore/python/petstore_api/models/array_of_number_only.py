# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ArrayOfNumberOnly(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'array_number': 'list[float]'
    }

    attribute_map = {
        'array_number': 'ArrayNumber'
    }

    def __init__(self, array_number=None):  # noqa: E501
        """ArrayOfNumberOnly - a model defined in OpenAPI"""  # noqa: E501

        self._array_number = None
        self.discriminator = None

        if array_number is not None:
            self.array_number = array_number

    @property
    def array_number(self):
        """Gets the array_number of this ArrayOfNumberOnly.  # noqa: E501


        :return: The array_number of this ArrayOfNumberOnly.  # noqa: E501
        :rtype: list[float]
        """
        return self._array_number

    @array_number.setter
    def array_number(self, array_number):
        """Sets the array_number of this ArrayOfNumberOnly.


        :param array_number: The array_number of this ArrayOfNumberOnly.  # noqa: E501
        :type: list[float]
        """

        self._array_number = array_number

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ArrayOfNumberOnly):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
