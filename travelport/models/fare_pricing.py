from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class FarePricing:
    """
    Container for Fare Pricing Information.

    One per PTC type.

    Parameters
    ----------
    passenger_type
    total_fare_amount
    private_fare
        NegotiatedFare attribute from earlier version of schema used to
        imply whether the fare is private fare or not. So, this attribute is
        renamed to PrivateFare as it best suited.
    negotiated_fare
        Identifies the fare as a Negotiated Fare.
    auto_priceable
        Identifies the fare as Autopriceable or not. False value means the
        fare filing is incomplete and the fare should not be used.
    total_net_fare_amount
        Total Net fare amount.
    base_fare
        Base fare amount.
    taxes
    mmid
        Contains the Reference id which is generated when the request was
        ReturnMM=”true”.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    passenger_type: None | str = field(
        default=None,
        metadata={
            "name": "PassengerType",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 5,
        },
    )
    total_fare_amount: None | str = field(
        default=None,
        metadata={
            "name": "TotalFareAmount",
            "type": "Attribute",
        },
    )
    private_fare: None | bool = field(
        default=None,
        metadata={
            "name": "PrivateFare",
            "type": "Attribute",
        },
    )
    negotiated_fare: None | bool = field(
        default=None,
        metadata={
            "name": "NegotiatedFare",
            "type": "Attribute",
        },
    )
    auto_priceable: None | bool = field(
        default=None,
        metadata={
            "name": "AutoPriceable",
            "type": "Attribute",
        },
    )
    total_net_fare_amount: None | str = field(
        default=None,
        metadata={
            "name": "TotalNetFareAmount",
            "type": "Attribute",
        },
    )
    base_fare: None | str = field(
        default=None,
        metadata={
            "name": "BaseFare",
            "type": "Attribute",
        },
    )
    taxes: None | str = field(
        default=None,
        metadata={
            "name": "Taxes",
            "type": "Attribute",
        },
    )
    mmid: None | str = field(
        default=None,
        metadata={
            "name": "MMid",
            "type": "Attribute",
        },
    )
