from dataclasses import dataclass, field
from typing import Optional

from .code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CodeWithAuthorityType(CodeType):
    code_space: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSpace",
            "type": "Attribute",
            "required": True,
        },
    )
