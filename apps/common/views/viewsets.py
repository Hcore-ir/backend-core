"""
============================================================
Common Base ViewSets and Utilities - H.CORE Project
============================================================

This module is part of the H.CORE backend system.

Author:        H.CORE Backend Team <amiran.amirhossein@gmail.com>
Project:       H.CORE - Hospital Management System (Open Source)
Repository:    https://github.com/Hcore-ir/backend-core

Description:
-------------
This file provides shared base ViewSet classes for Django REST Framework.

These include:
    - BaseParsedViewSet: Adds multipart/form-data parsing, pagination, filtering, and search
    - BaseCRUDViewSet: Full Create/Read/Update/Delete functionality
    - ReadOnlyListRetrieveViewSet: Read-only ViewSet with list and detail support
    - CreateOnlyViewSet: Allows only object creation (POST)
    - RetrieveOnlyViewSet: Allows only detail view by ID (GET)

These components are designed to be reused across apps to ensure consistency,
reduce boilerplate, and support scalable API development.

License: GPLv2
"""

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets, mixins

# Local pagination
from apps.common.pagination import StandardResultsSetPagination


class BaseParsedViewSet(viewsets.GenericViewSet):
    """
    Abstract base ViewSet with common API features.

    Features:
    - Parses multipart/form-data (e.g., file uploads)
    - Supports pagination using `StandardResultsSetPagination`
    - Enables filtering, searching, and ordering via query parameters

    Typical usage:
    - Extend this class with appropriate mixins (e.g., ListModelMixin)
    - Used as the base for all other custom ViewSets in the system
    """

    parser_classes = [MultiPartParser, FormParser]
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]


class BaseCRUDViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,  # Optional: add list support too
    BaseParsedViewSet,
):
    """
    Base ViewSet with full CRUD support.

    Inherits:
    - BaseParsedViewSet (pagination, filtering, parsing)
    - DRF mixins for standard CRUD methods

    Endpoints:
    - POST   /api/resource/        -> create object
    - GET    /api/resource/        -> list all
    - GET    /api/resource/{id}/   -> retrieve object
    - PUT    /api/resource/{id}/   -> update object
    - DELETE /api/resource/{id}/   -> delete object
    """

    pass


class CreateOnlyViewSet(mixins.CreateModelMixin, BaseParsedViewSet):
    """
    ViewSet that allows only object creation (POST).

    No read, update, or delete operations.

    Use Cases:
    - Public submission forms (feedback, registration)
    - Anonymous data ingestion endpoints
    """

    pass


class RetrieveOnlyViewSet(mixins.RetrieveModelMixin, BaseParsedViewSet):
    """
    ViewSet that allows retrieving a single object by ID.

    No listing, creation, update, or deletion.

    Use Cases:
    - Read-only detail views
    - Secure access to a specific object
    """

    pass


class ReadOnlyListRetrieveViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    BaseParsedViewSet,
):
    """
    ViewSet that supports listing and retrieving objects (read-only).

    Endpoints:
    - GET /api/resource/        -> list all (with pagination/filtering)
    - GET /api/resource/{id}/   -> retrieve a single resource

    No write (POST/PUT/DELETE) actions allowed.

    Use Cases:
    - Public APIs
    - Dropdowns, reference tables, readonly data
    """

    pass
