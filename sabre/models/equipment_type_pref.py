from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.equipment_type import EquipmentType
from sabre.models.prefer_level_type import PreferLevelType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class EquipmentTypePref(EquipmentType):
    """
    Attributes:
        prefer_level:
        wide_body: Specify if equipment should have a wide body or not.
    """

    prefer_level: PreferLevelType = field(
        default=PreferLevelType.PREFERRED,
        metadata={
            "name": "PreferLevel",
            "type": "Attribute",
        },
    )
    wide_body: None | bool = field(
        default=None,
        metadata={
            "name": "WideBody",
            "type": "Attribute",
        },
    )
