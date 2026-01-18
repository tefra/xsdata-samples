from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class BayGeometryEnumeration(Enum):
    UNSPECIFIED = "unspecified"
    ORTHOGONAL = "orthogonal"
    ANGLED = "angled"
    PARALLEL = "parallel"
    FREE_FORMAT = "freeFormat"
    OTHER = "other"
