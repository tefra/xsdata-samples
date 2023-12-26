from __future__ import annotations
from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class PenaltyInformation:
    """
    Parameters
    ----------
    value
    carrier
        Fare-owning carrier
    fare_basis
        Unique identifier that provides the association to the fare amount
        and fare rules.
    fare_component
        A portion of a journey or itinerary between two consecutive fare
        break points.
    priceable_unit
        Identifies FareComponents that are priced together
    board_point
        Origin for the FareComponent
    off_point
        Destination for the FareComponent
    minimum_change_fee
        Estimated minimum change fee associated with the fare component.
        Can be overridden by ChangeFeeApplicationCodes for other fare
        components.
    maximum_change_fee
        Estimated maximum change fee associated with the fare component.
        Can be overridden by ChangeFeeApplicationCodes for other fare
        components.
    filed_currency
        Currency of the filed change fee
    conversion_rate
        Conversion rate from filed change fee currency to reissue location
        currency
    refundable
        Answers whether the FareComponent is refundable
    change_fee_application_code
        Unique code associated with the PenaltyInformation text which
        defines how fees will be applied/calculated. E.g. J2 translates to
        "From among all fare components, changed and unchanged...."
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    carrier: None | str = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "length": 2,
        },
    )
    fare_basis: None | str = field(
        default=None,
        metadata={
            "name": "FareBasis",
            "type": "Attribute",
        },
    )
    fare_component: None | int = field(
        default=None,
        metadata={
            "name": "FareComponent",
            "type": "Attribute",
        },
    )
    priceable_unit: None | int = field(
        default=None,
        metadata={
            "name": "PriceableUnit",
            "type": "Attribute",
        },
    )
    board_point: None | str = field(
        default=None,
        metadata={
            "name": "BoardPoint",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        },
    )
    off_point: None | str = field(
        default=None,
        metadata={
            "name": "OffPoint",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        },
    )
    minimum_change_fee: None | str = field(
        default=None,
        metadata={
            "name": "MinimumChangeFee",
            "type": "Attribute",
        },
    )
    maximum_change_fee: None | str = field(
        default=None,
        metadata={
            "name": "MaximumChangeFee",
            "type": "Attribute",
        },
    )
    filed_currency: None | str = field(
        default=None,
        metadata={
            "name": "FiledCurrency",
            "type": "Attribute",
            "length": 3,
        },
    )
    conversion_rate: None | Decimal = field(
        default=None,
        metadata={
            "name": "ConversionRate",
            "type": "Attribute",
        },
    )
    refundable: None | bool = field(
        default=None,
        metadata={
            "name": "Refundable",
            "type": "Attribute",
        },
    )
    change_fee_application_code: None | str = field(
        default=None,
        metadata={
            "name": "ChangeFeeApplicationCode",
            "type": "Attribute",
            "length": 2,
        },
    )
