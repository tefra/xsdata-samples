from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class RequestReferenceDataItem:
    """
    Limits the responses to the requested subcategories for a specific Reference
    Data Type, Currently supported only for @TypeCode="HotelAmenities".

    Parameters
    ----------
    request_amenity
        Requested decoded values only for the specified Hotel Amenity codes.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    request_amenity: list[RequestReferenceDataItem.RequestAmenity] = field(
        default_factory=list,
        metadata={
            "name": "RequestAmenity",
            "type": "Element",
            "max_occurs": 9,
        },
    )

    @dataclass
    class RequestAmenity:
        """
        Parameters
        ----------
        type_value
            Limits to the response to the requested amenity type. Can be a
            general type: “HA” (Hotel Property Amenity) or “RA” (Room
            Amenity). Or, a specific type, for example: “TR”
            (Transportation) or “BT” (Bed Type). If no type is specified,
            all amenity types are returned.
        """

        type_value: None | str = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
                "required": True,
                "length": 2,
            },
        )
