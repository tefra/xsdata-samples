from dataclasses import dataclass, field
from typing import Optional
from generali.models.find import Find
from generali.models.self_mod import Self


@dataclass
class Links:
    class Meta:
        name = "_links"

    self_value: Optional[Self] = field(
        default=None,
        metadata={
            "name": "self",
            "type": "Element",
            "required": True,
        }
    )
    find: Optional[Find] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
