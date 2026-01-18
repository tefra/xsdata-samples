from __future__ import annotations

from dataclasses import dataclass, field

from .assignment_ref_structure import AssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DisplayAssignmentRefStructure(AssignmentRefStructure):
    order: int = field(
        default=1,
        metadata={
            "type": "Attribute",
        },
    )
