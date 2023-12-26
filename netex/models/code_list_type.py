from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CodeListType:
    value: List[str] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
    code_space: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSpace",
            "type": "Attribute",
        },
    )
