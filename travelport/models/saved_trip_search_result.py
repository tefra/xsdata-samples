from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.name_1 import Name1
from travelport.models.type_saved_trip_product_info import (
    TypeSavedTripProductInfo,
)

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class SavedTripSearchResult:
    """
    Container for SavedTrp that match the search criteria.

    Parameters
    ----------
    product_info
    earliest_travel_date
        The date on which the earliest travel can occur.
    created_date
        The date the SavedTrip was created.
    saved_trip_name
    locator_code
    universal_record_locator_code
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    product_info: list[SavedTripSearchResult.ProductInfo] = field(
        default_factory=list,
        metadata={
            "name": "ProductInfo",
            "type": "Element",
            "max_occurs": 999,
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
    saved_trip_name: None | str = field(
        default=None,
        metadata={
            "name": "SavedTripName",
            "type": "Attribute",
            "required": True,
        },
    )
    locator_code: None | str = field(
        default=None,
        metadata={
            "name": "LocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        },
    )
    universal_record_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "UniversalRecordLocatorCode",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
        },
    )

    @dataclass
    class ProductInfo(TypeSavedTripProductInfo):
        name: list[Name1] = field(
            default_factory=list,
            metadata={
                "name": "Name",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
                "max_occurs": 999,
            },
        )
