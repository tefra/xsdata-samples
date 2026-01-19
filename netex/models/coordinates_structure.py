from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class CoordinatesStructure:
    value: Sequence[str] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
