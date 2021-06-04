from dataclasses import dataclass
from netex.models.road_address_version_structure import RoadAddressVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RoadAddress(RoadAddressVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
