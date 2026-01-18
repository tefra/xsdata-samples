from dataclasses import dataclass, field

from .block_ref import BlockRef
from .compound_block_ref import CompoundBlockRef
from .compound_train_ref import CompoundTrainRef
from .entity_in_version_structure import DataManagedObjectStructure
from .journey_part_couple_ref import JourneyPartCoupleRef
from .journey_part_refs_rel_structure import JourneyPartRefsRelStructure
from .multilingual_string import MultilingualString
from .train_block_ref import TrainBlockRef
from .train_ref import TrainRef
from .vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BlockPartVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "BlockPart_VersionStructure"

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
    block_ref: TrainBlockRef | BlockRef | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TrainBlockRef",
                    "type": TrainBlockRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BlockRef",
                    "type": BlockRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    vehicle_type_ref: CompoundTrainRef | TrainRef | VehicleTypeRef | None = (
        field(
            default=None,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "CompoundTrainRef",
                        "type": CompoundTrainRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "TrainRef",
                        "type": TrainRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "VehicleTypeRef",
                        "type": VehicleTypeRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                ),
            },
        )
    )
    compound_block_ref: CompoundBlockRef | None = field(
        default=None,
        metadata={
            "name": "CompoundBlockRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journey_part_couple_ref_or_journey_parts: (
        JourneyPartCoupleRef | JourneyPartRefsRelStructure | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "JourneyPartCoupleRef",
                    "type": JourneyPartCoupleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "journeyParts",
                    "type": JourneyPartRefsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    order: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
