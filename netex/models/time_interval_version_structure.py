from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration, XmlTime

from .fare_interval_version_structure import FareIntervalVersionStructure
from .time_interval_prices_rel_structure import TimeIntervalPricesRelStructure
from .time_structure_factors_rel_structure import (
    TimeStructureFactorsRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimeIntervalVersionStructure(FareIntervalVersionStructure):
    class Meta:
        name = "TimeInterval_VersionStructure"

    start_time: XmlTime | None = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_time: XmlTime | None = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    day_offset: int | None = field(
        default=None,
        metadata={
            "name": "DayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    duration: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_duration: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "MinimumDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    prices: TimeIntervalPricesRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    time_structure_factors: TimeStructureFactorsRelStructure | None = field(
        default=None,
        metadata={
            "name": "timeStructureFactors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
