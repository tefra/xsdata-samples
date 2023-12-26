from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class SeatInformation:
    """Additional information about seats.

    Providers: 1G, 1V, 1P,ACH

    Parameters
    ----------
    power
        Detail about any electrical power the seat might have. For example:
        No Power Providers: 1G, 1V, 1P
    video
        Detail about any video components the seat might have. For example:
        No Video Providers: 1G, 1V, 1P
    type_value
        Detail about the type of seat. For example: Exit Row, Standard, etc.
        Providers: 1G, 1V, 1P
    description
        Detailed description of the seat. Providers: 1G, 1V, 1P
    rating
        Definition of the seat rating. Providers: 1G, 1V, 1P
    key
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    power: None | str = field(
        default=None,
        metadata={
            "name": "Power",
            "type": "Element",
            "required": True,
        },
    )
    video: None | str = field(
        default=None,
        metadata={
            "name": "Video",
            "type": "Element",
            "required": True,
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "required": True,
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "required": True,
        },
    )
    rating: None | SeatInformation.Rating = field(
        default=None,
        metadata={
            "name": "Rating",
            "type": "Element",
            "required": True,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        },
    )

    @dataclass
    class Rating:
        """
        Parameters
        ----------
        value
        number
            Numerical rating of the seat from 1 to 5 with 1 being bad and 5
            being good. Providers: 1G, 1V, 1P
        """

        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        number: None | int = field(
            default=None,
            metadata={
                "name": "Number",
                "type": "Attribute",
                "required": True,
            },
        )
