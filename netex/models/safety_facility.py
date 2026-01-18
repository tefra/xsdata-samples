from __future__ import annotations

from dataclasses import dataclass, field

from .safety_facility_enumeration import SafetyFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SafetyFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: SafetyFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
