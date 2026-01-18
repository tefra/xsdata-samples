from __future__ import annotations

from dataclasses import dataclass

from .online_service_operator_ref_structure import (
    OnlineServiceOperatorRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OnlineServiceOperatorRef(OnlineServiceOperatorRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
