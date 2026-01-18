from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.attribute_2 import Attribute2
from sdmx_ml.models.dimension import Dimension
from sdmx_ml.models.group_dimension import GroupDimension
from sdmx_ml.models.identifiable_type import IdentifiableType
from sdmx_ml.models.measure import Measure
from sdmx_ml.models.metadata_attribute_type import MetadataAttribute
from sdmx_ml.models.metadata_attribute_usage import MetadataAttributeUsage
from sdmx_ml.models.time_dimension import TimeDimension

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True, kw_only=True)
class ComponentListType(IdentifiableType):
    """
    ComponentListType is an abstract base type for all component lists.

    It contains a collection of components. Concrete types should restrict
    this to specific concrete components.
    """

    choice: tuple[
        MetadataAttribute
        | Measure
        | GroupDimension
        | TimeDimension
        | Dimension
        | MetadataAttributeUsage
        | Attribute2,
        ...,
    ] = field(
        default_factory=tuple,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "MetadataAttribute",
                    "type": MetadataAttribute,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "Measure",
                    "type": Measure,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "GroupDimension",
                    "type": GroupDimension,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "TimeDimension",
                    "type": TimeDimension,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "Dimension",
                    "type": Dimension,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "MetadataAttributeUsage",
                    "type": MetadataAttributeUsage,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "Attribute",
                    "type": Attribute2,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
            ),
        },
    )
