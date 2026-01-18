from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .group_of_timebands_ref import GroupOfTimebandsRef
from .group_of_timebands_versioned_child_structure import (
    GroupOfTimebandsVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfTimebandsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "groupOfTimebands_RelStructure"

    group_of_timebands_ref_or_group_of_timebands: Iterable[
        GroupOfTimebandsRef | GroupOfTimebandsVersionedChildStructure
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GroupOfTimebandsRef",
                    "type": GroupOfTimebandsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfTimebands",
                    "type": GroupOfTimebandsVersionedChildStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
