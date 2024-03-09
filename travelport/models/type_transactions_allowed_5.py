from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_booking_transactions_allowed_5 import (
    TypeBookingTransactionsAllowed5,
)

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class TypeTransactionsAllowed5(TypeBookingTransactionsAllowed5):
    """
    Parameters
    ----------
    shopping_enabled
        Allow or prohibit shopping transaction for the given product type on
        this Provider/Supplier. Inheritable.
    pricing_enabled
        Allow or prohibit pricing transaction for the given product type on
        this Provider/Supplier. Inheritable.
    """

    class Meta:
        name = "typeTransactionsAllowed"

    shopping_enabled: None | bool = field(
        default=None,
        metadata={
            "name": "ShoppingEnabled",
            "type": "Attribute",
        },
    )
    pricing_enabled: None | bool = field(
        default=None,
        metadata={
            "name": "PricingEnabled",
            "type": "Attribute",
        },
    )
