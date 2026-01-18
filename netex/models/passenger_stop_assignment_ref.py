from __future__ import annotations

from dataclasses import dataclass

from .passenger_stop_assignment_ref_structure import (
    PassengerStopAssignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassengerStopAssignmentRef(PassengerStopAssignmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
