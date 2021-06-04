from dataclasses import dataclass
from netex.models.passenger_carrying_requirement_ref_structure import PassengerCarryingRequirementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassengerCarryingRequirementRef(PassengerCarryingRequirementRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
