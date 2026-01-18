from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.name_1 import Name1
from travelport.models.type_product_info import TypeProductInfo
from travelport.models.type_record_status import TypeRecordStatus
from travelport.models.type_reservation_ticketed import TypeReservationTicketed
from travelport.models.urticket_status import UrticketStatus

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass(kw_only=True)
class UniversalRecordSearchResult:
    """
    Container for reservations that match the search criteria.

    Parameters
    ----------
    product_info
    universal_record_locator_code
    earliest_travel_date
        The date on which th earliest travel can occur
    created_date
        The date the resevation record was created
    saved_trip_locator_code
        Locator Code of the Saved Trip that is associated to the Universal
        Record.
    ticketed
        If the universal record is ticketed or not or partially ticketed
    record_status
        Status of Universal Record e.g. Current,Past,Cancelled
    ticket_status
        If the universal record is ticketed or not or partially ticketed
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    product_info: list[UniversalRecordSearchResult.ProductInfo] = field(
        default_factory=list,
        metadata={
            "name": "ProductInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    universal_record_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "UniversalRecordLocatorCode",
            "type": "Attribute",
        },
    )
    earliest_travel_date: None | str = field(
        default=None,
        metadata={
            "name": "EarliestTravelDate",
            "type": "Attribute",
        },
    )
    created_date: None | str = field(
        default=None,
        metadata={
            "name": "CreatedDate",
            "type": "Attribute",
        },
    )
    saved_trip_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "SavedTripLocatorCode",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
        },
    )
    ticketed: None | TypeReservationTicketed = field(
        default=None,
        metadata={
            "name": "Ticketed",
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
    ticket_status: None | UrticketStatus = field(
        default=None,
        metadata={
            "name": "TicketStatus",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class ProductInfo(TypeProductInfo):
        name: list[Name1] = field(
            default_factory=list,
            metadata={
                "name": "Name",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
                "max_occurs": 999,
            },
        )
