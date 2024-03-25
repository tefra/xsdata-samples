from dataclasses import dataclass, field
from typing import Tuple, Union

from sdmx_ml.models.attribute_list import AttributeList
from sdmx_ml.models.dimension_list import DimensionList
from sdmx_ml.models.group import Group
from sdmx_ml.models.measure_list import MeasureList
from sdmx_ml.models.metadata_attribute_list import MetadataAttributeList

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class GroupingType:
    """GroupType is an abstract base type for specific structure groupings.

    It contains a collection of component lists. Concrete instances of
    this should restrict to specific concrete component lists.
    """

    choice: Tuple[
        Union[
            MetadataAttributeList,
            MeasureList,
            Group,
            DimensionList,
            AttributeList,
        ],
        ...,
    ] = field(
        default_factory=tuple,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "MetadataAttributeList",
                    "type": MetadataAttributeList,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "MeasureList",
                    "type": MeasureList,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "Group",
                    "type": Group,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "DimensionList",
                    "type": DimensionList,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "AttributeList",
                    "type": AttributeList,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
            ),
        },
    )
