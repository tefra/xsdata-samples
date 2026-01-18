from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class CoordinatesStructure:
    value: Iterable[str] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
