"""
================================================================================
Medical Facility Models - H.CORE Project
================================================================================

This module defines the core data models related to medical facilities used in
the H.CORE backend system. These models represent different aspects of a
healthcare facility including its type, subtype (specialty), ownership model,
and main profile information.

Author:        H.CORE Backend Team <amiran.amirhossein@gmail.com>
Project:       H.CORE - Hospital Management System (Open Source)
Repository:    https://github.com/Hcore-ir/backend-core

Description:
-------------
This file includes the following models:
    - MedicalFacilityType:      High-level classification of the facility (e.g., Hospital, Clinic)
    - MedicalFacilitySubType:   Specific function or specialty (e.g., Psychiatric Hospital)
    - MedicalFacilityOwnershipType: Ownership/governance type (e.g., Public, Private)
    - MedicalFacility:          Represents a detailed instance of a facility with contact info,
                                history, mission, and legal documentation.

These models are designed to be reused across the platform to ensure a normalized,
scalable structure for managing healthcare centers and hospitals.

License: GPLv2
"""

from django.db import models
from tinymce.models import HTMLField


class MedicalFacilityType(models.Model):
    """
    Main category for medical facilities.

    Example:
        slug = "hospital"
        title = "Hospital"
    """

    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=255, verbose_name="Facility Type Title")

    def __str__(self):
        return self.title


class MedicalFacilitySubType(models.Model):
    """
    Describes the specialty or function of the facility.

    Example:
        - General Hospital
        - Psychiatric Hospital
        - Specialized Clinic
    """

    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=255, verbose_name="Facility Subtype Title")

    class Meta:
        verbose_name = "Facility Subtype (Specialty)"
        verbose_name_plural = "Facility Subtypes (Specialties)"

    def __str__(self):
        return self.title


class MedicalFacilityOwnershipType(models.Model):
    """
    Indicates the governance or funding model of the facility.

    Examples:
        - Public
        - Private
        - Charity-based
        - Government-owned
    """

    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=255, verbose_name="Ownership Type")

    class Meta:
        verbose_name = "Ownership Type"
        verbose_name_plural = "Ownership Types"

    def __str__(self):
        return self.title


class MedicalFacility(models.Model):
    """
    Represents an individual medical facility.
    """
    slug = models.SlugField()
    name = models.CharField(max_length=255, verbose_name="Facility Name")

    type = models.ForeignKey(
        MedicalFacilityType,
        on_delete=models.CASCADE,
        related_name="facilities",
        verbose_name="Facility Type",
    )

    subtype = models.ForeignKey(
        MedicalFacilitySubType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="facilities",
        verbose_name="Facility Subtype",
    )

    ownership = models.ForeignKey(
        MedicalFacilityOwnershipType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="facilities",
        verbose_name="Ownership Type",
    )

    history = HTMLField(
        blank=True,
        verbose_name="Facility History",
        help_text="Provide a historical background of the facility.",
    )

    presentation = HTMLField(
        blank=True,
        verbose_name="Mission and Vision",
        help_text="Describe the mission, values, or goals of the facility.",
    )

    legal_charters = HTMLField(
        blank=True,
        verbose_name="Legal Charters / Declarations",
        help_text="Include any official charters, patient rights, or legal documents.",
    )

    # Contact & Location
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    logo = models.ImageField(
        upload_to="facilities/logos/",
        blank=True,
        null=True,
        verbose_name="Facility Logo",
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Medical Facility"
        verbose_name_plural = "Medical Facilities"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
