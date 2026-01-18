from dataclasses import dataclass, field
from typing import Optional

from sdmx_ml.models.status_message_type_1 import StatusMessageType1
from sdmx_ml.models.status_type import StatusType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry"


@dataclass(frozen=True)
class StatusMessageType2:
    """
    StatusMessageType carries the text of error messages and/or warnings in
    response to queries or requests.

    :ivar message_text: MessageText contains the text of the error
        and/or warning message. It can occur multiple times to
        communicate message for multiple warnings or errors.
    :ivar status: The status attribute carries the status of the query
        or request.
    """

    class Meta:
        name = "StatusMessageType"

    message_text: tuple[StatusMessageType1, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "MessageText",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
        },
    )
    status: StatusType | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
