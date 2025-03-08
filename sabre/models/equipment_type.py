from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class EquipmentType:
    """
    Specifies the aircraft equipment type.

    Attributes:
        value:
        air_equip_type: This is the 3 character IATA code.
        change_of_gauge: Indicates there is an equipment change.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    air_equip_type: None | str = field(
        default=None,
        metadata={
            "name": "AirEquipType",
            "type": "Attribute",
            "required": True,
            "min_length": 3,
            "max_length": 3,
        },
    )
    change_of_gauge: bool = field(
        default=False,
        metadata={
            "name": "ChangeofGauge",
            "type": "Attribute",
        },
    )
