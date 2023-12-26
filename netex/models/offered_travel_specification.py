from dataclasses import dataclass
from .offered_travel_specification_version_structure import (
    OfferedTravelSpecificationVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OfferedTravelSpecification(OfferedTravelSpecificationVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
