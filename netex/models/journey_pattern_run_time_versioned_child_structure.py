from dataclasses import dataclass, field
from typing import Optional, Union

from .dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from .journey_pattern_ref import JourneyPatternRef
from .journey_run_time_versioned_child_structure import (
    JourneyRunTimeVersionedChildStructure,
)
from .service_journey_pattern_ref import ServiceJourneyPatternRef
from .service_pattern_ref import ServicePatternRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyPatternRunTimeVersionedChildStructure(
    JourneyRunTimeVersionedChildStructure
):
    class Meta:
        name = "JourneyPatternRunTime_VersionedChildStructure"

    journey_pattern_ref: Optional[
        Union[
            ServiceJourneyPatternRef,
            ServicePatternRef,
            DeadRunJourneyPatternRef,
            JourneyPatternRef,
        ]
    ] = field(
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
