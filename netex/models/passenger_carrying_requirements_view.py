from dataclasses import dataclass
from netex.models.passenger_carrying_requirement_version_structure import PassengerCarryingRequirementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassengerCarryingRequirementsView(PassengerCarryingRequirementVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
