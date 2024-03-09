from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.grouped_option import GroupedOption

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class GroupedOptionInfo:
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    grouped_option: list[GroupedOption] = field(
        default_factory=list,
        metadata={
            "name": "GroupedOption",
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 999,
        },
    )
