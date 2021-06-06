from dataclasses import dataclass
from .train_version_structure import TrainVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Train(TrainVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
