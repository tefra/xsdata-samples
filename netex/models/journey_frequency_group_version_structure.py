from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

from .explicit_journey_refs_rel_structure import (
    ExplicitJourneyRefsRelStructure,
)
from .group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)
from .time_demand_type_refs_rel_structure import TimeDemandTypeRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyFrequencyGroupVersionStructure(GroupOfEntitiesVersionStructure):
    class Meta:
        name = "JourneyFrequencyGroup_VersionStructure"

    first_departure_time: XmlTime | None = field(
        default=None,
        metadata={
            "name": "FirstDepartureTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    first_day_offset: int | None = field(
        default=None,
        metadata={
            "name": "FirstDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    last_departure_time: XmlTime | None = field(
        default=None,
        metadata={
            "name": "LastDepartureTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    last_day_offset: int | None = field(
        default=None,
        metadata={
            "name": "LastDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    time_demand_types: TimeDemandTypeRefsRelStructure | None = field(
        default=None,
        metadata={
            "name": "timeDemandTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journeys: ExplicitJourneyRefsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
