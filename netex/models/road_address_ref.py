from dataclasses import dataclass
from netex.models.road_address_ref_structure import RoadAddressRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RoadAddressRef(RoadAddressRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
