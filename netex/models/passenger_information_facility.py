from dataclasses import dataclass, field
from typing import Optional
from .passenger_information_facility_enumeration import (
    PassengerInformationFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassengerInformationFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Optional[PassengerInformationFacilityEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
