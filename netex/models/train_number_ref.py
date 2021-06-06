from dataclasses import dataclass
from .train_number_ref_structure import TrainNumberRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrainNumberRef(TrainNumberRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
