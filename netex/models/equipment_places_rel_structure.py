from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .equipment_place import EquipmentPlace
from .equipment_place_ref import EquipmentPlaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EquipmentPlacesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "equipmentPlaces_RelStructure"

    equipment_place_ref: List[EquipmentPlaceRef] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    equipment_place: List[EquipmentPlace] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
