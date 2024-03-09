from dataclasses import dataclass, field
from typing import Optional

from .medical_facility_enumeration import MedicalFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MedicalFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Optional[MedicalFacilityEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
