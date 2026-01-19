from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .medical_facility_enumeration import MedicalFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MedicalFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Sequence[MedicalFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
