from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .sanitary_facility_enumeration import SanitaryFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SanitaryFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Sequence[SanitaryFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
