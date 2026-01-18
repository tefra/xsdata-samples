from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ListAgencyName:
    class Meta:
        name = "@list-agency-name"

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
