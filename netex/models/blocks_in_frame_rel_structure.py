from dataclasses import dataclass, field
from typing import List
from .block import Block
from .compound_block import CompoundBlock
from .containment_aggregation_structure import ContainmentAggregationStructure
from .train_block import TrainBlock

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BlocksInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "blocksInFrame_RelStructure"

    block: List[Block] = field(
        default_factory=list,
        metadata={
            "name": "Block",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    compound_block: List[CompoundBlock] = field(
        default_factory=list,
        metadata={
            "name": "CompoundBlock",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_block: List[TrainBlock] = field(
        default_factory=list,
        metadata={
            "name": "TrainBlock",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )