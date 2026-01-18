from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PublicUseEnumeration(Enum):
    ALL = "all"
    DISABLED_PUBLIC_ONLY = "disabledPublicOnly"
    AUTHORISED_PUBLIC_ONLY = "authorisedPublicOnly"
    STAFF_ONLY = "staffOnly"
    PUBLIC_ONLY = "publicOnly"
