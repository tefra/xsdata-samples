from __future__ import annotations

from dataclasses import dataclass, field

from .complex_feature_members_rel_structure import (
    ComplexFeatureMembersRelStructure,
)
from .group_of_points_version_structure import GroupOfPointsVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ComplexFeatureVersionStructure(GroupOfPointsVersionStructure):
    class Meta:
        name = "ComplexFeature_VersionStructure"

    feature_members: None | ComplexFeatureMembersRelStructure = field(
        default=None,
        metadata={
            "name": "featureMembers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
