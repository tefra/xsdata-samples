from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.host_token_1 import HostToken1
from travelport.models.journey_remark import JourneyRemark
from travelport.models.rail_segment import RailSegment
from travelport.models.rail_segment_ref import RailSegmentRef
from travelport.models.type_element_status_1 import TypeElementStatus1
from travelport.models.type_journey_direction import TypeJourneyDirection

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass
class RailJourney:
    """
    Captures all journey-related data.

    Parameters
    ----------
    rail_segment
    rail_segment_ref
    journey_remark
    host_token
    key
    origin
        The IATA location code for this origination of this entity.
    destination
        The IATA location code for this destination of this entity.
    departure_time
        The date and time at which this entity departs. This does not
        include time zone information since it can be derived from the
        origin location.
    arrival_time
        The date and time at which this entity arrives at the destination.
        This does not include time zone information since it can be derived
        from the origin location.
    origin_station_name
        The origin station name for the Journey.
    destination_station_name
        The destination station name for the Journey.
    rail_loc_origin
        RCH specific origin code (a.k.a UCodes) which uniquely identifies a
        train station.
    rail_loc_destination
        RCH specific destination code (a.k.a UCodes) which uniquely
        identifies a train station.
    route_description
        The description of the route.
    journey_direction
        The direction of the Journey (Outward or Return).
    journey_duration
        The duration of the entire Journey in minutes
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
    provider_code
    supplier_code
    status
        Status of this Journey.
    provider_reservation_info_ref
        Provider reservation reference key.
    passive_provider_reservation_info_ref
        Passive provider reservation reference key.
    travel_order
        To identify the appropriate travel sequence for Air/Car/Hotel/Rail
        segments/reservations/Journeys based on travel dates. This ordering
        is applicable across the UR not provider or traveler specific
    route_reference
        RouteReference is required in seat assignment purpose
    el_stat
        This attribute is used to show the action results of an element.
        Possible values are "A" (when elements have been added to the UR)
        and "M" (when existing elements have been modified). Response only.
    key_override
        If a duplicate key is found where we are adding elements in some
        cases like URAdd, then instead of erroring out set this attribute to
        true.
    operation
        "Type of exchange. Add - Add new Journey. Update - Modify existing
        Journey. Delete - Remove existing Journey"
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    rail_segment: list[RailSegment] = field(
        default_factory=list,
        metadata={
            "name": "RailSegment",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    rail_segment_ref: list[RailSegmentRef] = field(
        default_factory=list,
        metadata={
            "name": "RailSegmentRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    journey_remark: list[JourneyRemark] = field(
        default_factory=list,
        metadata={
            "name": "JourneyRemark",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    host_token: list[HostToken1] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
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
    departure_time: None | str = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Attribute",
            "required": True,
        }
    )
    arrival_time: None | str = field(
        default=None,
        metadata={
            "name": "ArrivalTime",
            "type": "Attribute",
        }
    )
    origin_station_name: None | str = field(
        default=None,
        metadata={
            "name": "OriginStationName",
            "type": "Attribute",
        }
    )
    destination_station_name: None | str = field(
        default=None,
        metadata={
            "name": "DestinationStationName",
            "type": "Attribute",
        }
    )
    rail_loc_origin: None | str = field(
        default=None,
        metadata={
            "name": "RailLocOrigin",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 8,
            "white_space": "collapse",
        }
    )
    rail_loc_destination: None | str = field(
        default=None,
        metadata={
            "name": "RailLocDestination",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 8,
            "white_space": "collapse",
        }
    )
    route_description: None | str = field(
        default=None,
        metadata={
            "name": "RouteDescription",
            "type": "Attribute",
            "max_length": 255,
        }
    )
    journey_direction: None | TypeJourneyDirection = field(
        default=None,
        metadata={
            "name": "JourneyDirection",
            "type": "Attribute",
        }
    )
    journey_duration: None | int = field(
        default=None,
        metadata={
            "name": "JourneyDuration",
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
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    supplier_code: None | str = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        }
    )
    status: None | str = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
        }
    )
    provider_reservation_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        }
    )
    passive_provider_reservation_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "PassiveProviderReservationInfoRef",
            "type": "Attribute",
        }
    )
    travel_order: None | int = field(
        default=None,
        metadata={
            "name": "TravelOrder",
            "type": "Attribute",
        }
    )
    route_reference: None | str = field(
        default=None,
        metadata={
            "name": "RouteReference",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 255,
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
    operation: None | str = field(
        default=None,
        metadata={
            "name": "Operation",
            "type": "Attribute",
        }
    )
