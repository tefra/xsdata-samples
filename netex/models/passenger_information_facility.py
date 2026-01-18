from dataclasses import dataclass, field

from .passenger_information_facility_enumeration import (
    PassengerInformationFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassengerInformationFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: PassengerInformationFacilityEnumeration | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
