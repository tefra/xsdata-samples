from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.booking_traveler_ref_1 import BookingTravelerRef1
from travelport.models.rail_booking_info import RailBookingInfo
from travelport.models.rail_fare import RailFare
from travelport.models.rail_fare_ref import RailFareRef
from travelport.models.type_element_status_1 import TypeElementStatus1
from travelport.models.type_passenger_type_1 import TypePassengerType1

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass
class RailPricingInfo:
    """
    Per traveler type pricing breakdown.

    Parameters
    ----------
    rail_fare
    rail_fare_ref
    rail_booking_info
    passenger_type
    booking_traveler_ref
    key
    exchange_amount
        The amount to pay to cover the exchange of the fare (includes
        penalties).
    approximate_exchange_amount
    total_price
        The total price for this entity including base price and all taxes.
    base_price
        Represents the base price for this entity. This does not include any
        taxes or surcharges.
    approximate_total_price
        The Converted total price in Default Currency for this entity
        including base price and all taxes.
    approximate_base_price
        The Converted base price in Default Currency for this entity. This
        does not include any taxes or surcharges.
    equivalent_base_price
        Represents the base price in the related currency for this entity.
        This does not include any taxes or surcharges.
    taxes
        The aggregated amount of all the taxes that are associated with this
        entity. See the associated TaxInfo array for a breakdown of the
        individual taxes.
    fees
        The aggregated amount of all the fees that are associated with this
        entity. See the associated FeeInfo array for a breakdown of the
        individual fees.
    services
        The total cost for all optional services.
    approximate_taxes
        The Converted tax amount in Default Currency.
    approximate_fees
        The Converted fee amount in Default Currency.
    el_stat
        This attribute is used to show the action results of an element.
        Possible values are "A" (when elements have been added to the UR)
        and "M" (when existing elements have been modified). Response only.
    key_override
        If a duplicate key is found where we are adding elements in some
        cases like URAdd, then instead of erroring out set this attribute to
        true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    rail_fare: list[RailFare] = field(
        default_factory=list,
        metadata={
            "name": "RailFare",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    rail_fare_ref: list[RailFareRef] = field(
        default_factory=list,
        metadata={
            "name": "RailFareRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    rail_booking_info: list[RailBookingInfo] = field(
        default_factory=list,
        metadata={
            "name": "RailBookingInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    passenger_type: list[TypePassengerType1] = field(
        default_factory=list,
        metadata={
            "name": "PassengerType",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    booking_traveler_ref: list[BookingTravelerRef1] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    exchange_amount: None | str = field(
        default=None,
        metadata={
            "name": "ExchangeAmount",
            "type": "Attribute",
        }
    )
    approximate_exchange_amount: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateExchangeAmount",
            "type": "Attribute",
        }
    )
    total_price: None | str = field(
        default=None,
        metadata={
            "name": "TotalPrice",
            "type": "Attribute",
        }
    )
    base_price: None | str = field(
        default=None,
        metadata={
            "name": "BasePrice",
            "type": "Attribute",
        }
    )
    approximate_total_price: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateTotalPrice",
            "type": "Attribute",
        }
    )
    approximate_base_price: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateBasePrice",
            "type": "Attribute",
        }
    )
    equivalent_base_price: None | str = field(
        default=None,
        metadata={
            "name": "EquivalentBasePrice",
            "type": "Attribute",
        }
    )
    taxes: None | str = field(
        default=None,
        metadata={
            "name": "Taxes",
            "type": "Attribute",
        }
    )
    fees: None | str = field(
        default=None,
        metadata={
            "name": "Fees",
            "type": "Attribute",
        }
    )
    services: None | str = field(
        default=None,
        metadata={
            "name": "Services",
            "type": "Attribute",
        }
    )
    approximate_taxes: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateTaxes",
            "type": "Attribute",
        }
    )
    approximate_fees: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateFees",
            "type": "Attribute",
        }
    )
    el_stat: None | TypeElementStatus1 = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: None | bool = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )
