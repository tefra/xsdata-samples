from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.component_list_type import ComponentListType
from sdmx_ml.models.metadata_attribute_type import MetadataAttribute

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class MetadataAttributeListType(ComponentListType):
    """
    MetadataAttributeListType describes the structure of a meta data
    attribute list.

    It comprises a set of metadata attributes that can be defined as a
    hierarchy.

    :ivar choice_1:
    :ivar metadata_attribute:
    :ivar id: The id attribute is provided in this case for
        completeness. However, its value is fixed to
        MetadataAttributeDescriptor.
    """

    choice_1: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    metadata_attribute: tuple[MetadataAttribute, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "MetadataAttribute",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
        },
    )
    id: str = field(
        init=False,
        default="MetadataAttributeDescriptor",
        metadata={
            "type": "Attribute",
            "pattern": r"[A-Za-z0-9_@$\-]+",
        },
    )
