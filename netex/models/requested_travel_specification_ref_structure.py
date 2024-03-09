from dataclasses import dataclass

from .travel_specification_ref_structure import TravelSpecificationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RequestedTravelSpecificationRefStructure(
    TravelSpecificationRefStructure
):
    pass
