from dataclasses import dataclass, field
from typing import List
from .couchette_facility_enumeration import CouchetteFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CouchetteFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[CouchetteFacilityEnumeration] = field(
        default_factory=lambda: [
            CouchetteFacilityEnumeration.UNKNOWN,
        ],
        metadata={
            "tokens": True,
        }
    )
