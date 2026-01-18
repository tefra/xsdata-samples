from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_date_spec import TypeDateSpec

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass(kw_only=True)
class HotelReservationCriteria:
    """
    Criteria for searching the Hotel reservations.

    Parameters
    ----------
    check_in_date
        Hotel Check In Date or Date Range
    hotel_chain_code
        Hotel Chain Code
    hotel_code
    hotel_confirmation
    location
    passive_only
        Search for Passives Only
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    check_in_date: None | TypeDateSpec = field(
        default=None,
        metadata={
            "name": "CheckInDate",
            "type": "Element",
        },
    )
    hotel_chain_code: None | str = field(
        default=None,
        metadata={
            "name": "HotelChainCode",
            "type": "Attribute",
            "length": 2,
        },
    )
    hotel_code: None | str = field(
        default=None,
        metadata={
            "name": "HotelCode",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    hotel_confirmation: None | str = field(
        default=None,
        metadata={
            "name": "HotelConfirmation",
            "type": "Attribute",
        },
    )
    location: None | str = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        },
    )
    passive_only: bool = field(
        default=False,
        metadata={
            "name": "PassiveOnly",
            "type": "Attribute",
        },
    )
