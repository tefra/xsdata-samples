from dataclasses import dataclass, field
from typing import Optional

from sdmx_ml.models.metadata_attribute_list import MetadataAttributeList
from sdmx_ml.models.metadata_structure_components_base_type import (
    MetadataStructureComponentsBaseType,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class MetadataStructureComponentsType(MetadataStructureComponentsBaseType):
    """
    MetadataStructureComponentsType describes the structure of the grouping
    of the sets of the components that make up the metadata structure
    definition.
    """

    metadata_attribute_list: Optional[MetadataAttributeList] = field(
        default=None,
        metadata={
            "name": "MetadataAttributeList",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
        },
    )
