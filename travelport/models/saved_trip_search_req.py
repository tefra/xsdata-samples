from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_reservation_criteria import AirReservationCriteria
from travelport.models.base_req_1 import BaseReq1
from travelport.models.hotel_reservation_criteria import (
    HotelReservationCriteria,
)
from travelport.models.rail_reservation_criteria import RailReservationCriteria
from travelport.models.saved_trip_search_modifiers import (
    SavedTripSearchModifiers,
)
from travelport.models.search_agent import SearchAgent
from travelport.models.traveler_criteria_1 import TravelerCriteria1
from travelport.models.type_saved_trip_record_status import (
    TypeSavedTripRecordStatus,
)
from travelport.models.vehicle_reservation_criteria import (
    VehicleReservationCriteria,
)

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class SavedTripSearchReq(BaseReq1):
    """
    Request to retrieve a summary information for reservations under a
    SavedTrip.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    saved_trip_search_modifiers: None | SavedTripSearchModifiers = field(
        default=None,
        metadata={
            "name": "SavedTripSearchModifiers",
            "type": "Element",
        },
    )
    traveler_criteria: None | TravelerCriteria1 = field(
        default=None,
        metadata={
            "name": "TravelerCriteria",
            "type": "Element",
        },
    )
    search_agent: None | SearchAgent = field(
        default=None,
        metadata={
            "name": "SearchAgent",
            "type": "Element",
        },
    )
    air_reservation_criteria: None | AirReservationCriteria = field(
        default=None,
        metadata={
            "name": "AirReservationCriteria",
            "type": "Element",
        },
    )
    hotel_reservation_criteria: None | HotelReservationCriteria = field(
        default=None,
        metadata={
            "name": "HotelReservationCriteria",
            "type": "Element",
        },
    )
    vehicle_reservation_criteria: None | VehicleReservationCriteria = field(
        default=None,
        metadata={
            "name": "VehicleReservationCriteria",
            "type": "Element",
        },
    )
    rail_reservation_criteria: None | RailReservationCriteria = field(
        default=None,
        metadata={
            "name": "RailReservationCriteria",
            "type": "Element",
        },
    )
    record_status: None | TypeSavedTripRecordStatus = field(
        default=None,
        metadata={
            "name": "RecordStatus",
            "type": "Attribute",
        },
    )
