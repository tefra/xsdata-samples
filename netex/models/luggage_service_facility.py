from dataclasses import dataclass, field
from typing import Optional
from .luggage_service_facility_enumeration import LuggageServiceFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LuggageServiceFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Optional[LuggageServiceFacilityEnumeration] = field(
        default=None
    )
