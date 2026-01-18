from __future__ import annotations

from dataclasses import dataclass

from .code_with_authority_type import CodeWithAuthorityType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Identifier(CodeWithAuthorityType):
    class Meta:
        name = "identifier"
        namespace = "http://www.opengis.net/gml/3.2"
