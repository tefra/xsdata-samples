from dataclasses import dataclass, field

from sdmx_ml.models.coded_status_message_type import CodedStatusMessageType
from sdmx_ml.models.severity_code_type import SeverityCodeType

__NAMESPACE__ = (
    "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message/footer"
)


@dataclass(frozen=True)
class FooterMessageType(CodedStatusMessageType):
    """
    FooterMessageType defines the structure of a message that is contained
    in the footer of a message.

    It is a status message that have a severity code of Error, Information,
    or Warning added to it.
    """

    severity: SeverityCodeType | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
