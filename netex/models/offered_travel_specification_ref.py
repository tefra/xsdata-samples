from dataclasses import dataclass
from netex.models.offered_travel_specification_ref_structure import OfferedTravelSpecificationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OfferedTravelSpecificationRef(OfferedTravelSpecificationRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
