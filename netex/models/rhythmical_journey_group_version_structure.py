from __future__ import annotations

from dataclasses import dataclass, field

from .journey_frequency_group_version_structure import (
    JourneyFrequencyGroupVersionStructure,
)
from .timeband_refs_rel_structure import TimebandRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RhythmicalJourneyGroupVersionStructure(
    JourneyFrequencyGroupVersionStructure
):
    class Meta:
        name = "RhythmicalJourneyGroup_VersionStructure"

    timebands: None | TimebandRefsRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
