from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class OutputDetailEnumeration(Enum):
    ALL = "All"
    BASIC = "Basic"
    NO_GEOMETRY = "NoGeometry"
    XREF = "Xref"
    ALL_WITH_XREF = "AllWithXref"
