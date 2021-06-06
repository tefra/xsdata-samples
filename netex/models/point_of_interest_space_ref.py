from dataclasses import dataclass
from .point_of_interest_space_ref_structure import PointOfInterestSpaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOfInterestSpaceRef(PointOfInterestSpaceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
