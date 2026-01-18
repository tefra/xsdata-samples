from __future__ import annotations

from dataclasses import dataclass

from .stop_assignment_ref_structure import StopAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleTypeStopAssignmentRefStructure(StopAssignmentRefStructure):
    pass
