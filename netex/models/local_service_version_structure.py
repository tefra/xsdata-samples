from dataclasses import dataclass, field
from typing import Optional
from .equipment_version_structure import EquipmentVersionStructure
from .type_of_service_feature_refs_rel_structure import (
    TypeOfServiceFeatureRefsRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LocalServiceVersionStructure(EquipmentVersionStructure):
    class Meta:
        name = "LocalService_VersionStructure"

    types_of_service_feature: Optional[
        TypeOfServiceFeatureRefsRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "typesOfServiceFeature",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
