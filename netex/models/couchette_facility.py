from dataclasses import dataclass, field

from .couchette_facility_enumeration import CouchetteFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CouchetteFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: CouchetteFacilityEnumeration = field(
        default=CouchetteFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
