from __future__ import annotations

from dataclasses import dataclass, field

from .entity_in_version_structure import VersionedChildStructure
from .point_of_interest_classification_ref_structure import (
    PointOfInterestClassificationRefStructure,
)
from .point_of_interest_hierarchy_ref import PointOfInterestHierarchyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOfInterestClassificationHierarchyMemberStructure(
    VersionedChildStructure
):
    point_of_interest_hierarchy_ref: None | PointOfInterestHierarchyRef = (
        field(
            default=None,
            metadata={
                "name": "PointOfInterestHierarchyRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    parent_classification_ref: (
        None | PointOfInterestClassificationRefStructure
    ) = field(
        default=None,
        metadata={
            "name": "ParentClassificationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    point_of_interest_classification_ref: (
        None | PointOfInterestClassificationRefStructure
    ) = field(
        default=None,
        metadata={
            "name": "PointOfInterestClassificationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
