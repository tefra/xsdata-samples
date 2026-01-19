from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .assistance_facility_enumeration import AssistanceFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AssistanceFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Sequence[AssistanceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
