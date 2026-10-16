from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SeriesPresentationEnumeration(StrEnum):
    NONE = "none"
    REQUIRED = "required"
    OPTIONAL_LEFT = "optionalLeft"
    OPTIONAL_RIGHT = "optionalRight"
