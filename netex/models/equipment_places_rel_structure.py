from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .equipment_place import EquipmentPlace
from .equipment_place_ref import EquipmentPlaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EquipmentPlacesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "equipmentPlaces_RelStructure"

    equipment_place_ref_or_equipment_place: Iterable[
        Union[EquipmentPlaceRef, EquipmentPlace]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "EquipmentPlaceRef",
                    "type": EquipmentPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EquipmentPlace",
                    "type": EquipmentPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
