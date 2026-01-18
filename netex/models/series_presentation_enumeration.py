from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SeriesPresentationEnumeration(Enum):
    NONE = "none"
    REQUIRED = "required"
    OPTIONAL_LEFT = "optionalLeft"
    OPTIONAL_RIGHT = "optionalRight"
