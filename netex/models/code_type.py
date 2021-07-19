from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CodeType:
    value: Optional[str] = field(
        default=None
    )
    code_space: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSpace",
            "type": "Attribute",
        }
    )
