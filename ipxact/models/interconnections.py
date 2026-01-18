from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.interconnection import Interconnection
from ipxact.models.monitor_interconnection import MonitorInterconnection

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class Interconnections:
    """
    Connections between internal sub components.
    """

    class Meta:
        name = "interconnections"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    interconnection: list[Interconnection] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    monitor_interconnection: list[MonitorInterconnection] = field(
        default_factory=list,
        metadata={
            "name": "monitorInterconnection",
            "type": "Element",
        },
    )
