from dataclasses import dataclass, field
from typing import Optional
from netex.models.complex_feature_members_rel_structure import ComplexFeatureMembersRelStructure
from netex.models.group_of_entities_ref_1 import GroupOfEntitiesRef1
from netex.models.group_of_points_version_structure import GroupOfPointsVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ComplexFeatureVersionStructure(GroupOfPointsVersionStructure):
    class Meta:
        name = "ComplexFeature_VersionStructure"

    group_of_entities_ref: Optional[GroupOfEntitiesRef1] = field(
        default=None,
        metadata={
            "name": "GroupOfEntitiesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    feature_members: Optional[ComplexFeatureMembersRelStructure] = field(
        default=None,
        metadata={
            "name": "featureMembers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
