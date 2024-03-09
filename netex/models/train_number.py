from dataclasses import dataclass

from .train_number_version_structure import TrainNumberVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrainNumber(TrainNumberVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
