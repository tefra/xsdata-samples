from __future__ import annotations

from dataclasses import dataclass

from sdmx_ml.models.error_type import ErrorType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message"


@dataclass(frozen=True)
class Error(ErrorType):
    """
    Error is used to communicate that an error has occurred when responding
    to a request in an non-registry environment.

    The content will be a collection of error messages.
    """

    class Meta:
        namespace = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message"
