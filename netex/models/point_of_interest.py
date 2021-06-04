from dataclasses import dataclass
from netex.models.point_of_interest_version_structure import PointOfInterestVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOfInterest(PointOfInterestVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
