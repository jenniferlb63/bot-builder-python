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


class MessageReaction(Model):
    """Message reaction object.

    :param type: Message reaction type. Possible values include: 'like',
     'plusOne'
    :type type: str or ~bot.connector.models.MessageReactionTypes
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, type=None):
        super(MessageReaction, self).__init__()
        self.type = type
