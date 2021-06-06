from dataclasses import dataclass
from .train_in_compound_train_ref_structure import TrainInCompoundTrainRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrainInCompoundTrainRef(TrainInCompoundTrainRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
