from dataclasses import dataclass, field
from typing import List, Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.road_type_enum import RoadTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Road:
    """Identification of a road by its name, identifier, type ...

    :ivar name_of_road: The name of the road.
    :ivar road_identifier: Identifier/number of the road.
    :ivar type_of_road: Type of the road.
    :ivar road_destination: Name of some city, area, compass direction
        or other identification the road is leading to (to determine the
        direction in question).
    :ivar road_origination: Name of some city, area, compass direction
        or other identification this road comes from.
    :ivar distance_to_this_road: Distance to the road in metres (from
        the calling component/object).
    :ivar road_extension:
    """
    name_of_road: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "nameOfRoad",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    road_identifier: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "roadIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    type_of_road: Optional[RoadTypeEnum] = field(
        default=None,
        metadata={
            "name": "typeOfRoad",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    road_destination: List[MultilingualString] = field(
        default_factory=list,
        metadata={
            "name": "roadDestination",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    road_origination: List[MultilingualString] = field(
        default_factory=list,
        metadata={
            "name": "roadOrigination",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    distance_to_this_road: Optional[int] = field(
        default=None,
        metadata={
            "name": "distanceToThisRoad",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    road_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
