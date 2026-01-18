from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CodeListType:
    value: Iterable[str] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
    code_space: str | None = field(
        default=None,
        metadata={
            "name": "codeSpace",
            "type": "Attribute",
        },
    )
