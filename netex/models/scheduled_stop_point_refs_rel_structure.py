from dataclasses import dataclass, field
from typing import Optional, Union
from .fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .scheduled_stop_point_ref import ScheduledStopPointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ScheduledStopPointRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "scheduledStopPointRefs_RelStructure"

    scheduled_stop_point_ref: Optional[
        Union[FareScheduledStopPointRef, ScheduledStopPointRef]
    ] = field(
        default=None,
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
        },
    )
