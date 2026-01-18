from __future__ import annotations

from dataclasses import dataclass

from .vehicle_position_alignment_ref_structure import (
    VehiclePositionAlignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehiclePositionAlignmentRef(VehiclePositionAlignmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
