from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class CodeListType:
    value: Sequence[str] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
    code_space: None | str = field(
        default=None,
        metadata={
            "name": "codeSpace",
            "type": "Attribute",
        },
    )
