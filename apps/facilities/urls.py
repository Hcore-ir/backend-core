"""
================================================================================
Medical Facility API Routes - H.CORE Project
================================================================================

This module defines the URL routing for the MedicalFacility API endpoints
using Django REST Framework's router system. It connects the MedicalFacilityViewSet
to the appropriate RESTful routes under the `/medical_facility/` prefix.

Author:        H.CORE Backend Team <amiran.amirhossein@gmail.com>
Project:       H.CORE - Hospital Management System (Open Source)
Repository:    https://github.com/Hcore-ir/backend-core

Description:
-------------
This file includes:
    - A DRF SimpleRouter that automatically maps standard CRUD routes
      (list, retrieve, create, update, destroy) to MedicalFacilityViewSet.
    - A URL pattern that namespaces all routes under the path: `/medical_facility/`

Registered endpoints:
    - GET     /medical_facility/           → list all medical facilities
    - POST    /medical_facility/           → create a new facility
    - GET     /medical_facility/{id}/      → retrieve a facility
    - PUT     /medical_facility/{id}/      → update a facility
    - DELETE  /medical_facility/{id}/      → delete a facility

License: GPLv2
"""


from django.urls import path, include
from rest_framework.routers import SimpleRouter

from apps.facilities.views import MedicalFacilityViewSet

medical_facility = SimpleRouter()
medical_facility.register(r"", MedicalFacilityViewSet, basename="medical_facility")

urlpatterns = [
    path("medical_facility/", include(medical_facility.urls)),
]
