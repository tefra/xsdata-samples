from dataclasses import dataclass, field
from typing import Optional

from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString
from .train_block_ref import TrainBlockRef
from .vehicle_journey_refs_rel_structure import VehicleJourneyRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CoupledJourneyVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "CoupledJourney_VersionStructure"

    name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    train_block_ref: TrainBlockRef | None = field(
        default=None,
        metadata={
            "name": "TrainBlockRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journeys: VehicleJourneyRefsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
