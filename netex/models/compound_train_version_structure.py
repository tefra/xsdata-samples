from dataclasses import dataclass, field
from typing import Optional
from .trains_in_compound_train_rel_structure import TrainsInCompoundTrainRelStructure
from .vehicle_type_version_structure import VehicleTypeVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CompoundTrainVersionStructure(VehicleTypeVersionStructure):
    class Meta:
        name = "CompoundTrain_VersionStructure"

    components: Optional[TrainsInCompoundTrainRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
