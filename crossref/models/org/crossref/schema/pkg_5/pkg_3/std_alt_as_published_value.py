from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


class StdAltAsPublishedValue(Enum):
    EDITORIAL = "editorial"
    REVISION = "revision"
    REAPPROVAL = "reapproval"
    CORRECTION = "correction"
    AMENDMENT = "amendment"
