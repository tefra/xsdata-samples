from dataclasses import dataclass, field
from .reservation_enumeration import ReservationEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceReservationFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: ReservationEnumeration = field(
        default=ReservationEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
