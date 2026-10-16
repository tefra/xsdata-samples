from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ServiceAlterationEnumeration(StrEnum):
    EXTRA_JOURNEY = "extraJourney"
    CANCELLATION = "cancellation"
    PLANNED = "planned"
    REPLACED = "replaced"
