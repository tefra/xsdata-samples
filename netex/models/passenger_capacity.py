from dataclasses import dataclass
from .passenger_capacity_structure import PassengerCapacityStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassengerCapacity(PassengerCapacityStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
