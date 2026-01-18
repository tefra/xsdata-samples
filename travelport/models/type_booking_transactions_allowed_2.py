from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass(kw_only=True)
class TypeBookingTransactionsAllowed2:
    """
    Parameters
    ----------
    booking_enabled
        Allow or prohibit booking transaction for the given product type on
        this Provider/Supplier. Inheritable.
    """

    class Meta:
        name = "typeBookingTransactionsAllowed"

    booking_enabled: None | bool = field(
        default=None,
        metadata={
            "name": "BookingEnabled",
            "type": "Attribute",
        },
    )
