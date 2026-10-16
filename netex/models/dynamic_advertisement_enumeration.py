from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DynamicAdvertisementEnumeration(StrEnum):
    ALWAYS = "always"
    NEVER = "never"
    ONLY_IF_ORDERED = "onlyIfOrdered"
    ONLY_IF_SIGNED_ON = "onlyIfSignedOn"
