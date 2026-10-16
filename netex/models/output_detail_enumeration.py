from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class OutputDetailEnumeration(StrEnum):
    ALL = "All"
    BASIC = "Basic"
    NO_GEOMETRY = "NoGeometry"
    XREF = "Xref"
    ALL_WITH_XREF = "AllWithXref"
