from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.ad_hoc_connection import AdHocConnection

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class AdHocConnections:
    """
    Defines the set of ad-hoc connections in a design.

    An ad-hoc connection represents a connection between two component pins
    which were not connected as a result of interface connections (i.e.the
    pin to pin connection was made explicitly and is represented
    explicitly).
    """

    class Meta:
        name = "adHocConnections"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    ad_hoc_connection: list[AdHocConnection] = field(
        default_factory=list,
        metadata={
            "name": "adHocConnection",
            "type": "Element",
            "min_occurs": 1,
        },
    )
