from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .passenger_stop_assignment_derived_view_structure import (
    PassengerStopAssignmentDerivedViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassengerStopAssignmentView(PassengerStopAssignmentDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    label: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    branding_ref: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
