from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_coach_class_type import TypeCoachClassType

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass
class Characteristic2:
    """
    Defines coach characteristics such as accommodation class, smoking
    choice, etc.
    """

    class Meta:
        name = "Characteristic"
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    smoking: bool = field(
        default=False,
        metadata={
            "name": "Smoking",
            "type": "Attribute",
        },
    )
    class_value: None | TypeCoachClassType = field(
        default=None,
        metadata={
            "name": "Class",
            "type": "Attribute",
        },
    )
