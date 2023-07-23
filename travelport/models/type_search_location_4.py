from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.airport_4 import Airport4
from travelport.models.city_4 import City4
from travelport.models.city_or_airport_4 import CityOrAirport4
from travelport.models.coordinate_location_4 import CoordinateLocation4
from travelport.models.distance_4 import Distance4
from travelport.models.rail_location_4 import RailLocation4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class TypeSearchLocation4:
    class Meta:
        name = "typeSearchLocation"

    airport: None | Airport4 = field(
        default=None,
        metadata={
            "name": "Airport",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        }
    )
    city: None | City4 = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        }
    )
    city_or_airport: None | CityOrAirport4 = field(
        default=None,
        metadata={
            "name": "CityOrAirport",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        }
    )
    coordinate_location: None | CoordinateLocation4 = field(
        default=None,
        metadata={
            "name": "CoordinateLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        }
    )
    rail_location: None | RailLocation4 = field(
        default=None,
        metadata={
            "name": "RailLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        }
    )
    distance: None | Distance4 = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        }
    )
