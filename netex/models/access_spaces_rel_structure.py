from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .access_space import AccessSpace
from .access_space_ref import AccessSpaceRef
from .containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessSpacesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "accessSpaces_RelStructure"

    access_space_ref_or_access_space: Iterable[
        AccessSpaceRef | AccessSpace
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AccessSpaceRef",
                    "type": AccessSpaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessSpace",
                    "type": AccessSpace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
