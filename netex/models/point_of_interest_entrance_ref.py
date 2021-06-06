from dataclasses import dataclass
from .point_of_interest_entrance_ref_structure import PointOfInterestEntranceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOfInterestEntranceRef(PointOfInterestEntranceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
