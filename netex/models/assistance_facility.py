from __future__ import annotations

from dataclasses import dataclass, field

from .assistance_facility_enumeration import AssistanceFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AssistanceFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: AssistanceFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
