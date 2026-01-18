from dataclasses import dataclass, field
from typing import Optional

from sdmx_ml.models.base_header_type import BaseHeaderType
from sdmx_ml.models.footer import Footer

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message"


@dataclass(frozen=True)
class MessageType:
    """
    MessageType is an abstract type which is used by all of the messages,
    to allow inheritance of common features.

    Every message consists of a mandatory header, followed by optional
    payload (which may occur multiple times), and finally an optional
    footer section for conveying error, warning, and informational
    messages.
    """

    header: BaseHeaderType | None = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
            "required": True,
        },
    )
    target_namespace_element: tuple[object, ...] = field(
        default_factory=tuple,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )
    footer: Footer | None = field(
        default=None,
        metadata={
            "name": "Footer",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message/footer",
        },
    )
