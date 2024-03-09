from dataclasses import dataclass

from .train_component_version_structure import TrainComponentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrainComponent(TrainComponentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
