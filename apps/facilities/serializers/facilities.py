"""
================================================================================
Medical Facility Serializers - H.CORE Project
================================================================================

This module defines the serializers for medical facility-related models used in
the H.CORE backend system. Serializers are responsible for converting model
instances to and from JSON representations for use in the API layer.

Author:        H.CORE Backend Team <amiran.amirhossein@gmail.com>
Project:       H.CORE - Hospital Management System (Open Source)
Repository:    https://github.com/Hcore-ir/backend-core

Description:
-------------
This file includes:
    - MedicalFacilitySerializer: Serializer for the MedicalFacility model, handling
      full facility profile, classification, contact information, and metadata.

It leverages the custom BaseModelSerializer which provides:
    - Automatic slug generation (if `slug_fields` is defined in Meta)
    - Consistent handling of read-only fields (`created_at`, `updated_at`, `slug`)
    - Proper ManyToMany field handling in create/update

These serializers are used in views and APIs to enforce a consistent structure
and simplify data handling for medical facility resources.

License: GPLv2
"""

from apps.common.serializers import BaseModelSerializer
from apps.facilities.models import (
    MedicalFacility,
    MedicalFacilityType,
    MedicalFacilitySubType,
    MedicalFacilityOwnershipType,
)


class MedicalFacilitySerializer(BaseModelSerializer):
    """
    Serializer for the MedicalFacility model.
    Includes full profile, classification, contact, and metadata fields.
    """

    class Meta:
        model = MedicalFacility
        read_only_fields = ["created_at", "updated_at", "slug"]
        slug_fields = ["name", "city"]
        fields = [
            "name",
            "type",
            "subtype",
            "ownership",
            "history",
            "presentation",
            "legal_charters",
            "city",
            "province",
            "postal_code",
            "phone_number",
            "email",
            "website",
            "logo",
            "is_active",
            "created_at",
            "updated_at",
        ]
