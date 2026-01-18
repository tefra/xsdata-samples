from __future__ import annotations

from dataclasses import dataclass, field

from .assistance_facility_enumeration import AssistanceFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AssistanceFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: None | AssistanceFacilityEnumeration = field(
        default=None,
        metadata={
            "required": True,
        },
    )
