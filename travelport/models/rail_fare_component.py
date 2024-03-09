from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.discount_card_1 import DiscountCard1

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass
class RailFareComponent:
    """
    Contains fare and discount information for each passenger type.

    Parameters
    ----------
    discount
        Discount information specific to the fare component
    key
    amount
        FareComponent amount
    age
    passenger_type_code
        The three character passenger code
    supplier_passenger_type
        Supplier passenger type code
    quantity
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    discount: list[RailFareComponent.Discount] = field(
        default_factory=list,
        metadata={
            "name": "Discount",
            "type": "Element",
            "max_occurs": 5,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        },
    )
    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        },
    )
    age: None | int = field(
        default=None,
        metadata={
            "name": "Age",
            "type": "Attribute",
        },
    )
    passenger_type_code: None | str = field(
        default=None,
        metadata={
            "name": "PassengerTypeCode",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 5,
        },
    )
    supplier_passenger_type: None | str = field(
        default=None,
        metadata={
            "name": "SupplierPassengerType",
            "type": "Attribute",
        },
    )
    quantity: None | int = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Attribute",
        },
    )

    @dataclass
    class Discount:
        discount_card: list[DiscountCard1] = field(
            default_factory=list,
            metadata={
                "name": "DiscountCard",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
                "min_occurs": 1,
                "max_occurs": 9,
            },
        )
        key: None | str = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
            },
        )
