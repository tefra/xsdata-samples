from dataclasses import dataclass, field
from typing import Optional

from .journey_ref_structure import JourneyRefStructure
from .passing_time_versioned_child_structure import (
    PassingTimeVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DatedPassingTimeVersionedChildStructure(
    PassingTimeVersionedChildStructure
):
    class Meta:
        name = "DatedPassingTime_VersionedChildStructure"

    dated_journey_ref: JourneyRefStructure | None = field(
        default=None,
        metadata={
            "name": "DatedJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
