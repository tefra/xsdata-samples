from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.models.complex_feature_ref import ComplexFeatureRef
from netex.models.multilingual_string import MultilingualString
from netex.models.simple_feature_ref import SimpleFeatureRef
from netex.models.spatial_feature_ref import SpatialFeatureRef
from netex.models.type_of_projection_ref_structure import TypeOfProjectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ProjectionVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "Projection_VersionStructure"

    type_of_projection_ref: Optional[TypeOfProjectionRefStructure] = field(
        default=None,
        metadata={
            "name": "TypeOfProjectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    complex_feature_ref: List[ComplexFeatureRef] = field(
        default_factory=list,
        metadata={
            "name": "ComplexFeatureRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    simple_feature_ref: List[SimpleFeatureRef] = field(
        default_factory=list,
        metadata={
            "name": "SimpleFeatureRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    spatial_feature_ref: Optional[SpatialFeatureRef] = field(
        default=None,
        metadata={
            "name": "SpatialFeatureRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
