# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from .about import __version__

from .bot_adapter import BotAdapter
from .bot_framework_adapter import BotFrameworkAdapter, BotFrameworkAdapterSettings
from .bot_context import BotContext
from .bot_state import BotState
from .conversation_state import ConversationState
from .memory_storage import MemoryStorage
from .middleware_set import AnonymousReceiveMiddleware, Middleware, MiddlewareSet
from .storage import Storage, StoreItem, StorageKeyFactory, calculate_change_hash
from .test_adapter import TestAdapter
from .user_state import UserState

__all__ = ['AnonymousReceiveMiddleware',
           'BotAdapter',
           'BotContext',
           'BotFrameworkAdapter',
           'BotFrameworkAdapterSettings',
           'BotState',
           'calculate_change_hash',
           'ConversationState',
           'MemoryStorage',
           'Middleware',
           'MiddlewareSet',
           'Storage',
           'StorageKeyFactory',
           'StoreItem',
           'TestAdapter',
           'UserState',
           '__version__',]
