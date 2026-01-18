from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass(kw_only=True)
class HotelBedding:
    """
    Specify desired bedding.

    Parameters
    ----------
    type_value
        Queen, King, double, etc
    number_of_beds
        Number of beds of desired Type in room. Use '0' to delete the hotel
        Optional Beds ( Only RA RC CR )
    amount
        Fee for bed type.  Providers:  1g/1v/1p
    content
        Additional information Providers: 1p
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    type_value: str = field(
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
            "max_length": 15,
        }
    )
    number_of_beds: None | int = field(
        default=None,
        metadata={
            "name": "NumberOfBeds",
            "type": "Attribute",
        },
    )
    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
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
