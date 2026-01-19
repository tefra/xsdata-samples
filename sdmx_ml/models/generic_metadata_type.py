from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.footer import Footer
from sdmx_ml.models.generic_metadata_header_type import (
    GenericMetadataHeaderType,
)
from sdmx_ml.models.metadata_set_type import MetadataSetType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/message"


@dataclass(frozen=True, kw_only=True)
class GenericMetadataType:
    """
    GenericMetadataType defines the contents of a generic metadata message.
    """

    header: GenericMetadataHeaderType = field(
        metadata={
            "name": "Header",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/message",
            "required": True,
        }
    )
    metadata_set: tuple[MetadataSetType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "MetadataSet",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/message",
        },
    )
    footer: None | Footer = field(
        default=None,
        metadata={
            "name": "Footer",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/message/footer",
        },
    )
