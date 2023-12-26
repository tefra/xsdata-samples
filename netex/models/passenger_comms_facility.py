from dataclasses import dataclass, field
from .passenger_comms_facility_enumeration import (
    PassengerCommsFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassengerCommsFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: PassengerCommsFacilityEnumeration = field(
        default=PassengerCommsFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
