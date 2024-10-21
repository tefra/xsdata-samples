from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .point_of_interest_space import PointOfInterestSpace
from .site_component_ref_structure import SiteComponentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOfInterestSpacesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "pointOfInterestSpaces_RelStructure"

    point_of_interest_space_ref_or_point_of_interest_space: Iterable[
        Union[SiteComponentRefStructure, PointOfInterestSpace]
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
