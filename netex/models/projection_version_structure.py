from dataclasses import dataclass, field
from typing import Optional, Union

from .complex_feature_ref import ComplexFeatureRef
from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString
from .simple_feature_ref import SimpleFeatureRef
from .spatial_feature_ref import SpatialFeatureRef
from .type_of_projection_ref_structure import TypeOfProjectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ProjectionVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "Projection_VersionStructure"

    type_of_projection_ref: TypeOfProjectionRefStructure | None = field(
        default=None,
        metadata={
            "name": "TypeOfProjectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    spatial_feature_ref: ComplexFeatureRef | SimpleFeatureRef | SpatialFeatureRef | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ComplexFeatureRef",
                    "type": ComplexFeatureRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SimpleFeatureRef",
                    "type": SimpleFeatureRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SpatialFeatureRef",
                    "type": SpatialFeatureRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    order: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
