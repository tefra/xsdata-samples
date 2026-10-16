from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MandatoryEnumeration(StrEnum):
    REQUIRED = "required"
    OPTIONAL = "optional"
    NOT_ALLOWED = "notAllowed"
