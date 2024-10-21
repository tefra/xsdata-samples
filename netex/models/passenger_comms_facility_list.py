from collections.abc import Iterable
from dataclasses import dataclass, field

from .passenger_comms_facility_enumeration import (
    PassengerCommsFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassengerCommsFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Iterable[PassengerCommsFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
