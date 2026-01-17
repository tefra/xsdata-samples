from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


class ValidatingCarrierPreferLevelType(Enum):
    """
    Used to specify a preference level for ValidatingCarrier.

    For adding new enums see PreferLevelType.
    """

    UNACCEPTABLE = "Unacceptable"
    PREFERRED = "Preferred"
