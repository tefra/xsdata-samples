from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.metadata_structure_type_abstract import (
    MetadataStructureTypeAbstract,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


@dataclass(frozen=True)
class GenericMetadataStructureType(MetadataStructureTypeAbstract):
    """
    GenericMetadataStructureType defines the structural information for a generic
    metadata message.
    """

    namespace: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
