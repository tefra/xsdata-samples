from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.booking_source_1 import BookingSource1
from travelport.models.driver_info import DriverInfo
from travelport.models.loyalty_card_1 import LoyaltyCard1
from travelport.models.policy import Policy
from travelport.models.rate_modifiers import RateModifiers
from travelport.models.reference_point_1 import ReferencePoint1
from travelport.models.special_equipment_1 import SpecialEquipment1
from travelport.models.type_rate_category import TypeRateCategory
from travelport.models.type_rate_host_indicator import TypeRateHostIndicator
from travelport.models.type_rate_time_period import TypeRateTimePeriod
from travelport.models.type_vehicle_search_distance import (
    TypeVehicleSearchDistance,
)
from travelport.models.vehicle_modifier import VehicleModifier
from travelport.models.vehicle_type import VehicleType
from travelport.models.vendor import Vendor

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class VehicleSearchModifiers:
    """
    Controls and switches for the Vehicle Search request.

    Parameters
    ----------
    permitted_vendors
    prohibited_vendors
    vehicle_modifier
    vehicle_type
    rate_modifiers
    rate_host_indicator
    loyalty_card
    reference_point
        Search Car by reference point
    booking_source
        Supported Providers: 1P. Only type IataNumber is valid.
    special_equipment
        Allows vehicle search with Special equipment by specifying special
        equipment type. e.g. “BikeRack”. Not supported by all vendors. 1P
        only.
    search_distance
        Distance from search location. Supported for standard car search.
        Providers: 1g/1v
    policy
    driver_info
        Use to specify Driver's age. Supported Providers: 1P.
    key
    preferred_currency
        Alternate currency
    unlimited_mileage
        Set to true to search for rates with unlimited mileage.Defaults to
        false.
    rate_category
        The category of this rate (Best, etc)
    rate_guaranteed
        Guarantee indicator for vehicle rate.
    rate_period
        The period for the rate code (daily, weekly, etc)
    sellable_rates_only
        Set to true to search for sellable rates only.  Default is to search
        for all rates.  Providers: 1p
    return_source_currency
        Set to true to return the rate details in Vendor filed currency.
        Defaults to false. Supported Providers: 1G,1V.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    permitted_vendors: None | VehicleSearchModifiers.PermittedVendors = field(
        default=None,
        metadata={
            "name": "PermittedVendors",
            "type": "Element",
        },
    )
    prohibited_vendors: None | VehicleSearchModifiers.ProhibitedVendors = (
        field(
            default=None,
            metadata={
                "name": "ProhibitedVendors",
                "type": "Element",
            },
        )
    )
    vehicle_modifier: list[VehicleModifier] = field(
        default_factory=list,
        metadata={
            "name": "VehicleModifier",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    vehicle_type: list[VehicleType] = field(
        default_factory=list,
        metadata={
            "name": "VehicleType",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    rate_modifiers: list[RateModifiers] = field(
        default_factory=list,
        metadata={
            "name": "RateModifiers",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    rate_host_indicator: None | TypeRateHostIndicator = field(
        default=None,
        metadata={
            "name": "RateHostIndicator",
            "type": "Element",
        },
    )
    loyalty_card: list[LoyaltyCard1] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    reference_point: None | ReferencePoint1 = field(
        default=None,
        metadata={
            "name": "ReferencePoint",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    booking_source: None | BookingSource1 = field(
        default=None,
        metadata={
            "name": "BookingSource",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    special_equipment: list[SpecialEquipment1] = field(
        default_factory=list,
        metadata={
            "name": "SpecialEquipment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 5,
        },
    )
    search_distance: None | TypeVehicleSearchDistance = field(
        default=None,
        metadata={
            "name": "SearchDistance",
            "type": "Element",
        },
    )
    policy: list[Policy] = field(
        default_factory=list,
        metadata={
            "name": "Policy",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    driver_info: None | DriverInfo = field(
        default=None,
        metadata={
            "name": "DriverInfo",
            "type": "Element",
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    preferred_currency: None | str = field(
        default=None,
        metadata={
            "name": "PreferredCurrency",
            "type": "Attribute",
            "length": 3,
        },
    )
    unlimited_mileage: None | bool = field(
        default=None,
        metadata={
            "name": "UnlimitedMileage",
            "type": "Attribute",
        },
    )
    rate_category: None | TypeRateCategory = field(
        default=None,
        metadata={
            "name": "RateCategory",
            "type": "Attribute",
        },
    )
    rate_guaranteed: bool = field(
        default=False,
        metadata={
            "name": "RateGuaranteed",
            "type": "Attribute",
        },
    )
    rate_period: None | TypeRateTimePeriod = field(
        default=None,
        metadata={
            "name": "RatePeriod",
            "type": "Attribute",
        },
    )
    sellable_rates_only: None | bool = field(
        default=None,
        metadata={
            "name": "SellableRatesOnly",
            "type": "Attribute",
        },
    )
    return_source_currency: bool = field(
        default=False,
        metadata={
            "name": "ReturnSourceCurrency",
            "type": "Attribute",
        },
    )

    @dataclass
    class PermittedVendors:
        """
        Parameters
        ----------
        vendor
            1G/1V max 4 vendors, 1P max 99 vendors
        """

        vendor: list[Vendor] = field(
            default_factory=list,
            metadata={
                "name": "Vendor",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            },
        )

    @dataclass
    class ProhibitedVendors:
        vendor: list[Vendor] = field(
            default_factory=list,
            metadata={
                "name": "Vendor",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            },
        )
