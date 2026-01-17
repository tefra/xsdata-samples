from dataclasses import dataclass, field
from typing import Union

from sdmx_ml.models.attribute_2 import Attribute2
from sdmx_ml.models.attribute_list_base_type import AttributeListBaseType
from sdmx_ml.models.metadata_attribute_usage import MetadataAttributeUsage

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class AttributeListType(AttributeListBaseType):
    """
    AttributeListType describes the attribute descriptor for the data
    structure definition.
    """

    attribute_or_metadata_attribute_usage: tuple[
        Union[Attribute2, MetadataAttributeUsage], ...
    ] = field(
        default_factory=tuple,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Attribute",
                    "type": Attribute2,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "MetadataAttributeUsage",
                    "type": MetadataAttributeUsage,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
            ),
        },
    )
