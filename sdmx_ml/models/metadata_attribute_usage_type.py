from dataclasses import dataclass, field
from typing import Optional

from sdmx_ml.models.attribute_relationship_type import (
    AttributeRelationshipType,
)
from sdmx_ml.models.metadata_attribute_usage_base_type import (
    MetadataAttributeUsageBaseType,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class MetadataAttributeUsageType(MetadataAttributeUsageBaseType):
    """
    MetadataAttributeUsageType defines the structure of how a metadata
    attribute is used in a data structure.

    This is a local reference to a metadata attribute from the metadata
    structure referenced by the data structure. An attribute relationship
    can be defined in order to describe the relationship of the metadata
    attribute to the data structure components.

    :ivar metadata_attribute_reference: MetadataAttributeReference is a
        local reference to a metadata attribute defined in the metadata
        structure referenced by this data structure.
    :ivar attribute_relationship: AttributeRelationship defines the
        relationship between the referenced metadata attribute and the
        components of the data structure.
    """

    metadata_attribute_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "MetadataAttributeReference",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9_\-]*",
        },
    )
    attribute_relationship: Optional[AttributeRelationshipType] = field(
        default=None,
        metadata={
            "name": "AttributeRelationship",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
        },
    )
