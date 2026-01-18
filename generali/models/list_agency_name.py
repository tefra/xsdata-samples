from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class ListAgencyName:
    class Meta:
        name = "@list-agency-name"

    type_value: str = field(
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
