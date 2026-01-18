from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .medical_facility_enumeration import MedicalFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MedicalFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Iterable[MedicalFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
