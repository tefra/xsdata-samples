from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .complex_feature_projection import ComplexFeatureProjection
from .complex_feature_projection_ref import ComplexFeatureProjectionRef
from .containment_aggregation_structure import ContainmentAggregationStructure
from .link_projection import LinkProjection
from .link_projection_ref import LinkProjectionRef
from .link_sequence_projection import LinkSequenceProjection
from .link_sequence_projection_ref import LinkSequenceProjectionRef
from .point_projection import PointProjection
from .point_projection_ref import PointProjectionRef
from .topographic_projection import TopographicProjection
from .topographic_projection_ref import TopographicProjectionRef
from .zone_projection import ZoneProjection
from .zone_projection_ref import ZoneProjectionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ProjectionsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "projections_RelStructure"

    projection_ref_or_projection: Iterable[
        Union[
            TopographicProjectionRef,
            ComplexFeatureProjectionRef,
            LinkSequenceProjectionRef,
            ZoneProjectionRef,
            LinkProjectionRef,
            PointProjectionRef,
            TopographicProjection,
            ZoneProjection,
            ComplexFeatureProjection,
            LinkSequenceProjection,
            LinkProjection,
            PointProjection,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TopographicProjectionRef",
                    "type": TopographicProjectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ComplexFeatureProjectionRef",
                    "type": ComplexFeatureProjectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LinkSequenceProjectionRef",
                    "type": LinkSequenceProjectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ZoneProjectionRef",
                    "type": ZoneProjectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LinkProjectionRef",
                    "type": LinkProjectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointProjectionRef",
                    "type": PointProjectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TopographicProjection",
                    "type": TopographicProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ZoneProjection",
                    "type": ZoneProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ComplexFeatureProjection",
                    "type": ComplexFeatureProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LinkSequenceProjection",
                    "type": LinkSequenceProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LinkProjection",
                    "type": LinkProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointProjection",
                    "type": PointProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
