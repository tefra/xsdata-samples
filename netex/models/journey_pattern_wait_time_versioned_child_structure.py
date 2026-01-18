from dataclasses import dataclass, field

from .dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from .journey_pattern_ref import JourneyPatternRef
from .journey_wait_time_versioned_child_structure import (
    JourneyWaitTimeVersionedChildStructure,
)
from .service_journey_pattern_ref import ServiceJourneyPatternRef
from .service_pattern_ref import ServicePatternRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyPatternWaitTimeVersionedChildStructure(
    JourneyWaitTimeVersionedChildStructure
):
    class Meta:
        name = "JourneyPatternWaitTime_VersionedChildStructure"

    journey_pattern_ref: (
        ServiceJourneyPatternRef
        | ServicePatternRef
        | DeadRunJourneyPatternRef
        | JourneyPatternRef
        | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceJourneyPatternRef",
                    "type": ServiceJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicePatternRef",
                    "type": ServicePatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRunJourneyPatternRef",
                    "type": DeadRunJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternRef",
                    "type": JourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
