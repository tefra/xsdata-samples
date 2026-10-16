from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LicenceRequirementsEnumeration(StrEnum):
    FULL = "full"
    PROVISIONAL = "provisional"
    ADDITIONAL = "additional"
    NONE = "none"
