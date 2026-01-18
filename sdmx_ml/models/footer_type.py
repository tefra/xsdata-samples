from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.footer_message_type import FooterMessageType

__NAMESPACE__ = (
    "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message/footer"
)


@dataclass(frozen=True)
class FooterType:
    """
    FooterType describes the structure of a message footer.

    The footer is used to convey any error, information, or warning
    messages. This is to be used when the message has payload, but also
    needs to communicate additional information. If an error occurs and no
    payload is generated, an Error message should be returned.

    :ivar message: Message contains a single error, information, or
        warning message. A code is provided along with an optional
        severity. The text of the message can be expressed in multiple
        languages.
    """

    message: tuple[FooterMessageType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Message",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message/footer",
            "min_occurs": 1,
        },
    )
