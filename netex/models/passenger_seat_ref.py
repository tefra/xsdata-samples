from dataclasses import dataclass
from netex.models.passenger_seat_ref_structure import PassengerSeatRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassengerSeatRef(PassengerSeatRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
