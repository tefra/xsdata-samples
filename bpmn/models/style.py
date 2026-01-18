from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.omg.org/spec/DD/20100524/DI"


@dataclass(kw_only=True)
class Style:
    class Meta:
        namespace = "http://www.omg.org/spec/DD/20100524/DI"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
