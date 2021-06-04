from dataclasses import dataclass
from netex.models.compound_train_version_structure import CompoundTrainVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CompoundTrain(CompoundTrainVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
