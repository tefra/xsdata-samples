from dataclasses import dataclass, field
from typing import List
from netex.models.complex_feature import ComplexFeature
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.simple_feature import SimpleFeature

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SpatialFeaturesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "spatialFeaturesInFrame_RelStructure"

    simple_feature: List[SimpleFeature] = field(
        default_factory=list,
        metadata={
            "name": "SimpleFeature",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    complex_feature: List[ComplexFeature] = field(
        default_factory=list,
        metadata={
            "name": "ComplexFeature",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
