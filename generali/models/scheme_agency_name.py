from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class SchemeAgencyName:
    class Meta:
        name = "@scheme-agency-name"

    type_value: str = field(
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
