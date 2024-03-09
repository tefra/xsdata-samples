from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlTime

from .block_part_version_structure import BlockPartVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrainBlockPartVersionStructure(BlockPartVersionStructure):
    class Meta:
        name = "TrainBlockPart_VersionStructure"

    start_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    start_time_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "StartTimeDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_time_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "EndTimeDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_coupling: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypeOfCoupling",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
