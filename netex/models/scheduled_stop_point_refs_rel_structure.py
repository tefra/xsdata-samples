from dataclasses import dataclass, field
from typing import Optional
from netex.models.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.models.scheduled_stop_point_ref import ScheduledStopPointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ScheduledStopPointRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "scheduledStopPointRefs_RelStructure"

    fare_scheduled_stop_point_ref: Optional[FareScheduledStopPointRef] = field(
        default=None,
        metadata={
            "name": "FareScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    scheduled_stop_point_ref: Optional[ScheduledStopPointRef] = field(
        default=None,
        metadata={
            "name": "ScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
