from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_guest_child_information import (
    TypeGuestChildInformation,
)

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class TypeAdaptedRoomGuestAllocation:
    """The allocation of guests per room assigned by the aggregator or supplier
    (hotel property).

    Returned only when the requested guest allocation is different from
    the provider or supplier’s adapted guest allocation.

    Parameters
    ----------
    child
        Information about a child guest.
    number_of_adults
        The number of adult guests per room. Maximum number of adults may
        vary by supplier or aggregator.
    """

    class Meta:
        name = "typeAdaptedRoomGuestAllocation"

    child: list[TypeGuestChildInformation] = field(
        default_factory=list,
        metadata={
            "name": "Child",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_occurs": 6,
        },
    )
    number_of_adults: None | int = field(
        default=None,
        metadata={
            "name": "NumberOfAdults",
            "type": "Attribute",
        },
    )
