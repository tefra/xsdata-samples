from dataclasses import dataclass, field
from typing import Optional

from sdmx_ml.models.status_message_type_1 import StatusMessageType1

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


@dataclass(frozen=True)
class CodedStatusMessageType(StatusMessageType1):
    """
    CodedStatusMessageType describes the structure of an error or warning
    message which required a code.
    """

    code: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
