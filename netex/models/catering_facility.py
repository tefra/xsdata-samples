from dataclasses import dataclass, field
from netex.models.catering_facility_enumeration import CateringFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CateringFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: CateringFacilityEnumeration = field(
        default=CateringFacilityEnumeration.UNKNOWN,
    )
