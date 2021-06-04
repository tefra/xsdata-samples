from dataclasses import dataclass
from netex.models.vehicle_position_alignment_version_structure import VehiclePositionAlignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehiclePositionAlignment(VehiclePositionAlignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
