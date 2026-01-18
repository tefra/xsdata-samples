from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_time_range_1 import TypeTimeRange1

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class McoCreateDate(TypeTimeRange1):
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"
