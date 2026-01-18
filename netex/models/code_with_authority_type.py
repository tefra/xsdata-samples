from __future__ import annotations

from dataclasses import dataclass, field

from .code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class CodeWithAuthorityType(CodeType):
    code_space: str = field(
        metadata={
            "name": "codeSpace",
            "type": "Attribute",
            "required": True,
        }
    )
