from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ServicedOrganisationTypeEnumeration(StrEnum):
    SCHOOL = "school"
    COLLEGE = "college"
    UNIVERSITY = "university"
    MILITARY_BASE = "militaryBase"
    WORKS = "works"
    RETAIIL_CENTRE = "retaiilCentre"
    HOSPITAL = "hospital"
    GOVERNMENT_OFFICE = "governmentOffice"
    OTHER = "other"
