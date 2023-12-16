from dataclasses import dataclass, field
from typing import List, Optional, Union
from .alternative_texts_rel_structure import VersionedChildStructure
from .fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from .journey_part_ref_structure import JourneyPartRefStructure
from .scheduled_stop_point_ref import ScheduledStopPointRef

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
    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref: List[Union[FareScheduledStopPointRef, ScheduledStopPointRef]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareScheduledStopPointRef",
                    "type": FareScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledStopPointRef",
                    "type": ScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
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
