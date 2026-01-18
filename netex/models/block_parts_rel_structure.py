from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

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

    choice: Iterable[
        TrainBlockPartRef | BlockPartRef | BlockPart | TrainBlockPart
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TrainBlockPartRef",
                    "type": TrainBlockPartRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BlockPartRef",
                    "type": BlockPartRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BlockPart",
                    "type": BlockPart,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainBlockPart",
                    "type": TrainBlockPart,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
