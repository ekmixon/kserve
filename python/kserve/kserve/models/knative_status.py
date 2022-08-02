#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

"""
    KServe

    Python SDK for KServe  # noqa: E501

    OpenAPI spec version: v0.1

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from kserve.models.knative_condition import KnativeCondition  # noqa: F401,E501


class KnativeStatus(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'conditions': 'list[KnativeCondition]',
        'observed_generation': 'int'
    }

    attribute_map = {
        'conditions': 'conditions',
        'observed_generation': 'observedGeneration'
    }

    def __init__(self, conditions=None, observed_generation=None):  # noqa: E501
        """KnativeStatus - a model defined in Swagger"""  # noqa: E501

        self._conditions = None
        self._observed_generation = None
        self.discriminator = None

        if conditions is not None:
            self.conditions = conditions
        if observed_generation is not None:
            self.observed_generation = observed_generation

    @property
    def conditions(self):
        """Gets the conditions of this KnativeStatus.  # noqa: E501

        Conditions the latest available observations of a resource's current state.  # noqa: E501

        :return: The conditions of this KnativeStatus.  # noqa: E501
        :rtype: list[KnativeCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this KnativeStatus.

        Conditions the latest available observations of a resource's current state.  # noqa: E501

        :param conditions: The conditions of this KnativeStatus.  # noqa: E501
        :type: list[KnativeCondition]
        """

        self._conditions = conditions

    @property
    def observed_generation(self):
        """Gets the observed_generation of this KnativeStatus.  # noqa: E501

        ObservedGeneration is the 'Generation' of the Service that was last processed by the controller.  # noqa: E501

        :return: The observed_generation of this KnativeStatus.  # noqa: E501
        :rtype: int
        """
        return self._observed_generation

    @observed_generation.setter
    def observed_generation(self, observed_generation):
        """Sets the observed_generation of this KnativeStatus.

        ObservedGeneration is the 'Generation' of the Service that was last processed by the controller.  # noqa: E501

        :param observed_generation: The observed_generation of this KnativeStatus.  # noqa: E501
        :type: int
        """

        self._observed_generation = observed_generation

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
        if issubclass(KnativeStatus, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        return (
            self.__dict__ == other.__dict__
            if isinstance(other, KnativeStatus)
            else False
        )

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
