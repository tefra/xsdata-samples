from dataclasses import dataclass
from netex.models.train_block_part_version_structure import TrainBlockPartVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrainBlockPart(TrainBlockPartVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
