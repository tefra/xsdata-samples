from dataclasses import dataclass
from netex.models.passenger_capacity_ref_structure import PassengerCapacityRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassengerCapacityRef(PassengerCapacityRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
