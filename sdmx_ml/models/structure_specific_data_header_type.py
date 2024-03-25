from dataclasses import dataclass, field
from typing import Any, Tuple

from sdmx_ml.models.base_header_type import BaseHeaderType
from sdmx_ml.models.structure_specific_data_structure_type import (
    StructureSpecificDataStructureType,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message"


@dataclass(frozen=True)
class StructureSpecificDataHeaderType(BaseHeaderType):
    """
    StructureSpecificDataHeaderType defines the header structure for a structure
    specific data message.

    :ivar metadata_provider: MetadataProvider identifies the provider of
        the metadata for a metadata message.
    :ivar structure:
    """

    metadata_provider: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    structure: Tuple[StructureSpecificDataStructureType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Structure",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
            "min_occurs": 1,
        },
    )
