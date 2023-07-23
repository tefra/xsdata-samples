from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class DepositAmount:
    """
    Amount required for deposit/prepayment.

    Parameters
    ----------
    amount
        Supplier deposit amount required for deposit/prepayment.Supported by
        all Providers when supported by supplier
    approximate_amount
        Approximate deposit amount required for deposit/prepayment.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        }
    )
    approximate_amount: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateAmount",
            "type": "Attribute",
        }
    )
