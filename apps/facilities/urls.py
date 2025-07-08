"""
================================================================================
Medical Facility API Routes - H.CORE Project
================================================================================

This module defines the URL routing for the MedicalFacility API endpoints
using Django REST Framework's router system. It connects the MedicalFacilityViewSet
to the appropriate RESTful routes under the `/facility/` prefix.

Author:        H.CORE Backend Team <amiran.amirhossein@gmail.com>
Project:       H.CORE - Hospital Management System (Open Source)
Repository:    https://github.com/Hcore-ir/backend-core

Description:
-------------
This file includes:
    - A DRF SimpleRouter that automatically maps standard CRUD routes
      (list, retrieve, create, update, destroy) to MedicalFacilityViewSet.
    - A URL pattern that namespaces all routes under the path: `/facility/`
        and `/facality`

Registered endpoints:
    - GET     /facility/           → list all medical facilities
    - POST    /facility/           → create a new facility
    - GET     /facility/{id}/      → retrieve a facility
    - PUT     /facility/{id}/      → update a facility
    - DELETE  /facility/{id}/      → delete a facility
    ---
    - GET     /facility-meta/type                → list all facilities/type
    - GET     /facility-meta/sub_type            → list all facilities/sub_type
    - GET     /facility-meta/ownership           → list all facilities/ownership

License: GPLv2
"""

from django.urls import path, include
from rest_framework.routers import SimpleRouter

from apps.facilities.views import (
    MedicalFacilityViewSet,
    MedicalFacilityTypeViewSet,
    MedicalFacilitySubTypeViewSet,
    MedicalFacilityOwnershipTypeViewSet,
)

facility = SimpleRouter()
facility.register(r"", MedicalFacilityViewSet, basename="facility")

facility_meta = SimpleRouter()
facility_meta.register(r"type", MedicalFacilityTypeViewSet, basename="facility-type")
facility_meta.register(
    r"sub_type", MedicalFacilitySubTypeViewSet, basename="facility-subtype"
)
facility_meta.register(
    r"ownership", MedicalFacilityOwnershipTypeViewSet, basename="facility-ownership"
)

urlpatterns = [
    path("facility/", include(facility.urls)),
    path("facility-meta/", include(facility_meta.urls)),
]
