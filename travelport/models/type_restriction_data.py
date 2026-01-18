from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class TypeRestrictionData:
    """
    Restriction data.

    Parameters
    ----------
    amount
        Implies a flat amount to be adjusted. Negative value implies a
        discount.
    percentage
        Implies an adjustment to be made on original price. Negative value
        implies a discount.
    name
        Possible value for restriction name "Non-Refundable","Non-
        Changeable","Cancellation","Changes", "Non-Refundable marked with No
        Show","No Show","Non-Changeable marked with No Show"
    value
        Possible value for restriction value "After Departure","Anytime" and
        "Before Departure"
    """

    class Meta:
        name = "typeRestrictionData"

    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        },
    )
    percentage: None | str = field(
        default=None,
        metadata={
            "name": "Percentage",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "pattern": r"([0-9]{1,2}|100)\.[0-9]{1,2}",
        },
    )
    name: None | object = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        },
    )
    value: None | object = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
        },
    )
