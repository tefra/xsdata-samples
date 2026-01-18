from __future__ import annotations

from dataclasses import dataclass

from .passenger_stop_assignment_version_structure import (
    PassengerStopAssignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassengerStopAssignment(PassengerStopAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
