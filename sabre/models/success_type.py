from __future__ import annotations

from dataclasses import dataclass

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class SuccessType:
    """
    Standard way to indicate successful processing of an OTA message.

    Returning an empty element of this type indicates success.
    """
