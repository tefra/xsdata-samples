from collections.abc import Iterable
from dataclasses import dataclass, field

from .complex_feature_member_versioned_child_structure import (
    ComplexFeatureMemberVersionedChildStructure,
)
from .containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ComplexFeatureMembersRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "complexFeatureMembers_RelStructure"

    complex_feature_member: Iterable[
        ComplexFeatureMemberVersionedChildStructure
    ] = field(
        default_factory=list,
        metadata={
            "name": "ComplexFeatureMember",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
