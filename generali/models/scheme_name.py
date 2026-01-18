from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class SchemeName:
    class Meta:
        name = "@scheme-name"

    type_value: str = field(
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
