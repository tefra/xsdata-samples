from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.w3.org/2006/02/addressing/wsdl"


class AnonymousType(Enum):
    OPTIONAL = "optional"
    REQUIRED = "required"
    PROHIBITED = "prohibited"
