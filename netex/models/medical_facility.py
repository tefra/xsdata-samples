from __future__ import annotations

from dataclasses import dataclass, field

from .medical_facility_enumeration import MedicalFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MedicalFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: MedicalFacilityEnumeration | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
