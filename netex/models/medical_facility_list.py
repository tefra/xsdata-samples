from dataclasses import dataclass, field
from typing import List
from .medical_facility_enumeration import MedicalFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MedicalFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[MedicalFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
