# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PaymentMethodData(Model):
    """Indicates a set of supported payment methods and any associated payment
    method specific data for those methods.

    :param supported_methods: Required sequence of strings containing payment
     method identifiers for payment methods that the merchant web site accepts
    :type supported_methods: list[str]
    :param data: A JSON-serializable object that provides optional information
     that might be needed by the supported payment methods
    :type data: object
    """

    _attribute_map = {
        'supported_methods': {'key': 'supportedMethods', 'type': '[str]'},
        'data': {'key': 'data', 'type': 'object'},
    }

    def __init__(self, supported_methods=None, data=None):
        super(PaymentMethodData, self).__init__()
        self.supported_methods = supported_methods
        self.data = data
