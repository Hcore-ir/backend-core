from django.contrib import admin
from apps.facilities.models import (
    MedicalFacility,
    MedicalFacilityType,
    MedicalFacilitySubType,
    MedicalFacilityOwnershipType,
)
# Register your models here.

admin.site.register(MedicalFacility)
admin.site.register(MedicalFacilityType)
admin.site.register(MedicalFacilitySubType)
admin.site.register(MedicalFacilityOwnershipType)
