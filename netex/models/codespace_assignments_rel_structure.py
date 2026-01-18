from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .codespace_assignment_versioned_child_structure import (
    CodespaceAssignmentVersionedChildStructure,
)
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CodespaceAssignmentsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "codespaceAssignments_RelStructure"

    codespace_assignment: Iterable[
        CodespaceAssignmentVersionedChildStructure
    ] = field(
        default_factory=list,
        metadata={
            "name": "CodespaceAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
