from __future__ import annotations

from dataclasses import dataclass

from .online_service_operator_version_structure import (
    OnlineServiceOperatorVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OnlineServiceOperator(OnlineServiceOperatorVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
