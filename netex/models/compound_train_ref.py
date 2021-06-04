from dataclasses import dataclass
from netex.models.compound_train_ref_structure import CompoundTrainRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CompoundTrainRef(CompoundTrainRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
