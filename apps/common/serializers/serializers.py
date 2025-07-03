"""
================================================================================
Base Serializers for H.CORE Project
================================================================================

This module is part of the H.CORE backend system.

Author:        H.CORE Backend Team <amiran.amirhossein@gmail.com>
Project:       H.CORE - Hospital Management System (Open Source)
Repository:    https://github.com/Hcore-ir/backend-core

Description:
-------------
This module provides reusable base classes for Django REST Framework serializers.

Key Features:
    - Automatic slug generation based on configurable fields (`slug_fields` in Meta)
    - Proper handling of ManyToMany relationships during both create and update
    - Standard inclusion of common fields such as `slug`, `created_at`, and `updated_at`

These components are intended to be subclassed by app-specific serializers in
order to promote DRY principles, enforce consistency, and simplify CRUD logic
across the system.

License: GPLv2
"""

from rest_framework import serializers
from django.utils.text import slugify


class BaseModelSerializer(serializers.ModelSerializer):
    """
    Base serializer with:
      - Automatic slug generation (if `slug_fields` is provided in Meta)
      - Correct handling of ManyToMany fields during create and update
    """

    slug = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def _pop_m2m_fields(self, validated_data):
        """
        Extract ManyToMany fields from validated_data.
        Returns (cleaned_data, m2m_data)
        """
        m2m_fields = {}
        model_class = self.Meta.model
        for field in model_class._meta.many_to_many:
            if field.name in validated_data:
                m2m_fields[field.name] = validated_data.pop(field.name)
        return validated_data, m2m_fields

    def _generate_slug(self, instance, validated_data):
        """
        If `slug_fields` is defined in Meta, generate a slug from them.
        """
        slug_fields = getattr(self.Meta, "slug_fields", None)
        if slug_fields and hasattr(instance, "slug") and not getattr(instance, "slug"):
            slug_value = "-".join(
                str(validated_data.get(field, "")) for field in slug_fields
            )
            instance.slug = slugify(slug_value, allow_unicode=True)

    def create(self, validated_data):
        validated_data, m2m_data = self._pop_m2m_fields(validated_data)
        instance = self.Meta.model(**validated_data)
        self._generate_slug(instance, validated_data)
        instance.save()

        for field_name, values in m2m_data.items():
            getattr(instance, field_name).set(values)

        return instance

    def update(self, instance, validated_data):
        validated_data, m2m_data = self._pop_m2m_fields(validated_data)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        self._generate_slug(instance, validated_data)
        instance.save()

        for field_name, values in m2m_data.items():
            getattr(instance, field_name).set(values)

        return instance
