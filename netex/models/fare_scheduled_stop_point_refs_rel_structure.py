from collections.abc import Iterable
from dataclasses import dataclass, field

from .fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareScheduledStopPointRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "fareScheduledStopPointRefs_RelStructure"

    fare_scheduled_stop_point_ref: Iterable[FareScheduledStopPointRef] = field(
        default_factory=list,
        metadata={
            "name": "FareScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
