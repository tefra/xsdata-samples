from __future__ import annotations

from dataclasses import dataclass, field

from .mobility_facility_enumeration import MobilityFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MobilityFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: MobilityFacilityEnumeration = field(
        default=MobilityFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
