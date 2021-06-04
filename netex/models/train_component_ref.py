from dataclasses import dataclass
from netex.models.train_component_ref_structure import TrainComponentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrainComponentRef(TrainComponentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
