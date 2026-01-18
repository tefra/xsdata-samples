from dataclasses import dataclass, field
from typing import Optional

from .train_components_rel_structure import TrainComponentsRelStructure
from .train_size import TrainSize
from .vehicle_type_version_structure import VehicleTypeVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrainVersionStructure(VehicleTypeVersionStructure):
    class Meta:
        name = "Train_VersionStructure"

    train_size: TrainSize | None = field(
        default=None,
        metadata={
            "name": "TrainSize",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    components: TrainComponentsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
