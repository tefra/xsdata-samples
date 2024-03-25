from dataclasses import dataclass, field
from typing import Optional, Tuple

from sdmx_ml.models.footer import Footer
from sdmx_ml.models.generic_metadata_header_type import (
    GenericMetadataHeaderType,
)
from sdmx_ml.models.metadata_set_type import MetadataSetType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message"


@dataclass(frozen=True)
class GenericMetadataType:
    """
    GenericMetadataType defines the contents of a generic metadata message.
    """

    header: Optional[GenericMetadataHeaderType] = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
            "required": True,
        },
    )
    metadata_set: Tuple[MetadataSetType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "MetadataSet",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
        },
    )
    footer: Optional[Footer] = field(
        default=None,
        metadata={
            "name": "Footer",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message/footer",
        },
    )
