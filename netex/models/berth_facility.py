from __future__ import annotations

from dataclasses import dataclass, field

from .berth_facility_enumeration import BerthFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BerthFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: BerthFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
