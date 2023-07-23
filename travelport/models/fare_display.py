from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.account_code_1 import AccountCode1
from travelport.models.air_fare_display_rule_key import AirFareDisplayRuleKey
from travelport.models.booking_code import BookingCode
from travelport.models.fare_display_rule import FareDisplayRule
from travelport.models.fare_pricing import FarePricing
from travelport.models.fare_restriction import FareRestriction
from travelport.models.fare_rule_failure_info import FareRuleFailureInfo
from travelport.models.price_change_type import PriceChangeType
from travelport.models.type_atpcoglobal_indicator import TypeAtpcoglobalIndicator
from travelport.models.type_fare_trip_type import TypeFareTripType
from travelport.models.type_mile_or_route_based_fare import TypeMileOrRouteBasedFare

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class FareDisplay:
    """
    Fare/Tariff Display.

    Parameters
    ----------
    fare_display_rule
    fare_pricing
    fare_restriction
    fare_routing_information
    fare_mileage_information
    air_fare_display_rule_key
    booking_code
    account_code
    addl_booking_code_information
    fare_rule_failure_info
        Returns fare rule failure info for Non Valid fares.
    price_change
        Indicates a price change is found in Fare Control Manager
    carrier
    fare_basis
    amount
    trip_type
    fare_type_code
    special_fare
    instant_purchase
    eligibility_restricted
    flight_restricted
    stopovers_restricted
    transfers_restricted
    blackouts_exist
    accompanied_travel
    mile_or_route_based_fare
    global_indicator
    origin
        Returns the origin airport or city code for which this tariff is
        applicable.
    destination
        Returns the destination airport or city code for which this tariff
        is applicable.
    fare_ticketing_code
        Returns the ticketing code for which this tariff is applicable.
    fare_ticketing_designator
        Returns the ticketing designator for which this tariff is
        applicable.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    fare_display_rule: None | FareDisplayRule = field(
        default=None,
        metadata={
            "name": "FareDisplayRule",
            "type": "Element",
            "required": True,
        }
    )
    fare_pricing: list[FarePricing] = field(
        default_factory=list,
        metadata={
            "name": "FarePricing",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    fare_restriction: list[FareRestriction] = field(
        default_factory=list,
        metadata={
            "name": "FareRestriction",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    fare_routing_information: None | str = field(
        default=None,
        metadata={
            "name": "FareRoutingInformation",
            "type": "Element",
        }
    )
    fare_mileage_information: None | str = field(
        default=None,
        metadata={
            "name": "FareMileageInformation",
            "type": "Element",
        }
    )
    air_fare_display_rule_key: None | AirFareDisplayRuleKey = field(
        default=None,
        metadata={
            "name": "AirFareDisplayRuleKey",
            "type": "Element",
        }
    )
    booking_code: list[BookingCode] = field(
        default_factory=list,
        metadata={
            "name": "BookingCode",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    account_code: list[AccountCode1] = field(
        default_factory=list,
        metadata={
            "name": "AccountCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    addl_booking_code_information: None | str = field(
        default=None,
        metadata={
            "name": "AddlBookingCodeInformation",
            "type": "Element",
            "min_length": 1,
            "white_space": "collapse",
        }
    )
    fare_rule_failure_info: None | FareRuleFailureInfo = field(
        default=None,
        metadata={
            "name": "FareRuleFailureInfo",
            "type": "Element",
        }
    )
    price_change: list[PriceChangeType] = field(
        default_factory=list,
        metadata={
            "name": "PriceChange",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    carrier: None | str = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )
    fare_basis: None | str = field(
        default=None,
        metadata={
            "name": "FareBasis",
            "type": "Attribute",
            "required": True,
        }
    )
    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "required": True,
        }
    )
    trip_type: None | TypeFareTripType = field(
        default=None,
        metadata={
            "name": "TripType",
            "type": "Attribute",
        }
    )
    fare_type_code: None | str = field(
        default=None,
        metadata={
            "name": "FareTypeCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        }
    )
    special_fare: None | bool = field(
        default=None,
        metadata={
            "name": "SpecialFare",
            "type": "Attribute",
        }
    )
    instant_purchase: None | bool = field(
        default=None,
        metadata={
            "name": "InstantPurchase",
            "type": "Attribute",
        }
    )
    eligibility_restricted: None | bool = field(
        default=None,
        metadata={
            "name": "EligibilityRestricted",
            "type": "Attribute",
        }
    )
    flight_restricted: None | bool = field(
        default=None,
        metadata={
            "name": "FlightRestricted",
            "type": "Attribute",
        }
    )
    stopovers_restricted: None | bool = field(
        default=None,
        metadata={
            "name": "StopoversRestricted",
            "type": "Attribute",
        }
    )
    transfers_restricted: None | bool = field(
        default=None,
        metadata={
            "name": "TransfersRestricted",
            "type": "Attribute",
        }
    )
    blackouts_exist: None | bool = field(
        default=None,
        metadata={
            "name": "BlackoutsExist",
            "type": "Attribute",
        }
    )
    accompanied_travel: None | bool = field(
        default=None,
        metadata={
            "name": "AccompaniedTravel",
            "type": "Attribute",
        }
    )
    mile_or_route_based_fare: None | TypeMileOrRouteBasedFare = field(
        default=None,
        metadata={
            "name": "MileOrRouteBasedFare",
            "type": "Attribute",
        }
    )
    global_indicator: None | TypeAtpcoglobalIndicator = field(
        default=None,
        metadata={
            "name": "GlobalIndicator",
            "type": "Attribute",
        }
    )
    origin: None | str = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination: None | str = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    fare_ticketing_code: None | str = field(
        default=None,
        metadata={
            "name": "FareTicketingCode",
            "type": "Attribute",
        }
    )
    fare_ticketing_designator: None | str = field(
        default=None,
        metadata={
            "name": "FareTicketingDesignator",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 20,
        }
    )
