from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class BookingAccessEnumeration(Enum):
    PUBLIC = "public"
    AUTHORISED_PUBLIC = "authorisedPublic"
    STAFF = "staff"
    OTHER = "other"
