from __future__ import annotations

from dataclasses import dataclass

from .train_stop_assignment_ref_structure import (
    TrainStopAssignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainStopAssignmentRef(TrainStopAssignmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
