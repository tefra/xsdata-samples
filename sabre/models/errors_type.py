from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.error_type import ErrorType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class ErrorsType:
    """
    A collection of errors that occurred during the processing of a
    message.

    Attributes:
        error: Describes an error that occurred during the processing of
            an OTA message
    """

    error: list[ErrorType] = field(
        default_factory=list,
        metadata={
            "name": "Error",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_occurs": 1,
        },
    )
