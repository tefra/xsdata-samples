from dataclasses import dataclass, field
from typing import List
from .block_part import BlockPart
from .block_part_ref import BlockPartRef
from .containment_aggregation_structure import ContainmentAggregationStructure
from .train_block_part import TrainBlockPart
from .train_block_part_ref import TrainBlockPartRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BlockPartsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "blockParts_RelStructure"

    train_block_part_ref: List[TrainBlockPartRef] = field(
        default_factory=list,
        metadata={
            "name": "TrainBlockPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    block_part_ref: List[BlockPartRef] = field(
        default_factory=list,
        metadata={
            "name": "BlockPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    block_part: List[BlockPart] = field(
        default_factory=list,
        metadata={
            "name": "BlockPart",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_block_part: List[TrainBlockPart] = field(
        default_factory=list,
        metadata={
            "name": "TrainBlockPart",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
