from __future__ import annotations

from dataclasses import dataclass

from .vehicle_quay_alignment_version_structure import (
    VehicleQuayAlignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleQuayAlignment(VehicleQuayAlignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
