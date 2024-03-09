from dataclasses import dataclass, field
from typing import Optional

from .block_version_structure import BlockVersionStructure
from .coupled_journeys_rel_structure import CoupledJourneysRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrainBlockVersionStructure(BlockVersionStructure):
    class Meta:
        name = "TrainBlock_VersionStructure"

    coupled_journeys: Optional[CoupledJourneysRelStructure] = field(
        default=None,
        metadata={
            "name": "coupledJourneys",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
