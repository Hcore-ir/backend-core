"""
============================================================
Common Utilities for H.CORE Project
============================================================

This module is part of the H.CORE backend system.

Author:        H.CORE Backend Team <amiran.amirhossein@gmail.com>
Project:       H.CORE - Hospital Management System (Open Source)
Repository:    https://github.com/Hcore-ir/backend-core

Description:
-------------
This file provides shared base classes and utilities for Django REST Framework,
including base Pagination. These components are designed to be reusable
across multiple apps to maintain consistency and reduce code duplication.

License: GPLv2
"""

from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    """
    Standard pagination class to provide paginated responses for list views.

    Default behavior:
    - 10 items per page
    - Clients can override using `?page_size=<int>`
    - Maximum allowed `page_size` is 100

    This class is intended to be reused across all paginated views.
    """

    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100
