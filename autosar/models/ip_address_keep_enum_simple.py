from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class IpAddressKeepEnumSimple(Enum):
    """
    :cvar FORGET: After a dynamic IP address has been assigned just use
        it for this session.
    :cvar STORE_PERSISTENTLY: After a dynamic IP address has been
        assigned store the address persistently.
    """

    FORGET = "FORGET"
    STORE_PERSISTENTLY = "STORE-PERSISTENTLY"
