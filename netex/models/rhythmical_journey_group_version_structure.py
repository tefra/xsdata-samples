from dataclasses import dataclass, field
from typing import Optional
from .journey_frequency_group_version_structure import (
    JourneyFrequencyGroupVersionStructure,
)
from .timeband_refs_rel_structure import TimebandRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RhythmicalJourneyGroupVersionStructure(
    JourneyFrequencyGroupVersionStructure
):
    class Meta:
        name = "RhythmicalJourneyGroup_VersionStructure"

    timebands: Optional[TimebandRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
