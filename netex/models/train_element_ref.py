from dataclasses import dataclass
from netex.models.train_element_ref_structure import TrainElementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrainElementRef(TrainElementRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
