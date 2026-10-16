from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DestinationDisplayContextEnumeration(StrEnum):
    ANY = "any"
    CONTINUE_TO = "continueTo"
    ENDS_AT = "endsAt"
    TRANSFER_AT = "transferAt"
    VIA = "via"
    IN_MESSAGE = "inMessage"
    UNKNOWN = "unknown"
