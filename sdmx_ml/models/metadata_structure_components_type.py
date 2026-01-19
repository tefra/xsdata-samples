from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.metadata_attribute_list import MetadataAttributeList
from sdmx_ml.models.metadata_structure_components_base_type import (
    MetadataStructureComponentsBaseType,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class MetadataStructureComponentsType(MetadataStructureComponentsBaseType):
    """
    MetadataStructureComponentsType describes the structure of the grouping
    of the sets of the components that make up the metadata structure
    definition.
    """

    metadata_attribute_list: MetadataAttributeList = field(
        metadata={
            "name": "MetadataAttributeList",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
            "required": True,
        }
    )
