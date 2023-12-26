from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_leg_modifiers import AirLegModifiers
from travelport.models.type_flexible_time_spec_1 import TypeFlexibleTimeSpec1
from travelport.models.type_search_location_1 import TypeSearchLocation1
from travelport.models.type_time_spec_1 import TypeTimeSpec1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class SearchAirLeg:
    """
    Search version of AirLeg used to specify search criteria.

    Parameters
    ----------
    search_origin
    search_destination
    search_dep_time
    search_arv_time
        Specifies the preferred time within the time range. For 1G, 1V, 1P,
        it is supported for AvailabilitySearchReq (TimeRange must also be
        specified) and not supported for LowFareSearchReq. ACH does not
        support search by arrival time.
    air_leg_modifiers
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

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
            "max_occurs": 999,
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
    air_leg_modifiers: None | AirLegModifiers = field(
        default=None,
        metadata={
            "name": "AirLegModifiers",
            "type": "Element",
        },
    )
