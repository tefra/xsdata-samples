from dataclasses import dataclass

from .train_size_structure import TrainSizeStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrainSize(TrainSizeStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
