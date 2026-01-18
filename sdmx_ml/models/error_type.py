from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.coded_status_message_type import CodedStatusMessageType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message"


@dataclass(frozen=True, kw_only=True)
class ErrorType:
    """
    ErrorType describes the structure of an error response.

    :ivar error_message: ErrorMessage contains the error message. It can
        occur multiple times to communicate message for multiple errors,
        or to communicate the error message in parallel languages. If
        both messages for multiple errors and parallel language messages
        are used, then each error message should be given a code in
        order to distinguish message for unique errors.
    """

    error_message: tuple[CodedStatusMessageType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ErrorMessage",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
            "min_occurs": 1,
        },
    )
