from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.rail_station_location_modifiers import (
    RailStationLocationModifiers,
)

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class ReferenceDataSearchModifiers:
    """
    Modifiers to narrow the reference data search results.

    Parameters
    ----------
    rail_station_location_modifiers
    max_results
        Used to limit the number of results returned.
    start_from_result
        Used to browse beyond the maximum number of results specified with
        the MaxResults parameter. Acts as an offset to skip the specified
        number of items from the begining of the result set.
    provider_code
        Provider Specific restriction(e.g. 1G, 1P etc) .
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    rail_station_location_modifiers: None | RailStationLocationModifiers = (
        field(
            default=None,
            metadata={
                "name": "RailStationLocationModifiers",
                "type": "Element",
            },
        )
    )
    max_results: int = field(
        default=20,
        metadata={
            "name": "MaxResults",
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )
    start_from_result: int = field(
        default=0,
        metadata={
            "name": "StartFromResult",
            "type": "Attribute",
            "min_inclusive": 0,
        },
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        },
    )
