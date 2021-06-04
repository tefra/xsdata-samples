from dataclasses import dataclass, field
from typing import Optional
from netex.models.journey_ref_structure import JourneyRefStructure
from netex.models.passing_time_versioned_child_structure import PassingTimeVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DatedPassingTimeVersionedChildStructure(PassingTimeVersionedChildStructure):
    class Meta:
        name = "DatedPassingTime_VersionedChildStructure"

    dated_journey_ref: Optional[JourneyRefStructure] = field(
        default=None,
        metadata={
            "name": "DatedJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
