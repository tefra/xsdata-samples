from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class SchemeName:
    class Meta:
        name = "@scheme-name"

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
