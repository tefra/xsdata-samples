from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_keyword_1 import TypeKeyword1

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class Policy(TypeKeyword1):
    """Policy category code, e.g. “AGE”.

    Valid for 1P only.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"
