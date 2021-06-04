from dataclasses import dataclass
from netex.models.travel_specification_version_structure import TravelSpecificationVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TravelSpecification2(TravelSpecificationVersionStructure):
    class Meta:
        name = "TravelSpecification"
        namespace = "http://www.netex.org.uk/netex"
