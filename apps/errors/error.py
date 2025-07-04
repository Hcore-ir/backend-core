"""
================================================================================
Error Management Utilities - H.CORE Project
================================================================================

This module provides a multilingual error management system for the H.CORE
backend. It is designed to standardize how error messages are defined, stored,
and retrieved across the project, with support for multiple languages and
custom error categories.

--------------------------------------------------------------------------------
Author:      H.CORE Backend Team <amiran.amirhossein@gmail.com>
Project:     H.CORE - Hospital Management System (Open Source)
Repository:  https://github.com/Hcore-ir/backend-core
License:     GPLv2
--------------------------------------------------------------------------------

Key Components:
---------------
- ErrorHolder:
    Centralized registry for error messages.
    Stores error dictionaries by event and language.
    Provides access and extension capabilities.

- init():
    Initializes the global `errors_holder` instance and registers default
    error messages for supported modules and languages (currently: COURSE,
    INSTRUCTOR in English and Farsi).

- getText(event, error, *args, lang="fa"):
    Retrieves the localized error message corresponding to the given `event`
    and `error` code. Supports optional formatting with `args`. Falls back to
    raising a `ValidationError` if the message is not found.

Usage Example:
--------------
    error_message = getText("COURSE", "INVALID_TITLE", "Python 101", lang="en")
    # → "Invalid title: Python 101"

Extending Errors:
-----------------
You can extend or override error dictionaries at runtime using:
    errors_holder.extendsError(event, lang, error_dict)

This enables dynamic customization of messages (e.g., from plugins).

"""

import os
from collections import defaultdict

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# import local Modules
from apps.errors import errors_en
from apps.errors import errors_fa

def init():
    global errors_holder
    errors_holder = ErrorHolder()

    # register English Errors
    # register Farsi Errors

class ErrorHolder:
    def __init__(self):
        self.__error_maps = defaultdict(dict)
    def registerError(
        self,
        event: str,
        lang: str,
        error_dict: dict,
    ):
        self.__error_maps[event][lang] = error_dict

    def get(
        self,
        event: str,
        lang: str,
        error: str
    ):
        return self.__error_maps[event][lang][error]

    def extendsError(
        self,
        event: str,
        lang: str,
        error_dict: str
    ):
        if event not in self.__error_maps:
            self.__error_maps[event][lang] = {}

        return self.__error_maps[event][lang].update(error_dict)

def getText(
    event : str,
    error: str,
    *args,
    lang:str = os.getenv("LANG_ERROR", "fa"),
):
    try:
        global errors_holder
        error_str = errors_holder.get(event, lang, error)

        if args:
            error_str = error_str % args
        return error_str

    except Exception:
        raise ValidationError(
            _("%(event)s this Error Event Not Found."),
            params={"event": event},
        )
