from dataclasses import dataclass
from netex.models.vehicle_quay_alignment_ref_structure import VehicleQuayAlignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleQuayAlignmentRef(VehicleQuayAlignmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
