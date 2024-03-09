from dataclasses import dataclass

from .point_of_interest_entrance_version_structure import (
    PointOfInterestEntranceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOfInterestEntrance(PointOfInterestEntranceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
