from dataclasses import dataclass, field
from .accommodation_facility_enumeration import AccommodationFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccommodationFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: AccommodationFacilityEnumeration = field(
        default=AccommodationFacilityEnumeration.SEATING
    )
