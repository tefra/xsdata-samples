from dataclasses import dataclass
from .individual_traveller_ref_structure import IndividualTravellerRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class IndividualTravellerRef(IndividualTravellerRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
