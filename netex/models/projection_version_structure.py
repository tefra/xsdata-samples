from dataclasses import dataclass, field
from typing import Optional
from .alternative_texts_rel_structure import DataManagedObjectStructure
from .complex_feature_ref import ComplexFeatureRef
from .multilingual_string import MultilingualString
from .simple_feature_ref import SimpleFeatureRef
from .spatial_feature_ref import SpatialFeatureRef
from .type_of_projection_ref_structure import TypeOfProjectionRefStructure

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
    complex_feature_ref: Optional[ComplexFeatureRef] = field(
        default=None,
        metadata={
            "name": "ComplexFeatureRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    simple_feature_ref: Optional[SimpleFeatureRef] = field(
        default=None,
        metadata={
            "name": "SimpleFeatureRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
