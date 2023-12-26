from dataclasses import dataclass
from .requested_travel_specification_ref_structure import (
    RequestedTravelSpecificationRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RequestedTravelSpecificationRef(
    RequestedTravelSpecificationRefStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
