from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlTime
from .alternative_texts_rel_structure import DataManagedObjectStructure
from .block_ref import BlockRef
from .journey_part_ref_structure import JourneyPartRefStructure
from .journey_part_refs_rel_structure import JourneyPartRefsRelStructure
from .multilingual_string import MultilingualString
from .scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from .train_block_ref import TrainBlockRef
from .train_number_ref import TrainNumberRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyPartCoupleVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "JourneyPartCouple_VersionStructure"

    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    start_time_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "StartTimeDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    end_time_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "EndTimeDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    from_stop_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "FromStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    to_stop_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "ToStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    main_part_ref: Optional[JourneyPartRefStructure] = field(
        default=None,
        metadata={
            "name": "MainPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    train_block_ref: List[TrainBlockRef] = field(
        default_factory=list,
        metadata={
            "name": "TrainBlockRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
        }
    )
    block_ref: Optional[BlockRef] = field(
        default=None,
        metadata={
            "name": "BlockRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_parts: Optional[JourneyPartRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "journeyParts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_number_ref: Optional[TrainNumberRef] = field(
        default=None,
        metadata={
            "name": "TrainNumberRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )