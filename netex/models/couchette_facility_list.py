from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .couchette_facility_enumeration import CouchetteFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CouchetteFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Sequence[CouchetteFacilityEnumeration] = field(
        default_factory=lambda: [
            CouchetteFacilityEnumeration.UNKNOWN,
        ],
        metadata={
            "tokens": True,
        },
    )
