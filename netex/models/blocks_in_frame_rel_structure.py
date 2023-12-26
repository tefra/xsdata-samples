from dataclasses import dataclass, field
from typing import List, Union
from .block import Block
from .compound_block import CompoundBlock
from .containment_aggregation_structure import ContainmentAggregationStructure
from .train_block import TrainBlock

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BlocksInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "blocksInFrame_RelStructure"

    block_or_compound_block_or_train_block: List[
        Union[Block, CompoundBlock, TrainBlock]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Block",
                    "type": Block,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompoundBlock",
                    "type": CompoundBlock,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainBlock",
                    "type": TrainBlock,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
