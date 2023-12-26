from dataclasses import dataclass
from .travel_specification_version_structure import (
    TravelSpecificationVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OfferedTravelSpecificationVersionStructure(
    TravelSpecificationVersionStructure
):
    class Meta:
        name = "OfferedTravelSpecification_VersionStructure"
