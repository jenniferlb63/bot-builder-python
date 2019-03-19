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


class SemanticAction(Model):
    """Represents a reference to a programmatic action.

    :param id: ID of this action
    :type id: str
    :param entities: Entities associated with this action
    :type entities: dict[str, ~botframework.connector.models.Entity]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'entities': {'key': 'entities', 'type': '{Entity}'},
    }

    def __init__(self, *, id: str=None, entities=None, **kwargs) -> None:
        super(SemanticAction, self).__init__(**kwargs)
        self.id = id
        self.entities = entities
