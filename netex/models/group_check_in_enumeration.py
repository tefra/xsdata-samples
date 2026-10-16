from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class GroupCheckInEnumeration(StrEnum):
    NONE = "none"
    REQUIRED = "required"
    ALLOWED = "allowed"
