from dataclasses import dataclass, field
from .retail_facility_enumeration import RetailFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RetailFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: RetailFacilityEnumeration = field(
        default=RetailFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
