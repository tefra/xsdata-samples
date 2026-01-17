from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from travelport.models.air_reservation_criteria import AirReservationCriteria
from travelport.models.base_req_1 import BaseReq1
from travelport.models.hotel_reservation_criteria import (
    HotelReservationCriteria,
)
from travelport.models.rail_reservation_criteria import RailReservationCriteria
from travelport.models.search_account import SearchAccount
from travelport.models.search_agent import SearchAgent
from travelport.models.traveler_criteria_1 import TravelerCriteria1
from travelport.models.type_record_status import TypeRecordStatus
from travelport.models.universal_record_search_modifiers import (
    UniversalRecordSearchModifiers,
)
from travelport.models.urticket_status import UrticketStatus
from travelport.models.vehicle_reservation_criteria import (
    VehicleReservationCriteria,
)

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class UniversalRecordSearchReq(BaseReq1):
    """
    Request to retrieve a summary information for reservations under a
    Universal Record.

    Parameters
    ----------
    universal_record_search_modifiers
    traveler_criteria
    search_agent
    air_reservation_criteria
    hotel_reservation_criteria
    vehicle_reservation_criteria
    rail_reservation_criteria
    search_account
    action_date
    record_status
    client_id
    provider_code
    provider_locator_code
    external_search_index
    restrict_to_profile_id
        Used to restrict the search to a specific Branch, Branch Group or
        Agency
    passive_only
        Search for Passives Only
    ticket_status
        Search universal record with Ticket Status
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_record_search_modifiers: (
        None | UniversalRecordSearchModifiers
    ) = field(
        default=None,
        metadata={
            "name": "UniversalRecordSearchModifiers",
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
    search_account: None | SearchAccount = field(
        default=None,
        metadata={
            "name": "SearchAccount",
            "type": "Element",
        },
    )
    action_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "ActionDate",
            "type": "Attribute",
        },
    )
    record_status: None | TypeRecordStatus = field(
        default=None,
        metadata={
            "name": "RecordStatus",
            "type": "Attribute",
        },
    )
    client_id: None | str = field(
        default=None,
        metadata={
            "name": "ClientId",
            "type": "Attribute",
        },
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
        },
    )
    provider_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
        },
    )
    external_search_index: None | str = field(
        default=None,
        metadata={
            "name": "ExternalSearchIndex",
            "type": "Attribute",
        },
    )
    restrict_to_profile_id: None | object = field(
        default=None,
        metadata={
            "name": "RestrictToProfileId",
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
    ticket_status: None | UrticketStatus = field(
        default=None,
        metadata={
            "name": "TicketStatus",
            "type": "Attribute",
        },
    )
