from dataclasses import dataclass, field
from typing import Optional

from .complex_feature_members_rel_structure import (
    ComplexFeatureMembersRelStructure,
)
from .group_of_points_version_structure import GroupOfPointsVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ComplexFeatureVersionStructure(GroupOfPointsVersionStructure):
    class Meta:
        name = "ComplexFeature_VersionStructure"

    feature_members: Optional[ComplexFeatureMembersRelStructure] = field(
        default=None,
        metadata={
            "name": "featureMembers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
