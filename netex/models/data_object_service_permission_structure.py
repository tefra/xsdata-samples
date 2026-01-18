from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DataObjectServicePermissionStructure:
    value: None | float = field(
        default=None,
        metadata={
            "required": True,
        },
    )
