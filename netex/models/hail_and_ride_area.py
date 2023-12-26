from dataclasses import dataclass
from .hail_and_ride_area_version_structure import (
    HailAndRideAreaVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class HailAndRideArea(HailAndRideAreaVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
