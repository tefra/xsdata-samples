from __future__ import annotations

from dataclasses import dataclass

from .vehicle_position_alignment_version_structure import (
    VehiclePositionAlignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehiclePositionAlignment(VehiclePositionAlignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
