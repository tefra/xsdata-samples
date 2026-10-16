from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class BookingProcessEnumeration(StrEnum):
    PRODUCT_NOT_AVAILABLE = "productNotAvailable"
    PRODUCT_NOT_BOOKABLE = "productNotBookable"
    BOOKABLE_THROUGH_INTERNATIONAL_SYSTEM = (
        "bookableThroughInternationalSystem"
    )
    BOOKABLE_THROUGH_NATIONAL_SYSTEM = "bookableThroughNationalSystem"
    BOOKABLE_MANUALLLY = "bookableManuallly"
    OTHER = "other"
