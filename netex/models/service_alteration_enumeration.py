from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ServiceAlterationEnumeration(Enum):
    EXTRA_JOURNEY = "extraJourney"
    CANCELLATION = "cancellation"
    PLANNED = "planned"
    REPLACED = "replaced"
