from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_1 import BaseReq1
from travelport.models.provider_reservation_divide_req_create_child_universal_record import (
    ProviderReservationDivideReqCreateChildUniversalRecord,
)

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass(kw_only=True)
class ProviderReservationDivideReq(BaseReq1):
    """
    Request to split a PNR containing atleast 1 air reservation .

    Parameters
    ----------
    booking_traveler_ref
        Reference Element for Booking Traveler
    universal_record_locator_code
        Represents a valid Universal Record locator code
    provider_code
    provider_locator_code
    create_child_universal_record
        Represents the options given to the user to store the Child PNR
        inside existing  UR or in new UR after split.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    booking_traveler_ref: list[
        ProviderReservationDivideReq.BookingTravelerRef
    ] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    universal_record_locator_code: str = field(
        metadata={
            "name": "UniversalRecordLocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    provider_code: str = field(
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )
    provider_locator_code: str = field(
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "required": True,
            "max_length": 15,
        }
    )
    create_child_universal_record: ProviderReservationDivideReqCreateChildUniversalRecord = field(
        metadata={
            "name": "CreateChildUniversalRecord",
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass(kw_only=True)
    class BookingTravelerRef:
        key: str = field(
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )
