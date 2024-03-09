from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class CorporateDiscountId6:
    """
    These are zero or more negotiated rate codes.

    Parameters
    ----------
    value
    negotiated_rate_code
        When set to true, the data in the CorporateDiscountID is a
        negotiated rate code. Otherwise, this data is a Corporate Discount
        ID rate.
    """

    class Meta:
        name = "CorporateDiscountID"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    negotiated_rate_code: None | bool = field(
        default=None,
        metadata={
            "name": "NegotiatedRateCode",
            "type": "Attribute",
        },
    )
