from __future__ import annotations

from dataclasses import dataclass, field

from .display_assignment_version_structure import (
    DisplayAssignmentVersionStructure,
)
from .status_enumeration import StatusEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DisplayAssignment(DisplayAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    name_of_class: str | None = field(
        default=None,
        metadata={
            "name": "nameOfClass",
            "type": "Attribute",
        },
    )
    data_source_ref: str | None = field(
        default=None,
        metadata={
            "name": "dataSourceRef",
            "type": "Attribute",
        },
    )
    status: StatusEnumeration = field(
        default=StatusEnumeration.ACTIVE,
        metadata={
            "type": "Attribute",
        },
    )
    derived_from_version_ref: str | None = field(
        default=None,
        metadata={
            "name": "derivedFromVersionRef",
            "type": "Attribute",
        },
    )
