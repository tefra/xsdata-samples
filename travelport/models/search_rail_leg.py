from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.rail_leg_modifiers import RailLegModifiers
from travelport.models.rail_segment_list import RailSegmentList
from travelport.models.type_flexible_time_spec_1 import TypeFlexibleTimeSpec1
from travelport.models.type_search_location_1 import TypeSearchLocation1
from travelport.models.type_time_spec_1 import TypeTimeSpec1

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass
class SearchRailLeg:
    """
    Holds Origin, Destination, and Departure times for a Rail Leg to search for.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    search_origin: list[TypeSearchLocation1] = field(
        default_factory=list,
        metadata={
            "name": "SearchOrigin",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    search_destination: list[TypeSearchLocation1] = field(
        default_factory=list,
        metadata={
            "name": "SearchDestination",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    rail_segment_list: None | RailSegmentList = field(
        default=None,
        metadata={
            "name": "RailSegmentList",
            "type": "Element",
        },
    )
    search_dep_time: list[TypeFlexibleTimeSpec1] = field(
        default_factory=list,
        metadata={
            "name": "SearchDepTime",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    search_arv_time: list[TypeTimeSpec1] = field(
        default_factory=list,
        metadata={
            "name": "SearchArvTime",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    rail_leg_modifiers: None | RailLegModifiers = field(
        default=None,
        metadata={
            "name": "RailLegModifiers",
            "type": "Element",
        },
    )
