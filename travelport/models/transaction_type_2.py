from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_tier_2 import AirTier2
from travelport.models.type_booking_transactions_allowed_2 import (
    TypeBookingTransactionsAllowed2,
)
from travelport.models.type_transactions_allowed_2 import (
    TypeTransactionsAllowed2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class TransactionType2:
    """Configuration for products by type.

    Inheritable.

    Parameters
    ----------
    air
    hotel
    rail
    vehicle
    passive
        For true passive segments such as ground, cruise etc
    background_passive
        For behind the scenes or background passives Only
    """

    class Meta:
        name = "TransactionType"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    air: None | TransactionType2.Air = field(
        default=None,
        metadata={
            "name": "Air",
            "type": "Element",
        },
    )
    hotel: None | TypeTransactionsAllowed2 = field(
        default=None,
        metadata={
            "name": "Hotel",
            "type": "Element",
        },
    )
    rail: None | TypeTransactionsAllowed2 = field(
        default=None,
        metadata={
            "name": "Rail",
            "type": "Element",
        },
    )
    vehicle: None | TypeTransactionsAllowed2 = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
        },
    )
    passive: None | TypeBookingTransactionsAllowed2 = field(
        default=None,
        metadata={
            "name": "Passive",
            "type": "Element",
        },
    )
    background_passive: None | TypeBookingTransactionsAllowed2 = field(
        default=None,
        metadata={
            "name": "BackgroundPassive",
            "type": "Element",
        },
    )

    @dataclass
    class Air(TypeTransactionsAllowed2):
        """
        Parameters
        ----------
        tier
            Indicate the Tier Level
        days_enabled
            Allow or prohibit Flexible Days (within a date range) shopping
            option
        weekends_enabled
            Allow or prohibit Flexible Weekends shopping option
        airports_enabled
            Allow or prohibit Flexible Airport (choice of Origin and
            Destination airports) shopping option
        odenabled
            Allow or prohibit Flexible Origin and Destination (choice of
            airports within a radius) shopping option
        one_way_shop
            Allows or prohibits one way shopping functionality for the
            associated provisioning provider configuration
        flex_explore
            Allows or prohibits flex explore functionality for the
            associated provisioning provider configuration
        rapid_reprice_enabled
            Allows or prohibits rapid reprice functionality for the
            associated provisioning provider configuration. Providers: 1G/1V
        """

        tier: None | AirTier2 = field(
            default=None,
            metadata={
                "name": "Tier",
                "type": "Attribute",
            },
        )
        days_enabled: None | bool = field(
            default=None,
            metadata={
                "name": "DaysEnabled",
                "type": "Attribute",
            },
        )
        weekends_enabled: None | bool = field(
            default=None,
            metadata={
                "name": "WeekendsEnabled",
                "type": "Attribute",
            },
        )
        airports_enabled: None | bool = field(
            default=None,
            metadata={
                "name": "AirportsEnabled",
                "type": "Attribute",
            },
        )
        odenabled: None | bool = field(
            default=None,
            metadata={
                "name": "ODEnabled",
                "type": "Attribute",
            },
        )
        one_way_shop: None | bool = field(
            default=None,
            metadata={
                "name": "OneWayShop",
                "type": "Attribute",
            },
        )
        flex_explore: None | bool = field(
            default=None,
            metadata={
                "name": "FlexExplore",
                "type": "Attribute",
            },
        )
        rapid_reprice_enabled: None | bool = field(
            default=None,
            metadata={
                "name": "RapidRepriceEnabled",
                "type": "Attribute",
            },
        )
