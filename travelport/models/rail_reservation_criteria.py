from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_date_spec import TypeDateSpec

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class RailReservationCriteria:
    """
    Criteria for searching the Rail reservations.

    Parameters
    ----------
    journey_departure_date
        Hotel Check In Date or Date Range
    journey_arrival_date
        Hotel Check In Date or Date Range
    segment_departure_date
        Hotel Check In Date or Date Range
    segment_arrival_date
        Hotel Check In Date or Date Range
    journey_origin
        The IATA location code for this origination of this entity.
    journey_destination
        The IATA location code for this destination of this entity.
    journey_rail_loc_origin
        RCH specific origin code (a.k.a UCodes) which uniquely identifies a
        train station.
    journey_rail_loc_destination
        RCH specific destination code (a.k.a UCodes) which uniquely
        identifies a train station.
    supplier_code
    train_number
    passive_only
        Search for Passives Only
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    journey_departure_date: None | TypeDateSpec = field(
        default=None,
        metadata={
            "name": "JourneyDepartureDate",
            "type": "Element",
        },
    )
    journey_arrival_date: None | TypeDateSpec = field(
        default=None,
        metadata={
            "name": "JourneyArrivalDate",
            "type": "Element",
        },
    )
    segment_departure_date: None | TypeDateSpec = field(
        default=None,
        metadata={
            "name": "SegmentDepartureDate",
            "type": "Element",
        },
    )
    segment_arrival_date: None | TypeDateSpec = field(
        default=None,
        metadata={
            "name": "SegmentArrivalDate",
            "type": "Element",
        },
    )
    journey_origin: None | str = field(
        default=None,
        metadata={
            "name": "JourneyOrigin",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        },
    )
    journey_destination: None | str = field(
        default=None,
        metadata={
            "name": "JourneyDestination",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        },
    )
    journey_rail_loc_origin: None | str = field(
        default=None,
        metadata={
            "name": "JourneyRailLocOrigin",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 8,
            "white_space": "collapse",
        },
    )
    journey_rail_loc_destination: None | str = field(
        default=None,
        metadata={
            "name": "JourneyRailLocDestination",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 8,
            "white_space": "collapse",
        },
    )
    supplier_code: None | str = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
        },
    )
    train_number: None | str = field(
        default=None,
        metadata={
            "name": "TrainNumber",
            "type": "Attribute",
        },
    )
    passive_only: bool = field(
        default=False,
        metadata={
            "name": "PassiveOnly",
            "type": "Attribute",
        },
    )
