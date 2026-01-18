from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.fare_validity import FareValidity
from travelport.models.ful_fillment_type import FulFillmentType
from travelport.models.host_token_1 import HostToken1
from travelport.models.rail_fare_component import RailFareComponent
from travelport.models.rail_fare_id import RailFareId
from travelport.models.rail_fare_idref import RailFareIdref
from travelport.models.rail_fare_note_ref import RailFareNoteRef
from travelport.models.type_element_status_1 import TypeElementStatus1
from travelport.models.type_journey_direction import TypeJourneyDirection

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass(kw_only=True)
class RailFare:
    """
    Information about this fare component.

    Parameters
    ----------
    rail_fare_note_ref
        Key reference to RailFareNote present in RailFareNotList
    rail_fare_id
    rail_fare_idref
    fare_validity
    host_token
    ful_fillment_type
    rail_fare_component
    key
    fare_basis
        The fare basis code  or fare description for this fare
    cabin_class
        The fare basis code or fare class for this fare
    passenger_type_code
        The PTC that is associated with this fare. Default to ADT
    origin
        Returns the airport or city code that defines the origin market for
        this fare.
    destination
        Returns the airport or city code that defines the destination market
        for this fare.
    effective_date
        Returns the date on which this fare was quoted. Set as current date
    amount
    route_description
        Describes the route of the train fare.
    ticket_type_code
        Describes the main identifier code of the fare.
    fare_reference
        Unique reference for the fare that is required in RailExchangeQuote
        request.
    cross_city_fare
        Set to 'true' if the fare is valid across a Metropolitan Area, eg.
        Cross-London travel via the London Underground.
    origin_station_name
        The origin station name for the Rail Fare.
    destination_station_name
        The destination station name for the Rail Fare.
    reservation_required
        Set to true if a seat reservation is required while booking.
    journey_direction
        The direction of the Journey (Outward or Return) associated with the
        Rail fare.
    rail_loc_origin
        RCH specific origin code (a.k.a UCodes) which uniquely identifies a
        train station.
    rail_loc_destination
        RCH specific destination code (a.k.a UCodes) which uniquely
        identifies a train station.
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

    rail_fare_note_ref: list[RailFareNoteRef] = field(
        default_factory=list,
        metadata={
            "name": "RailFareNoteRef",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    rail_fare_id: list[RailFareId] = field(
        default_factory=list,
        metadata={
            "name": "RailFareID",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    rail_fare_idref: list[RailFareIdref] = field(
        default_factory=list,
        metadata={
            "name": "RailFareIDRef",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    fare_validity: list[FareValidity] = field(
        default_factory=list,
        metadata={
            "name": "FareValidity",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    host_token: None | HostToken1 = field(
        default=None,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    ful_fillment_type: list[FulFillmentType] = field(
        default_factory=list,
        metadata={
            "name": "FulFillmentType",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    rail_fare_component: list[RailFareComponent] = field(
        default_factory=list,
        metadata={
            "name": "RailFareComponent",
            "type": "Element",
            "max_occurs": 99,
        },
    )
    key: str = field(
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    fare_basis: None | str = field(
        default=None,
        metadata={
            "name": "FareBasis",
            "type": "Attribute",
        },
    )
    cabin_class: str = field(
        metadata={
            "name": "CabinClass",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
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
    origin: None | str = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        },
    )
    destination: None | str = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        },
    )
    effective_date: str = field(
        metadata={
            "name": "EffectiveDate",
            "type": "Attribute",
            "required": True,
        }
    )
    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        },
    )
    route_description: None | str = field(
        default=None,
        metadata={
            "name": "RouteDescription",
            "type": "Attribute",
        },
    )
    ticket_type_code: None | str = field(
        default=None,
        metadata={
            "name": "TicketTypeCode",
            "type": "Attribute",
        },
    )
    fare_reference: None | str = field(
        default=None,
        metadata={
            "name": "FareReference",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        },
    )
    cross_city_fare: bool = field(
        default=False,
        metadata={
            "name": "CrossCityFare",
            "type": "Attribute",
        },
    )
    origin_station_name: None | str = field(
        default=None,
        metadata={
            "name": "OriginStationName",
            "type": "Attribute",
        },
    )
    destination_station_name: None | str = field(
        default=None,
        metadata={
            "name": "DestinationStationName",
            "type": "Attribute",
        },
    )
    reservation_required: None | bool = field(
        default=None,
        metadata={
            "name": "ReservationRequired",
            "type": "Attribute",
        },
    )
    journey_direction: None | TypeJourneyDirection = field(
        default=None,
        metadata={
            "name": "JourneyDirection",
            "type": "Attribute",
        },
    )
    rail_loc_origin: None | str = field(
        default=None,
        metadata={
            "name": "RailLocOrigin",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 8,
            "white_space": "collapse",
        },
    )
    rail_loc_destination: None | str = field(
        default=None,
        metadata={
            "name": "RailLocDestination",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 8,
            "white_space": "collapse",
        },
    )
    el_stat: None | TypeElementStatus1 = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        },
    )
    key_override: None | bool = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        },
    )
