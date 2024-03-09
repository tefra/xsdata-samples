from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.number_of_adults import NumberOfAdults
from travelport.models.number_of_children import NumberOfChildren

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class GuestInformation:
    """
    The information like number of rooms ,number of adults,children to be provided
    while booking the  hotel.

    Parameters
    ----------
    number_of_adults
    number_of_children
    extra_child
        Providers: 1p
    number_of_rooms
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    number_of_adults: None | NumberOfAdults = field(
        default=None,
        metadata={
            "name": "NumberOfAdults",
            "type": "Element",
        },
    )
    number_of_children: None | NumberOfChildren = field(
        default=None,
        metadata={
            "name": "NumberOfChildren",
            "type": "Element",
        },
    )
    extra_child: None | GuestInformation.ExtraChild = field(
        default=None,
        metadata={
            "name": "ExtraChild",
            "type": "Element",
        },
    )
    number_of_rooms: None | int = field(
        default=None,
        metadata={
            "name": "NumberOfRooms",
            "type": "Attribute",
        },
    )

    @dataclass
    class ExtraChild:
        """
        Parameters
        ----------
        count
            The number of extra children in the room
        content
            Additional information
        """

        count: None | int = field(
            default=None,
            metadata={
                "name": "Count",
                "type": "Attribute",
            },
        )
        content: None | str = field(
            default=None,
            metadata={
                "name": "Content",
                "type": "Attribute",
            },
        )
