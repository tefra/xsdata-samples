from dataclasses import dataclass

from .train_block_part_ref_structure import TrainBlockPartRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrainBlockPartRef(TrainBlockPartRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
