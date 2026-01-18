from __future__ import annotations

from dataclasses import dataclass, field

from .group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)
from .point_of_interest_classification_hierarchy_members_rel_structure import (
    PointOfInterestClassificationHierarchyMembersRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOfInterestClassificationHierarchyVersionStructure(
    GroupOfEntitiesVersionStructure
):
    class Meta:
        name = "PointOfInterestClassificationHierarchy_VersionStructure"

    members: (
        None | PointOfInterestClassificationHierarchyMembersRelStructure
    ) = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
