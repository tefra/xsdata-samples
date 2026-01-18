from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.find import Find
from generali.models.self_mod import Self


@dataclass(kw_only=True)
class Links:
    class Meta:
        name = "_links"

    self_value: Self = field(
        metadata={
            "name": "self",
            "type": "Element",
            "required": True,
        }
    )
    find: Find = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
