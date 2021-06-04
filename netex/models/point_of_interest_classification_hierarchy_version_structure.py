from dataclasses import dataclass, field
from typing import Optional
from netex.models.group_of_entities_version_structure import GroupOfEntitiesVersionStructure
from netex.models.point_of_interest_classification_hierarchy_members_rel_structure import PointOfInterestClassificationHierarchyMembersRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOfInterestClassificationHierarchyVersionStructure(GroupOfEntitiesVersionStructure):
    class Meta:
        name = "PointOfInterestClassificationHierarchy_VersionStructure"

    members: Optional[PointOfInterestClassificationHierarchyMembersRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
