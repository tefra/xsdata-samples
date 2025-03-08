from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


class PreferLevelType(Enum):
    """
    Used to specify a preference level for something that is or will be requested
    (e.g. a supplier of a service, a type of service, a form of payment, etc.).
    """

    ONLY = "Only"
    UNACCEPTABLE = "Unacceptable"
    PREFERRED = "Preferred"
