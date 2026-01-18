from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .point_of_interest_classification_hierarchy import (
    PointOfInterestClassificationHierarchy,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOfInterestClassificationHierarchiesInFrameRelStructure(
    ContainmentAggregationStructure
):
    class Meta:
        name = "pointOfInterestClassificationHierarchiesInFrame_RelStructure"

    point_of_interest_classification_hierarchy: Iterable[
        PointOfInterestClassificationHierarchy
    ] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestClassificationHierarchy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
