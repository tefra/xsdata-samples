from dataclasses import dataclass, field
from typing import Optional

from generali.models.find import Find
from generali.models.self_mod import Self


@dataclass
class Links:
    class Meta:
        name = "_links"

    self_value: Self | None = field(
        default=None,
        metadata={
            "name": "self",
            "type": "Element",
            "required": True,
        },
    )
    find: Find | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
