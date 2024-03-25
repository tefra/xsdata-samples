from dataclasses import dataclass, field
from typing import Optional, Tuple

from sdmx_ml.models.text_type import TextType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


@dataclass(frozen=True)
class StatusMessageType1:
    """StatusMessageType describes the structure of an error or warning message.

    A message contains the text of the message, as well as an optional
    language indicator and an optional code.

    :ivar text: Text contains the text of the message, in parallel
        language values.
    :ivar code: The code attribute holds an optional code identifying
        the underlying error that generated the message. This should be
        used if parallel language descriptions of the error are
        supplied, to distinguish which of the multiple error messages
        are for the same underlying error.
    """

    class Meta:
        name = "StatusMessageType"

    text: Tuple[TextType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common",
            "min_occurs": 1,
        },
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
