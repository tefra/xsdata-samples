from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.footer import Footer
from sdmx_ml.models.structure_header_type import StructureHeaderType
from sdmx_ml.models.structures_type import StructuresType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/message"


@dataclass(frozen=True, kw_only=True)
class StructureType:
    """
    StructureType defines the contents of a structure message.

    The payload is optional since this message may be returned from a web
    service with only information in the footer.
    """

    header: StructureHeaderType = field(
        metadata={
            "name": "Header",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/message",
            "required": True,
        }
    )
    structures: None | StructuresType = field(
        default=None,
        metadata={
            "name": "Structures",
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
