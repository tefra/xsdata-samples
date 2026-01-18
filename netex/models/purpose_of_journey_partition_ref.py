from __future__ import annotations

from dataclasses import dataclass

from .purpose_of_journey_partition_ref_structure import (
    PurposeOfJourneyPartitionRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PurposeOfJourneyPartitionRef(PurposeOfJourneyPartitionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
