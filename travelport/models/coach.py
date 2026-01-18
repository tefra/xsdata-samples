from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.characteristic_2 import Characteristic2
from travelport.models.remark_1 import Remark1

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass(kw_only=True)
class Coach:
    """
    Captures rail seat map/coach map information.

    Parameters
    ----------
    characteristic
    remark
    coach_number
        Coach number for which seat map/coach map is returned.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    characteristic: None | Characteristic2 = field(
        default=None,
        metadata={
            "name": "Characteristic",
            "type": "Element",
        },
    )
    remark: list[Remark1] = field(
        default_factory=list,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    coach_number: None | str = field(
        default=None,
        metadata={
            "name": "CoachNumber",
            "type": "Attribute",
        },
    )
