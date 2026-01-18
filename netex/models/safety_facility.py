from __future__ import annotations

from dataclasses import dataclass, field

from .safety_facility_enumeration import SafetyFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SafetyFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: None | SafetyFacilityEnumeration = field(
        default=None,
        metadata={
            "required": True,
        },
    )
