from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.alt_cities_combinations_locations_type import (
    AltCitiesCombinationsLocationsType,
)

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class AltCitiesCombinationsType:
    """
    Which (if any) alt cities locations should be handled in a special way (i.e.
    Validate instead of precomputed path).

    Attributes:
        origins: Which origins to process in live path (All or Main
            only)
        destinations: Which destinations to process in live path (All or
            Main only)
    """

    origins: AltCitiesCombinationsLocationsType = field(
        default=AltCitiesCombinationsLocationsType.MAIN,
        metadata={
            "name": "Origins",
            "type": "Attribute",
        },
    )
    destinations: AltCitiesCombinationsLocationsType = field(
        default=AltCitiesCombinationsLocationsType.MAIN,
        metadata={
            "name": "Destinations",
            "type": "Attribute",
        },
    )
