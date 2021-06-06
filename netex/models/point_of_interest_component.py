from dataclasses import dataclass
from .point_of_interest_component_version_structure import PointOfInterestComponentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOfInterestComponent(PointOfInterestComponentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
