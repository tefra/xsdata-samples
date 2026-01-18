from __future__ import annotations

from dataclasses import dataclass, field

from .type_of_battery_chemistry_value_structure import (
    TypeOfBatteryChemistryValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfBatteryChemistry(TypeOfBatteryChemistryValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    name_of_classified_entity_class: str = field(
        init=False,
        default="BatteryChemistry",
        metadata={
            "name": "nameOfClassifiedEntityClass",
            "type": "Attribute",
        },
    )
