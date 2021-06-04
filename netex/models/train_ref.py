from dataclasses import dataclass
from netex.models.train_ref_structure import TrainRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrainRef(TrainRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
