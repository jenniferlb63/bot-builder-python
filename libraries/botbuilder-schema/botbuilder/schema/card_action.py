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


class CardAction(Model):
    """A clickable action.

    :param type: The type of action implemented by this button. Possible
     values include: 'openUrl', 'imBack', 'postBack', 'playAudio', 'playVideo',
     'showImage', 'downloadFile', 'signin', 'call', 'payment', 'messageBack'
    :type type: str or ~botframework.connector.models.ActionTypes
    :param title: Text description which appears on the button
    :type title: str
    :param image: Image URL which will appear on the button, next to text
     label
    :type image: str
    :param text: Text for this action
    :type text: str
    :param display_text: (Optional) text to display in the chat feed if the
     button is clicked
    :type display_text: str
    :param value: Supplementary parameter for action. Content of this property
     depends on the ActionType
    :type value: object
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'image': {'key': 'image', 'type': 'str'},
        'text': {'key': 'text', 'type': 'str'},
        'display_text': {'key': 'displayText', 'type': 'str'},
        'value': {'key': 'value', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(CardAction, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.title = kwargs.get('title', None)
        self.image = kwargs.get('image', None)
        self.text = kwargs.get('text', None)
        self.display_text = kwargs.get('display_text', None)
        self.value = kwargs.get('value', None)
