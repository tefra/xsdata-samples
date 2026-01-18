from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

from .block_part_version_structure import BlockPartVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrainBlockPartVersionStructure(BlockPartVersionStructure):
    class Meta:
        name = "TrainBlockPart_VersionStructure"

    start_time: XmlTime | None = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    start_time_day_offset: int | None = field(
        default=None,
        metadata={
            "name": "StartTimeDayOffset",
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
    end_time_day_offset: int | None = field(
        default=None,
        metadata={
            "name": "EndTimeDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_coupling: str | None = field(
        default=None,
        metadata={
            "name": "TypeOfCoupling",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
