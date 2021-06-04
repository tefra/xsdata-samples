from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.alternative_texts_rel_structure import VersionedChildStructure
from netex.models.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from netex.models.journey_part_ref_structure import JourneyPartRefStructure
from netex.models.scheduled_stop_point_ref import ScheduledStopPointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyPartPositionVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "JourneyPartPosition_VersionedChildStructure"

    parent_journey_part_ref: Optional[JourneyPartRefStructure] = field(
        default=None,
        metadata={
            "name": "ParentJourneyPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_scheduled_stop_point_ref: List[FareScheduledStopPointRef] = field(
        default_factory=list,
        metadata={
            "name": "FareScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    scheduled_stop_point_ref: List[ScheduledStopPointRef] = field(
        default_factory=list,
        metadata={
            "name": "ScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    position_in_train: Optional[int] = field(
        default=None,
        metadata={
            "name": "PositionInTrain",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
