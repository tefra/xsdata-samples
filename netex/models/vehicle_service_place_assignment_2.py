from __future__ import annotations

from dataclasses import dataclass

from .assignment_version_structure_1 import AssignmentVersionStructure1

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleServicePlaceAssignment2(AssignmentVersionStructure1):
    class Meta:
        name = "VehicleServicePlaceAssignment_"
        namespace = "http://www.netex.org.uk/netex"
