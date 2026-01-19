from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .point_of_interest_space import PointOfInterestSpace
from .site_component_ref_structure import SiteComponentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOfInterestSpacesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "pointOfInterestSpaces_RelStructure"

    point_of_interest_space_ref_or_point_of_interest_space: Sequence[
        SiteComponentRefStructure | PointOfInterestSpace
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PointOfInterestSpaceRef",
                    "type": SiteComponentRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestSpace",
                    "type": PointOfInterestSpace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
