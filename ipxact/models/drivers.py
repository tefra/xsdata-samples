from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.driver import Driver

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class Drivers:
    """
    Container for wire port driver elements.

    :ivar driver: Wire port driver element. If no range is specified,
        default value applies to the entire range.
    """

    class Meta:
        name = "drivers"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    driver: list[Driver] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
