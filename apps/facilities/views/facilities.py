"""
================================================================================
Medical Facility ViewSets - H.CORE Project
================================================================================

This module defines the ViewSet for the MedicalFacility model in the H.CORE
backend system. ViewSets provide a high-level abstraction over Django REST
Framework's views to handle common CRUD operations (Create, Read, Update, Delete)
via API endpoints.

Author:        H.CORE Backend Team <amiran.amirhossein@gmail.com>
Project:       H.CORE - Hospital Management System (Open Source)
Repository:    https://github.com/Hcore-ir/backend-core

Description:
-------------
This file includes:
    - MedicalFacilityViewSet: A reusable and extendable ViewSet for managing
      MedicalFacility instances, including support for:
        • Queryset filtering
        • Searchable fields (name, type, city, etc.)
        • Default ordering
        • Serializer integration

It leverages:
    - BaseCRUDViewSet: A custom base class that encapsulates standard
      DRF functionality with project-specific extensions
    - MedicalFacilitySerializer: Serializer responsible for JSON representation
      and data validation of MedicalFacility objects

License: GPLv2
"""

from apps.common.views import BaseCRUDViewSet
from apps.facilities.models import (
    MedicalFacility,
    MedicalFacilityType,
    MedicalFacilitySubType,
    MedicalFacilityOwnershipType,
)
from apps.facilities.serializers import MedicalFacilitySerializer


class MedicalFacilityViewSet(BaseCRUDViewSet):
    queryset = MedicalFacility.objects.all()
    serializer_class = MedicalFacilitySerializer

    ordering = ["slug", "name", "city", "province"]
    search_fields = [
        "name",
        "city",
        "province",
        "type__title",
        "subtype__title",
        "ownership__title",
    ]
