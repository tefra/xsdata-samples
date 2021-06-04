from dataclasses import dataclass, field
from netex.models.mobility_facility_enumeration import MobilityFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MobilityFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: MobilityFacilityEnumeration = field(
        default=MobilityFacilityEnumeration.UNKNOWN,
    )
