from dataclasses import dataclass, field
from typing import List
from netex.models.complex_feature_projection import ComplexFeatureProjection
from netex.models.complex_feature_projection_ref import ComplexFeatureProjectionRef
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.link_projection import LinkProjection
from netex.models.link_projection_ref import LinkProjectionRef
from netex.models.link_sequence_projection import LinkSequenceProjection
from netex.models.link_sequence_projection_ref import LinkSequenceProjectionRef
from netex.models.point_projection import PointProjection
from netex.models.point_projection_ref import PointProjectionRef
from netex.models.projection import Projection
from netex.models.projection_ref import ProjectionRef
from netex.models.topographic_projection import TopographicProjection
from netex.models.topographic_projection_ref import TopographicProjectionRef
from netex.models.zone_projection import ZoneProjection
from netex.models.zone_projection_ref import ZoneProjectionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ProjectionsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "projections_RelStructure"

    topographic_projection_ref: List[TopographicProjectionRef] = field(
        default_factory=list,
        metadata={
            "name": "TopographicProjectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    complex_feature_projection_ref: List[ComplexFeatureProjectionRef] = field(
        default_factory=list,
        metadata={
            "name": "ComplexFeatureProjectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    link_sequence_projection_ref: List[LinkSequenceProjectionRef] = field(
        default_factory=list,
        metadata={
            "name": "LinkSequenceProjectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    zone_projection_ref: List[ZoneProjectionRef] = field(
        default_factory=list,
        metadata={
            "name": "ZoneProjectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    link_projection_ref: List[LinkProjectionRef] = field(
        default_factory=list,
        metadata={
            "name": "LinkProjectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_projection_ref: List[PointProjectionRef] = field(
        default_factory=list,
        metadata={
            "name": "PointProjectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    projection_ref: List[ProjectionRef] = field(
        default_factory=list,
        metadata={
            "name": "ProjectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    topographic_projection: List[TopographicProjection] = field(
        default_factory=list,
        metadata={
            "name": "TopographicProjection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    zone_projection: List[ZoneProjection] = field(
        default_factory=list,
        metadata={
            "name": "ZoneProjection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    complex_feature_projection: List[ComplexFeatureProjection] = field(
        default_factory=list,
        metadata={
            "name": "ComplexFeatureProjection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    link_sequence_projection: List[LinkSequenceProjection] = field(
        default_factory=list,
        metadata={
            "name": "LinkSequenceProjection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    link_projection: List[LinkProjection] = field(
        default_factory=list,
        metadata={
            "name": "LinkProjection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_projection: List[PointProjection] = field(
        default_factory=list,
        metadata={
            "name": "PointProjection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    projection: List[Projection] = field(
        default_factory=list,
        metadata={
            "name": "Projection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
