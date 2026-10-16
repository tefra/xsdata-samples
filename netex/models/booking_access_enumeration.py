from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class BookingAccessEnumeration(StrEnum):
    PUBLIC = "public"
    AUTHORISED_PUBLIC = "authorisedPublic"
    STAFF = "staff"
    OTHER = "other"
