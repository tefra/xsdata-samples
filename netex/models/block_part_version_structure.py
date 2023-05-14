from dataclasses import dataclass, field
from typing import Optional
from .alternative_texts_rel_structure import DataManagedObjectStructure
from .block_ref import BlockRef
from .compound_block_ref import CompoundBlockRef
from .compound_train_ref import CompoundTrainRef
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

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_block_ref_or_block_ref: Optional[object] = field(
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
        }
    )
    compound_train_ref_or_train_ref_or_vehicle_type_ref: Optional[object] = field(
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
        }
    )
    compound_block_ref: Optional[CompoundBlockRef] = field(
        default=None,
        metadata={
            "name": "CompoundBlockRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_part_couple_ref_or_journey_parts: Optional[object] = field(
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
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
