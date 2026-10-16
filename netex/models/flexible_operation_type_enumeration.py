from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class FlexibleOperationTypeEnumeration(StrEnum):
    FLEXIBLE_ROUTE = "flexibleRoute"
    FLEXIBLE_AREA = "flexibleArea"
    DEMAND_RESPONSIVE = "demandResponsive"
